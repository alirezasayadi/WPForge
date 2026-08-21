from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urlparse

import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text


APP_NAME = "WPForge"
APP_VERSION = "1.0.1"

CONFIG_FILE_NAME = ".wpforge"

TEMPLATE_RELATIVE_PATH = (
    Path("templates")
    / "wordpress-plugin"
    / "plugin-name"
)

TEXT_EXTENSIONS = {
    ".php",
    ".js",
    ".css",
    ".scss",
    ".sass",
    ".less",
    ".html",
    ".htm",
    ".txt",
    ".md",
    ".json",
    ".xml",
    ".yml",
    ".yaml",
    ".po",
    ".pot",
    ".ini",
    ".conf",
    ".dist",
    ".sh",
    ".bat",
    ".cmd",
}

console = Console()


class WPForgeException(Exception):
    """Raised when WPForge cannot complete an operation."""


# ============================================================================
# UI
# ============================================================================

def print_banner() -> None:
    """Print the WPForge banner."""

    banner = r"""
 __          _______  ______
 \ \        / /  __ \|  ____|
  \ \  /\  / /| |__) | |__ ___  _ __ __ _  ___
   \ \/  \/ / |  ___/|  __/ _ \| '__/ _` |/ _ \
    \  /\  /  | |    | | | (_) | | | (_| |  __/
     \/  \/   |_|    |_|  \___/|_|  \__, |\___|
                                     __/ |
                                    |___/

         WordPress Plugin Generator
    """

    console.print(
        Text(
            banner,
            style="blue bold",
        )
    )


def print_success(message: str) -> None:
    console.print(f"[green]✓[/green] {message}")


def print_error(message: str) -> None:
    console.print(f"[red]✗[/red] {message}")


def print_info(message: str) -> None:
    console.print(f"[blue]ℹ[/blue] {message}")


def print_warning(message: str) -> None:
    console.print(f"[yellow]⚠[/yellow] {message}")


# ============================================================================
# Configuration
# ============================================================================

def get_config_path() -> Path:
    """Return the user's WPForge configuration path."""

    return Path.home() / CONFIG_FILE_NAME


def read_config_file() -> dict[str, str]:
    """
    Read the WPForge configuration file.

    Example:

        author=John Doe
        authorEmail=john@example.com
        authorUrl=https://example.com
    """

    config_path = get_config_path()

    if not config_path.is_file():
        return {}

    config: dict[str, str] = {}

    try:
        with config_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            for line in file:
                line = line.strip()

                if (
                    not line
                    or line.startswith("#")
                    or "=" not in line
                ):
                    continue

                key, value = line.split("=", 1)

                config[key.strip()] = value.strip()

    except OSError as error:
        print_warning(
            f"Unable to read {config_path}: {error}"
        )
        return {}

    required_keys = {
        "author",
        "authorEmail",
        "authorUrl",
    }

    if not required_keys.issubset(config):
        print_warning(
            f"The {CONFIG_FILE_NAME} configuration file "
            "is incomplete."
        )
        return {}

    return config


# ============================================================================
# Validation
# ============================================================================

def validate_plugin_slug(value: str) -> bool:
    """
    Validate a WordPress plugin slug.

    Valid examples:

        my-plugin
        woocommerce-discount
        plugin123
        my-plugin-123
    """

    return bool(
        re.fullmatch(
            r"[a-z0-9]+(?:-[a-z0-9]+)*",
            value,
        )
    )


def validate_url(value: str) -> bool:
    """Validate an HTTP or HTTPS URL."""

    try:
        result = urlparse(value)
    except ValueError:
        return False

    return (
        result.scheme in {"http", "https"}
        and bool(result.netloc)
    )


def validate_email(value: str) -> bool:
    """Validate an email address."""

    return bool(
        re.fullmatch(
            r"[a-zA-Z0-9._%+-]+@"
            r"[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            value,
        )
    )


# ============================================================================
# Template
# ============================================================================

def get_template_directory() -> Path:
    """
    Locate the bundled WordPress plugin template.

    Supports both normal Python execution and PyInstaller builds.
    """

    candidates = [
        Path(__file__).resolve().parent
        / TEMPLATE_RELATIVE_PATH,
    ]

    bundle_root = getattr(
        sys,
        "_MEIPASS",
        None,
    )

    if bundle_root:
        candidates.append(
            Path(bundle_root)
            / TEMPLATE_RELATIVE_PATH
        )

    for candidate in candidates:
        if candidate.is_dir():
            return candidate

    searched_paths = "\n".join(
        str(path)
        for path in candidates
    )

    raise WPForgeException(
        "WordPress plugin template was not found.\n\n"
        "Searched locations:\n"
        f"{searched_paths}"
    )


def replace_plugin_header(
    content: str,
    *,
    plugin_name: str,
    plugin_url: str,
    plugin_description: str,
    author_name: str,
    author_email: str,
    author_url: str,
) -> str:
    """
    Replace WordPress plugin header fields.

    Header replacement is based on field names rather than the
    original boilerplate text, so changes to the template wording
    do not break plugin generation.
    """

    fields = {
        "Plugin Name": plugin_name,
        "Plugin URI": plugin_url,
        "Description": plugin_description,
        "Author": author_name,
        "Author URI": author_url,
        "Author Email": author_email,
    }

    for field, value in fields.items():
        pattern = (
            rf"(^\s*\*\s*{re.escape(field)}:"
            rf"\s*).*$"
        )

        content = re.sub(
            pattern,
            lambda match: f"{match.group(1)}{value}",
            content,
            flags=re.MULTILINE,
        )

    return content


# ============================================================================
# File handling
# ============================================================================

def is_text_file(path: Path) -> bool:
    """Return whether a file should be treated as text."""

    return (
        path.name.startswith(".")
        or path.suffix.lower() in TEXT_EXTENSIONS
    )


def replace_in_file(
    path: Path,
    replacements: dict[str, str],
) -> None:
    """Replace template placeholders inside a text file."""

    if not is_text_file(path):
        return

    try:
        content = path.read_text(
            encoding="utf-8",
        )
    except UnicodeDecodeError:
        return
    except OSError as error:
        raise WPForgeException(
            f"Unable to read file:\n"
            f"{path}\n\n"
            f"{error}"
        ) from error

    for old, new in replacements.items():
        content = content.replace(
            old,
            new,
        )

    try:
        path.write_text(
            content,
            encoding="utf-8",
        )
    except OSError as error:
        raise WPForgeException(
            f"Unable to write file:\n"
            f"{path}\n\n"
            f"{error}"
        ) from error


def replace_strings(
    directory: Path,
    replacements: dict[str, str],
) -> None:
    """Replace placeholders throughout a plugin directory."""

    for path in directory.rglob("*"):
        if path.is_file():
            replace_in_file(
                path,
                replacements,
            )


def replace_plugin_headers(
    directory: Path,
    *,
    plugin_name: str,
    plugin_url: str,
    plugin_description: str,
    author_name: str,
    author_email: str,
    author_url: str,
) -> None:
    """Update WordPress plugin headers in PHP files."""

    for path in directory.rglob("*.php"):
        try:
            content = path.read_text(
                encoding="utf-8",
            )
        except UnicodeDecodeError:
            continue
        except OSError as error:
            raise WPForgeException(
                f"Unable to read file:\n"
                f"{path}\n\n"
                f"{error}"
            ) from error

        updated_content = replace_plugin_header(
            content,
            plugin_name=plugin_name,
            plugin_url=plugin_url,
            plugin_description=plugin_description,
            author_name=author_name,
            author_email=author_email,
            author_url=author_url,
        )

        if updated_content == content:
            continue

        try:
            path.write_text(
                updated_content,
                encoding="utf-8",
            )
        except OSError as error:
            raise WPForgeException(
                f"Unable to write file:\n"
                f"{path}\n\n"
                f"{error}"
            ) from error


def rename_template_paths(
    directory: Path,
    plugin_slug: str,
) -> None:
    """
    Rename template files and directories containing
    'plugin-name'.

    Example:

        plugin-name.php

    becomes:

        my-plugin.php
    """

    paths = sorted(
        directory.rglob("*"),
        key=lambda path: len(path.parts),
        reverse=True,
    )

    for path in paths:
        if "plugin-name" not in path.name:
            continue

        new_path = path.with_name(
            path.name.replace(
                "plugin-name",
                plugin_slug,
            )
        )

        if new_path.exists():
            raise WPForgeException(
                f"Cannot rename:\n"
                f"{path}\n"
                f"to:\n"
                f"{new_path}\n\n"
                "The destination already exists."
            )

        try:
            path.rename(new_path)
        except OSError as error:
            raise WPForgeException(
                f"Unable to rename:\n"
                f"{path}\n"
                f"to:\n"
                f"{new_path}\n\n"
                f"{error}"
            ) from error


# ============================================================================
# Plugin generation
# ============================================================================

def create_plugin(
    destination: Path,
    plugin_slug: str,
    plugin_name: str,
    plugin_url: str,
    author_name: str,
    author_email: str,
    author_url: str,
    plugin_description: str,
) -> None:
    """Create a new WordPress plugin from the bundled template."""

    template_directory = get_template_directory()

    if destination.exists():
        raise WPForgeException(
            f"A folder named '{plugin_slug}' already exists."
        )

    try:
        shutil.copytree(
            template_directory,
            destination,
        )

        snake_case = plugin_slug.replace(
            "-",
            "_",
        )

        pascal_case = "".join(
            part.capitalize()
            for part in plugin_slug.split("-")
        )

        upper_snake = snake_case.upper()

        # These replacements handle PHP identifiers and template
        # placeholders throughout the project.
        replacements = {
            "Plugin_Name": pascal_case,
            "PLUGIN_NAME_VERSION": (
                f"{upper_snake}_VERSION"
            ),
            "plugin_name": snake_case,
            "plugin-name": plugin_slug,
        }

        replace_strings(
            destination,
            replacements,
        )

        # Plugin metadata is handled separately so it does not depend
        # on the exact wording used by the boilerplate template.
        replace_plugin_headers(
            destination,
            plugin_name=plugin_name,
            plugin_url=plugin_url,
            plugin_description=plugin_description,
            author_name=author_name,
            author_email=author_email,
            author_url=author_url,
        )

        rename_template_paths(
            destination,
            plugin_slug,
        )

    except WPForgeException:
        shutil.rmtree(
            destination,
            ignore_errors=True,
        )
        raise

    except OSError as error:
        shutil.rmtree(
            destination,
            ignore_errors=True,
        )

        raise WPForgeException(
            f"Unable to create plugin:\n"
            f"{error}"
        ) from error


# ============================================================================
# WordPress directory detection
# ============================================================================

def is_wordpress_plugin_directory(
    path: Path,
) -> bool:
    """Check whether a path looks like wp-content/plugins."""

    normalized = (
        str(path)
        .replace("\\", "/")
        .rstrip("/")
        .lower()
    )

    return normalized.endswith(
        "/wp-content/plugins"
    )


# ============================================================================
# Interactive prompts
# ============================================================================

def prompt_plugin_slug(
    value: str | None,
) -> str:
    """Prompt for and validate a plugin slug."""

    while True:
        result = value or click.prompt(
            "Plugin slug",
            default="sample-plugin",
        )

        if validate_plugin_slug(result):
            return result

        print_error(
            "Plugin slug must use lowercase letters, "
            "numbers and single hyphens."
        )

        value = None


def prompt_url(
    message: str,
    value: str | None,
    default: str,
) -> str:
    """Prompt for and validate an HTTP/HTTPS URL."""

    while True:
        result = value or click.prompt(
            message,
            default=default,
        )

        if validate_url(result):
            return result

        print_error(
            "Please enter a valid HTTP/HTTPS URL."
        )

        value = None


def prompt_email(
    value: str | None,
    default: str,
) -> str:
    """Prompt for and validate an email address."""

    while True:
        result = value or click.prompt(
            "Author email",
            default=default,
        )

        if validate_email(result):
            return result

        print_error(
            "Please enter a valid email address."
        )

        value = None


# ============================================================================
# New command
# ============================================================================

@click.command()
@click.option(
    "--plugin-name",
    help="Plugin name.",
)
@click.option(
    "--plugin-slug",
    help="Plugin slug.",
)
@click.option(
    "--plugin-url",
    help="Plugin URL.",
)
@click.option(
    "--author-name",
    help="Author name.",
)
@click.option(
    "--author-email",
    help="Author email.",
)
@click.option(
    "--author-url",
    help="Author URL.",
)
@click.option(
    "--plugin-description",
    help="Plugin description.",
)
@click.option(
    "--non-interactive",
    is_flag=True,
    help="Disable interactive prompts.",
)
def new(
    plugin_name: str | None,
    plugin_slug: str | None,
    plugin_url: str | None,
    author_name: str | None,
    author_email: str | None,
    author_url: str | None,
    plugin_description: str | None,
    non_interactive: bool,
) -> None:
    """Create a new WordPress plugin."""

    print_banner()

    current_directory = Path.cwd()

    # ------------------------------------------------------------------------
    # WordPress directory warning
    # ------------------------------------------------------------------------

    if not is_wordpress_plugin_directory(
        current_directory
    ):
        print_warning(
            "Current directory does not look like "
            "wp-content/plugins."
        )

        if (
            not non_interactive
            and not click.confirm(
                "Continue anyway?",
                default=False,
            )
        ):
            print_error(
                "Plugin creation cancelled."
            )

            raise click.Abort()

    # ------------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------------

    config = read_config_file()

    # ------------------------------------------------------------------------
    # Non-interactive mode
    # ------------------------------------------------------------------------

    if non_interactive:
        parameters = {
            "--plugin-name": plugin_name,
            "--plugin-slug": plugin_slug,
            "--plugin-url": plugin_url,
            "--author-name": author_name,
            "--author-email": author_email,
            "--author-url": author_url,
            "--plugin-description": plugin_description,
        }

        missing = [
            name
            for name, value in parameters.items()
            if not value
        ]

        if missing:
            raise click.UsageError(
                "Missing required options in "
                "--non-interactive mode:\n\n"
                + "\n".join(
                    f"  {item}"
                    for item in missing
                )
            )

    # ------------------------------------------------------------------------
    # Interactive mode
    # ------------------------------------------------------------------------

    else:
        plugin_name = (
            plugin_name
            or click.prompt(
                "Plugin name",
                default="Sample Plugin",
            )
        )

        plugin_slug = prompt_plugin_slug(
            plugin_slug,
        )

        plugin_url = prompt_url(
            "Plugin URL",
            plugin_url,
            "https://example.com",
        )

        author_name = (
            author_name
            or click.prompt(
                "Author name",
                default=config.get(
                    "author",
                    "John Doe",
                ),
            )
        )

        author_email = prompt_email(
            author_email,
            config.get(
                "authorEmail",
                "john.doe@example.com",
            ),
        )

        author_url = prompt_url(
            "Author URL",
            author_url,
            config.get(
                "authorUrl",
                "https://example.com",
            ),
        )

        plugin_description = (
            plugin_description
            or click.prompt(
                "Plugin description",
                default="This is a sample plugin.",
            )
        )

    # ------------------------------------------------------------------------
    # Type narrowing
    # ------------------------------------------------------------------------

    assert plugin_name
    assert plugin_slug
    assert plugin_url
    assert author_name
    assert author_email
    assert author_url
    assert plugin_description

    # ------------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------------

    if not validate_plugin_slug(plugin_slug):
        raise click.BadParameter(
            "Invalid plugin slug.",
            param_hint="--plugin-slug",
        )

    if not validate_url(plugin_url):
        raise click.BadParameter(
            "Invalid plugin URL.",
            param_hint="--plugin-url",
        )

    if not validate_url(author_url):
        raise click.BadParameter(
            "Invalid author URL.",
            param_hint="--author-url",
        )

    if not validate_email(author_email):
        raise click.BadParameter(
            "Invalid author email.",
            param_hint="--author-email",
        )

    # ------------------------------------------------------------------------
    # Destination
    # ------------------------------------------------------------------------

    destination = (
        current_directory
        / plugin_slug
    )

    if destination.exists():
        raise click.ClickException(
            f"A folder named '{plugin_slug}' "
            "already exists."
        )

    # ------------------------------------------------------------------------
    # Create plugin
    # ------------------------------------------------------------------------

    console.print()
    console.print(
        "[green]Starting plugin creation...[/green]"
    )

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn(
                "{task.description}"
            ),
            console=console,
        ) as progress:
            task = progress.add_task(
                "Creating plugin...",
                total=None,
            )

            create_plugin(
                destination=destination,
                plugin_slug=plugin_slug,
                plugin_name=plugin_name,
                plugin_url=plugin_url,
                author_name=author_name,
                author_email=author_email,
                author_url=author_url,
                plugin_description=plugin_description,
            )

            progress.update(
                task,
                completed=True,
            )

    except WPForgeException as error:
        raise click.ClickException(
            str(error)
        ) from error

    except Exception as error:
        shutil.rmtree(
            destination,
            ignore_errors=True,
        )

        raise click.ClickException(
            f"Unexpected error: {error}"
        ) from error

    # ------------------------------------------------------------------------
    # Success
    # ------------------------------------------------------------------------

    console.print()

    print_success(
        "Plugin created successfully!"
    )

    console.print(
        f"[blue]→[/blue] {destination}"
    )

    console.print()

    print_info(
        f"Activate the plugin with: "
        f"wp plugin activate {plugin_slug}"
    )

    print_success(
        "Start coding!"
    )


# ============================================================================
# Root CLI
# ============================================================================

@click.group(
    invoke_without_command=True,
)
@click.version_option(
    APP_VERSION,
    prog_name=APP_NAME,
)
@click.pass_context
def cli(
    ctx: click.Context,
) -> None:
    """WPForge - WordPress Plugin Generator."""

    if ctx.invoked_subcommand is None:
        print_banner()

        console.print(
            "Create a new WordPress plugin with:\n"
        )

        console.print(
            "    wpforge new"
        )

        console.print()

        console.print(
            "For help:"
        )

        console.print(
            "    wpforge --help"
        )


cli.add_command(new)


if __name__ == "__main__":
    cli()