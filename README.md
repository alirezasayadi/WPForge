# WPForge 🛠️

<p align="center">
  <strong>A cross-platform CLI tool for generating WordPress plugins from WordPress Plugin Boilerplate</strong>
</p>

<p align="center">
  <a href="https://github.com/alirezasayadi/WPForge/releases/latest">
    <img src="https://img.shields.io/github/v/release/alirezasayadi/WPForge?label=Latest%20Release" alt="Latest Release">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge/releases">
    <img src="https://img.shields.io/github/downloads/alirezasayadi/WPForge/total?label=Downloads" alt="Downloads">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge/releases">
    <img src="https://img.shields.io/github/release-date/alirezasayadi/WPForge?label=Released" alt="Release Date">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/alirezasayadi/WPForge/test-and-release.yml?label=Build%20%26%20Tests" alt="Build & Tests">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/alirezasayadi/WPForge" alt="License">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge">
    <img src="https://img.shields.io/github/stars/alirezasayadi/WPForge?style=flat" alt="GitHub Stars">
  </a>
</p>

<p align="center">
  <a href="README.fa.md">🇮🇷 راهنمای فارسی</a>
  ·
  <a href="https://github.com/alirezasayadi/WPForge/releases/latest">⬇️ Download</a>
  ·
  <a href="https://github.com/alirezasayadi/WPForge/releases">📦 Releases</a>
  ·
  <a href="https://github.com/alirezasayadi/WPForge/actions">⚙️ Actions</a>
</p>

---

## 📖 About

**WPForge** is a cross-platform command-line tool for quickly generating WordPress plugins using the structure of the **WordPress Plugin Boilerplate (WPPB)**.

It is designed to make starting a new WordPress plugin faster and easier by automatically creating the plugin structure and replacing common boilerplate information such as:

* Plugin name
* Plugin slug
* Plugin URL
* Author information
* Author email
* Author URL
* Plugin description

WPForge is written in **Python** and provides pre-built executables for:

* 🪟 Windows
* 🐧 Linux
* 🍎 macOS

Python does **not** need to be installed when using the pre-built releases.

---

## ✨ Features

* 🛠️ Generate WordPress plugins from WordPress Plugin Boilerplate
* 🪟 Windows support
* 🐧 Linux support
* 🍎 macOS support
* ⚡ Interactive CLI
* 🤖 Non-interactive CLI mode
* 📝 Automatic plugin metadata replacement
* 🔤 Automatic plugin slug conversion
* 📁 Automatic template file and directory renaming
* 👤 Author configuration support
* 🌐 Cross-platform configuration file
* 📦 Standalone executables
* 🔧 Works with the WordPress CLI (`wp`)
* 🚀 No Python installation required for pre-built releases
* 🔄 Available for multiple operating systems and architectures

---

## 📥 Download

[Latest Release](https://github.com/alirezasayadi/WPForge/releases/latest?utm_source=chatgpt.com)

### 🪟 Windows

Download the latest Windows executable and run it from PowerShell or Command Prompt.

For example:

```powershell
C:\Tools\WPForge\wpforge.exe
```

You should see:

```text
WPForge - WordPress Plugin Generator
```

#### Optional — Add WPForge to PATH

If you want to run:

```powershell
wpforge
```

from any directory, add the WPForge directory to your Windows `PATH`.

After adding it, restart PowerShell or Command Prompt.

Then run:

```powershell
wpforge --version
```

### 🐧 Linux

#### 1. Download WPForge

Open the latest release and download the Linux binary.

For example:

```text
wpforge-linux-x64
```

#### 2. Make it executable

Open Terminal:

```bash
chmod +x wpforge-linux-x64
```

#### 3. Run it

```bash
./wpforge-linux-x64
```

#### Optional — Install globally

You can move the executable to a directory in your `PATH`:

```bash
sudo mv wpforge-linux-x64 /usr/local/bin/wpforge
```

Then:

```bash
wpforge --version
```

You can now run WPForge from any directory.

### 🍎 macOS

#### 1. Download WPForge

Open the latest release and download the macOS build matching your Mac.

Available builds may include:

* Apple Silicon (ARM64)
* Intel (x64)

#### 2. Make the binary executable

Open Terminal:

```bash
chmod +x wpforge-macos-arm64
```

#### 3. Run WPForge

```bash
./wpforge-macos-arm64
```

#### Optional — Install globally

```bash
sudo mv wpforge-macos-arm64 /usr/local/bin/wpforge
```

Then:

```bash
wpforge --version
```

---

## 🐍 Python Installation

If you prefer running WPForge directly from source, Python is required.

### Requirements

* Python 3.10+
* pip

### Clone the repository

```bash
git clone https://github.com/alirezasayadi/WPForge.git
```

Enter the directory:

```bash
cd WPForge
```

### Create a virtual environment

#### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run WPForge

```bash
python main.py
```

---

## 🚀 Usage

WPForge supports both:

* Interactive mode
* Non-interactive mode

---

## 🧑‍💻 Interactive Mode

Interactive mode is recommended for beginners.

Simply run:

```bash
wpforge
```

or:

```bash
wpforge new
```

WPForge will ask you for the required information.

### Example

```text
Plugin name: My Awesome Plugin
Plugin slug: my-awesome-plugin
Plugin URL: https://example.com/my-plugin
Author name: John Doe
Author email: john@example.com
Author URL: https://example.com
Plugin description: My awesome WordPress plugin
```

After entering the information, WPForge generates the plugin automatically.

---

## 📁 Where Is the Plugin Created?

WPForge creates the plugin inside the current directory.

For example:

```text
wordpress/
└── wp-content/
    └── plugins/
        └── my-awesome-plugin/
```

If you run:

```bash
cd /path/to/wordpress/wp-content/plugins
```

then:

```bash
wpforge new
```

will create:

```text
wp-content/
└── plugins/
    └── my-awesome-plugin/
```

WPForge also checks whether the current directory looks like:

```text
wp-content/plugins
```

If it does not, WPForge displays a warning.

---

## ⚙️ Non-Interactive Mode

Non-interactive mode is useful for:

* Scripts
* Automation
* CI/CD
* GitHub Actions
* Developers who already know the required values

Use:

```bash
wpforge new --non-interactive \
  --plugin-name "My Plugin" \
  --plugin-slug my-plugin \
  --plugin-url https://example.com/my-plugin \
  --author-name "John Doe" \
  --author-email john@example.com \
  --author-url https://example.com \
  --plugin-description "My WordPress plugin"
```

### Windows PowerShell

Use backticks:

```powershell
wpforge new --non-interactive `
  --plugin-name "My Plugin" `
  --plugin-slug my-plugin `
  --plugin-url https://example.com/my-plugin `
  --author-name "John Doe" `
  --author-email john@example.com `
  --author-url https://example.com `
  --plugin-description "My WordPress plugin"
```

Or simply use one line:

```powershell
wpforge new --non-interactive --plugin-name "My Plugin" --plugin-slug my-plugin --plugin-url https://example.com/my-plugin --author-name "John Doe" --author-email john@example.com --author-url https://example.com --plugin-description "My WordPress plugin"
```

---

## 📋 Command Options

Run:

```bash
wpforge new --help
```

Available options:

| Option                 | Description                 |
| ---------------------- | --------------------------- |
| `--plugin-name`        | Plugin name                 |
| `--plugin-slug`        | Plugin slug                 |
| `--plugin-url`         | Plugin URL                  |
| `--author-name`        | Author name                 |
| `--author-email`       | Author email                |
| `--author-url`         | Author URL                  |
| `--plugin-description` | Plugin description          |
| `--non-interactive`    | Disable interactive prompts |

---

## 🔤 Plugin Slug

The plugin slug must contain:

* Lowercase letters
* Numbers
* Hyphens

### Valid

```text
my-plugin
woocommerce-tools
plugin123
my-plugin-123
advanced-discount
```

### Invalid

```text
My Plugin
my_plugin
My-Plugin
-my-plugin
my--plugin
```

The slug is also used to generate PHP naming conventions.

For example:

```text
my-awesome-plugin
```

becomes:

```text
my_awesome_plugin
```

and:

```text
MyAwesomePlugin
```

---

## 👤 Configuration

WPForge supports a configuration file named:

```text
.wpforge
```

The file is stored in the user's home directory.

### Windows

Usually:

```text
C:\Users\YourName\.wpforge
```

### Linux / macOS

Usually:

```text
~/.wpforge
```

### Configuration Example

Create:

```text
.wpforge
```

with:

```ini
author=John Doe
authorEmail=john@example.com
authorUrl=https://example.com
```

WPForge will automatically use these values as defaults.

This is especially useful if you create plugins frequently.

---

## 🧪 Example

Suppose you run:

```bash
wpforge new
```

and enter:

```text
Plugin name: Advanced Security
Plugin slug: advanced-security
Plugin URL: https://example.com/advanced-security
Author name: John Doe
Author email: john@example.com
Author URL: https://example.com
Plugin description: Advanced security tools for WordPress.
```

WPForge creates:

```text
advanced-security/
```

with the WordPress Plugin Boilerplate structure.

The generated files are automatically updated with the provided information.

---

## 🔧 WordPress CLI

After generating the plugin, you can activate it using WP-CLI:

```bash
wp plugin activate my-plugin
```

For example:

```bash
wp plugin activate advanced-security
```

Make sure WP-CLI is installed and you are running the command from your WordPress installation.

---

## 📦 Releases

WPForge releases are published on GitHub.

[View all releases](https://github.com/alirezasayadi/WPForge/releases?utm_source=chatgpt.com)

Each release may contain builds for:

* 🪟 Windows
* 🐧 Linux
* 🍎 macOS
* 🐍 Python/source

### Recommended Version

For most users, download the latest stable release.

You do not need to download the source code unless you want to develop WPForge itself.

---

## 🔄 Updating WPForge

### Windows

Download the new Windows release and replace the old executable.

### Linux

Download the latest binary and replace the existing installation:

```bash
sudo mv wpforge-linux-x64 /usr/local/bin/wpforge
```

### macOS

Download the latest macOS binary and replace the previous version.

### Python

If running from source:

```bash
git pull
```

Then update dependencies:

```bash
pip install -r requirements.txt --upgrade
```

---

## 🛠️ Development

Clone the repository:

```bash
git clone https://github.com/alirezasayadi/WPForge.git
```

Enter the project:

```bash
cd WPForge
```

Create a virtual environment.

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

Show help:

```bash
python main.py --help
```

Create a plugin:

```bash
python main.py new
```

---

## 🏗️ Building WPForge

WPForge can be packaged as a standalone executable using **PyInstaller**.

The generated executable does not require Python to be installed on the target machine.

Build instructions may vary depending on the target operating system.

GitHub Actions automatically builds release packages for supported platforms.

---

## 🤖 GitHub Actions

WPForge uses GitHub Actions to automate:

* Testing
* Building
* Packaging
* Release creation

The project is designed to produce platform-specific builds for:

* Windows
* Linux
* macOS

Release artifacts are attached automatically to GitHub Releases.

---

## 🧩 Project Structure

```text
WPForge/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── templates/
│   └── wordpress-plugin/
│       └── plugin-name/
└── .github/
    └── workflows/
        └── release.yml
```

The `templates/wordpress-plugin/plugin-name` directory contains the WordPress Plugin Boilerplate template used by WPForge.

---

## 📚 Based On

WPForge is inspired by and based on the work of:

* Tmeister's WPPB CLI
* WordPress Plugin Boilerplate

WPForge provides its own CLI implementation and tooling around the WordPress Plugin Boilerplate structure.

---

## 📄 License

WPForge is licensed under the **GNU General Public License v2.0 or later (GPL-2.0-or-later)**.

See:

```text
LICENSE
```

for the complete license text.

---

## 🤝 Contributing

Contributions are welcome.

If you find a bug or have an idea:

1. Open an issue.
2. Describe the problem or feature.
3. Provide reproduction steps when applicable.
4. Submit a pull request if you have a fix.

---

## 🐛 Bug Reports

When reporting a bug, please include:

* Operating system
* WPForge version
* Python version (if running from source)
* Command used
* Full error message
* Steps to reproduce the problem

Example:

```text
OS: Windows 11
WPForge: v1.0.0
Python: 3.12

Command:
wpforge new

Error:
...
```

---
## 🚀 Creating a Release

WPForge uses Git tags to create new releases.

When a new version tag such as `v1.0.0` is pushed to GitHub, GitHub Actions automatically:

- 🪟 Builds Windows x64
- 🐧 Builds Linux x64
- 🍎 Builds macOS ARM64
- 🍎 Builds macOS Intel x64
- 🔐 Generates SHA-256 checksums
- 📦 Creates a GitHub Release
- ⬆️ Uploads all compiled binaries to the release
- 📝 Generates release notes

You do not need to manually build the application for each operating system.

---

### 📋 Release Requirements

Before creating a release, make sure:

1. Your working tree is clean.
2. All changes have been committed.
3. You are on the correct branch.
4. The project builds successfully.
5. The version number is correct.

Check your Git status:

```bash
git status
````

You should ideally see:

```text
nothing to commit, working tree clean
```

---

# 🪟 Windows

WPForge includes:

```text
scripts/release.bat
```

This script is intended for Windows users.

### 1. Open Command Prompt

Open **Command Prompt (CMD)** and go to the WPForge directory:

```bat
cd D:\WPForge
```

You can also use another directory if WPForge is located elsewhere.

### 2. Run the release script

For example, to release version `1.0.0`:

```bat
scripts\release.bat 1.0.0
```

The script will create and push:

```text
v1.0.0
```

to GitHub.

### 3. What happens next?

After the tag is pushed:

```text
release.bat
    ↓
Git commit
    ↓
Git tag v1.0.0
    ↓
Push tag to GitHub
    ↓
GitHub Actions starts
    ↓
Build Windows
Build Linux
Build macOS ARM64
Build macOS x64
    ↓
Generate SHA256SUMS.txt
    ↓
Create GitHub Release
    ↓
Upload release files
```

You can monitor the build from:

**GitHub → Actions**

---

# 🐧 Linux / 🍎 macOS

WPForge also includes:

```text
scripts/release.sh
```

The same script can be used on Linux and macOS.

### 1. Open Terminal

Go to the WPForge directory:

```bash
cd /path/to/WPForge
```

For example:

```bash
cd ~/WPForge
```

### 2. Make the script executable

You only need to do this once:

```bash
chmod +x scripts/release.sh
```

### 3. Create a release

For example:

```bash
./scripts/release.sh 1.0.0
```

This creates:

```text
v1.0.0
```

and pushes the tag to GitHub.

GitHub Actions will then automatically build all supported platforms.

---

# 🔢 Versioning

WPForge releases use the following format:

```text
MAJOR.MINOR.PATCH
```

For example:

```text
1.0.0
1.0.1
1.1.0
2.0.0
```

The Git tag automatically receives the `v` prefix:

```text
v1.0.0
v1.0.1
v1.1.0
v2.0.0
```

### Version examples

Bug fix:

```text
1.0.0 → 1.0.1
```

New backward-compatible feature:

```text
1.0.0 → 1.1.0
```

Breaking change:

```text
1.0.0 → 2.0.0
```

---

# ⚠️ Important

Do **not** manually create the GitHub Release when using the release scripts.

The release process is automated.

You only need to create and push the version tag.

GitHub Actions will create the Release automatically.

---

# 🛠️ Manual Release

If you do not want to use the provided scripts, you can create a release manually.

First commit your changes:

```bash
git add .
git commit -m "Release v1.0.0"
```

Create the tag:

```bash
git tag v1.0.0
```

Push the branch:

```bash
git push origin main
```

Push the tag:

```bash
git push origin v1.0.0
```

After the tag is pushed, GitHub Actions automatically starts the release workflow.

---

# 🔍 Checking the Release

After pushing the tag, open the GitHub repository and go to:

```text
Actions
```

You should see:

```text
Build and Release WPForge
```

Wait until all jobs finish successfully.

The workflow should produce:

```text
Windows x64
Linux x64
macOS ARM64
macOS Intel x64
SHA256SUMS.txt
```

The final files will be available under:

```text
GitHub
  → Releases
    → WPForge v1.0.0
```

---

# 📦 Release Files

A typical WPForge release contains:

```text
WPForge-v1.0.0-Windows-x64.exe
WPForge-v1.0.0-Linux-x64
WPForge-v1.0.0-macOS-arm64
WPForge-v1.0.0-macOS-x64
SHA256SUMS.txt
```

### Windows

Download:

```text
WPForge-v1.0.0-Windows-x64.exe
```

No Python installation is required.

### Linux

Download:

```text
WPForge-v1.0.0-Linux-x64
```

Then:

```bash
chmod +x WPForge-v1.0.0-Linux-x64
```

Run:

```bash
./WPForge-v1.0.0-Linux-x64
```

### macOS Apple Silicon

For Apple Silicon Macs such as M1, M2, M3 and M4:

```text
WPForge-v1.0.0-macOS-arm64
```

Run:

```bash
chmod +x WPForge-v1.0.0-macOS-arm64
./WPForge-v1.0.0-macOS-arm64
```

### macOS Intel

For Intel-based Macs:

```text
WPForge-v1.0.0-macOS-x64
```

Run:

```bash
chmod +x WPForge-v1.0.0-macOS-x64
./WPForge-v1.0.0-macOS-x64
```

---

# 🔐 SHA-256 Checksums

Every release includes:

```text
SHA256SUMS.txt
```

This file contains SHA-256 hashes for the release binaries.

You can use it to verify that a downloaded file has not been corrupted or modified.

### Windows

PowerShell:

```powershell
Get-FileHash .\WPForge-v1.0.0-Windows-x64.exe -Algorithm SHA256
```

### Linux

```bash
sha256sum WPForge-v1.0.0-Linux-x64
```

### macOS

```bash
shasum -a 256 WPForge-v1.0.0-macOS-arm64
```

Compare the generated hash with the corresponding value in:

```text
SHA256SUMS.txt
```

---

# ❌ If a Release Fails

If GitHub Actions fails:

1. Open the repository on GitHub.
2. Go to **Actions**.
3. Open the failed workflow.
4. Select the failed job.
5. Check the error message.

Do not immediately create another tag with the same version.

For example, if:

```text
v1.0.0
```

failed, fix the problem first.

Then use a new patch version:

```text
v1.0.1
```

unless the original tag can safely be deleted and recreated.

---

# 💡 Recommended Release Workflow

For normal development, the recommended workflow is:

```text
1. Make changes
      ↓
2. Test locally
      ↓
3. Commit changes
      ↓
4. Run release.bat / release.sh
      ↓
5. Tag vX.Y.Z is pushed
      ↓
6. GitHub Actions builds all platforms
      ↓
7. GitHub Release is created
      ↓
8. Users download the binaries
```

This keeps the release process simple and consistent across Windows, Linux and macOS.

```

## ⭐ Support the Project

If WPForge is useful to you:

⭐ Star the repository on GitHub.

You can also report bugs, suggest features, and contribute code.

<p align="center">
  Made with ❤️ by
  <a href="https://github.com/alirezasayadi">Alireza Sayadi</a>
</p>
