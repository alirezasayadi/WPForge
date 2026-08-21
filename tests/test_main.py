from pathlib import Path

import pytest
from click.testing import CliRunner

import main


# ============================================================================
# Validation tests
# ============================================================================

@pytest.mark.parametrize(
    "slug",
    [
        "my-plugin",
        "woocommerce-tools",
        "plugin123",
        "my-plugin-123",
        "advanced-discount",
    ],
)
def test_valid_plugin_slug(slug):
    assert main.validate_plugin_slug(slug)


@pytest.mark.parametrize(
    "slug",
    [
        "",
        "My Plugin",
        "my_plugin",
        "My-Plugin",
        "-my-plugin",
        "my-plugin-",
        "my--plugin",
        "my.plugin",
        "my/plugin",
    ],
)
def test_invalid_plugin_slug(slug):
    assert not main.validate_plugin_slug(slug)


@pytest.mark.parametrize(
    "url",
    [
        "https://example.com",
        "http://example.com",
        "https://example.com/plugin",
        "https://www.example.com/",
    ],
)
def test_valid_url(url):
    assert main.validate_url(url)


@pytest.mark.parametrize(
    "url",
    [
        "",
        "example.com",
        "ftp://example.com",
        "not a url",
        "http://",
        "https://",
    ],
)
def test_invalid_url(url):
    assert not main.validate_url(url)


@pytest.mark.parametrize(
    "email",
    [
        "john@example.com",
        "john.doe@example.com",
        "test+wpforge@example.co",
        "developer@sub.example.com",
    ],
)
def test_valid_email(email):
    assert main.validate_email(email)


@pytest.mark.parametrize(
    "email",
    [
        "",
        "john@example",
        "john@",
        "@example.com",
        "john example@example.com",
        "john.example.com",
    ],
)
def test_invalid_email(email):
    assert not main.validate_email(email)


# ============================================================================
# WordPress path detection tests
# ============================================================================

def test_wordpress_plugin_directory(tmp_path):
    path = (
        tmp_path
        / "wordpress"
        / "wp-content"
        / "plugins"
    )

    path.mkdir(parents=True)

    assert main.is_wordpress_plugin_directory(path)


def test_non_wordpress_plugin_directory(tmp_path):
    path = tmp_path / "projects"

    path.mkdir()

    assert not main.is_wordpress_plugin_directory(path)


def test_windows_wordpress_plugin_directory():
    path = Path(
        r"C:\Users\Test\wordpress\wp-content\plugins"
    )

    assert main.is_wordpress_plugin_directory(path)


# ============================================================================
# File replacement tests
# ============================================================================

def test_replace_in_file(tmp_path):
    file_path = tmp_path / "test.php"

    file_path.write_text(
        "Hello plugin-name!",
        encoding="utf-8",
    )

    main.replace_in_file(
        file_path,
        {
            "plugin-name": "my-plugin",
        },
    )

    assert file_path.read_text(encoding="utf-8") == "Hello my-plugin!"


def test_replace_in_file_multiple_replacements(tmp_path):
    file_path = tmp_path / "test.php"

    file_path.write_text(
        "plugin-name plugin_name Plugin_Name",
        encoding="utf-8",
    )

    main.replace_in_file(
        file_path,
        {
            "plugin-name": "my-plugin",
            "plugin_name": "my_plugin",
            "Plugin_Name": "MyPlugin",
        },
    )

    assert file_path.read_text(encoding="utf-8") == (
        "my-plugin my_plugin MyPlugin"
    )


def test_replace_in_file_preserves_binary_file(tmp_path):
    file_path = tmp_path / "image.png"

    original = b"\x89PNG\r\n\x1a\n\x00\xff"

    file_path.write_bytes(original)

    main.replace_in_file(
        file_path,
        {
            "plugin-name": "my-plugin",
        },
    )

    assert file_path.read_bytes() == original


# ============================================================================
# Template path tests
# ============================================================================

def test_rename_template_paths(tmp_path):
    plugin_directory = tmp_path / "plugin"
    plugin_directory.mkdir()

    old_file = plugin_directory / "plugin-name.php"
    old_directory = plugin_directory / "plugin-name"

    old_file.write_text(
        "<?php",
        encoding="utf-8",
    )

    old_directory.mkdir()

    main.rename_template_paths(
        plugin_directory,
        "my-plugin",
    )

    assert not old_file.exists()
    assert not old_directory.exists()

    assert (plugin_directory / "my-plugin.php").is_file()
    assert (plugin_directory / "my-plugin").is_dir()


# ============================================================================
# Plugin generator tests
# ============================================================================

@pytest.fixture
def template_directory(tmp_path):
    template = tmp_path / "template"
    template.mkdir()

    plugin_file = template / "plugin-name.php"

    plugin_file.write_text(
        """<?php

/**
 * @package Plugin_Name
 *
 * @wordpress-plugin
 * Plugin Name:       WordPress Plugin Boilerplate
 * Plugin URI:        http://example.com/plugin-name-uri/
 * Description:       This is a short description.
 * Version:           1.0.0
 * Author:            Your Name or Your Company
 * Author URI:        http://example.com/
 * License:           GPL-2.0+
 * License URI:       http://www.gnu.org/licenses/gpl-2.0.txt
 * Text Domain:       plugin-name
 */

define( 'PLUGIN_NAME_VERSION', '1.0.0' );

$plugin_name = 'plugin_name';
""",
        encoding="utf-8",
    )

    return template


def test_create_plugin(
    tmp_path,
    monkeypatch,
    template_directory,
):
    monkeypatch.setattr(
        main,
        "get_template_directory",
        lambda: template_directory,
    )

    destination = tmp_path / "my-plugin"

    main.create_plugin(
        destination=destination,
        plugin_slug="my-plugin",
        plugin_name="My Awesome Plugin",
        plugin_url="https://example.com/my-plugin",
        author_name="John Doe",
        author_email="john@example.com",
        author_url="https://example.com",
        plugin_description="My awesome plugin.",
    )

    # Destination directory.
    assert destination.is_dir()

    # Main plugin file.
    plugin_file = destination / "my-plugin.php"

    assert plugin_file.is_file()

    content = plugin_file.read_text(
        encoding="utf-8",
    )

    # ------------------------------------------------------------------------
    # Plugin metadata
    # ------------------------------------------------------------------------

    assert "Plugin Name:       My Awesome Plugin" in content
    assert "Plugin URI:        https://example.com/my-plugin" in content
    assert "Description:       My awesome plugin." in content
    assert "Author:            John Doe" in content
    assert "Author URI:        https://example.com" in content

    # ------------------------------------------------------------------------
    # PHP naming conventions
    # ------------------------------------------------------------------------

    assert "MY_PLUGIN_VERSION" in content
    assert "$my_plugin" in content

    # ------------------------------------------------------------------------
    # Original boilerplate placeholders must be removed
    # ------------------------------------------------------------------------

    assert "WordPress Plugin Boilerplate" not in content
    assert "plugin-name" not in content
    assert "plugin_name" not in content
    assert "Plugin_Name" not in content
    assert "Your Name or Your Company" not in content


# ============================================================================
# CLI tests
# ============================================================================

def test_cli_version():
    runner = CliRunner()

    result = runner.invoke(
        main.cli,
        ["--version"],
    )

    assert result.exit_code == 0
    assert main.APP_VERSION in result.output


def test_cli_help():
    runner = CliRunner()

    result = runner.invoke(
        main.cli,
        ["--help"],
    )

    assert result.exit_code == 0
    assert "WPForge" in result.output


def test_new_help():
    runner = CliRunner()

    result = runner.invoke(
        main.cli,
        ["new", "--help"],
    )

    assert result.exit_code == 0

    expected_options = [
        "--plugin-name",
        "--plugin-slug",
        "--plugin-url",
        "--author-name",
        "--author-email",
        "--author-url",
        "--plugin-description",
        "--non-interactive",
    ]

    for option in expected_options:
        assert option in result.output