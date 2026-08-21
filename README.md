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


- Plugin name
- Plugin slug
- Plugin URL
- Author information
- Author email
- Author URL
- Plugin description


WPForge is written in **Python** and provides pre-built executables for:


- 🪟 Windows
- 🐧 Linux
- 🍎 macOS


Python does **not** need to be installed when using the pre-built releases.


---


## ✨ Features


- 🛠️ Generate WordPress plugins from WordPress Plugin Boilerplate
- 🪟 Windows support
- 🐧 Linux support
- 🍎 macOS support
- ⚡ Interactive CLI
- 🤖 Non-interactive CLI mode
- 📝 Automatic plugin metadata replacement
- 🔤 Automatic plugin slug conversion
- 📁 Automatic template file and directory renaming
- 👤 Author configuration support
- 🌐 Cross-platform configuration file
- 📦 Standalone executables
- 🔧 Works with the WordPress CLI (`wp`)
- 🚀 No Python installation required for pre-built releases
- 🔄 Available for multiple operating systems and architectures


---


# 📥 Download
Run WPForge

Open PowerShell or Command Prompt:

C:\Tools\WPForge\wpforge.exe

You should see:

WPForge - WordPress Plugin Generator
Optional — Add WPForge to PATH

If you want to run:

wpforge

from any directory, add the WPForge directory to your Windows PATH.

After adding it, restart PowerShell.

Then run:

wpforge --version
🐧 Linux
1. Download WPForge

Open the latest release and download the Linux binary.

For example:

wpforge-linux-x64
2. Make it executable

Open Terminal:

chmod +x wpforge-linux-x64
3. Run it
./wpforge-linux-x64
Optional — Install globally

You can move the executable to a directory in your PATH:

sudo mv wpforge-linux-x64 /usr/local/bin/wpforge

Then:

wpforge --version

You can now run WPForge from any directory.

🍎 macOS
1. Download WPForge

Open the latest release.

Download the macOS build matching your Mac.

For example:

Apple Silicon (ARM64)
Intel (x64)
2. Make the binary executable

Open Terminal:

chmod +x wpforge-macos-arm64
3. Run WPForge
./wpforge-macos-arm64
Optional — Install globally
sudo mv wpforge-macos-arm64 /usr/local/bin/wpforge

Then:

wpforge --version
🐍 Python Installation

If you prefer running WPForge directly from source, Python is required.

Requirements
Python 3.10+
pip

Clone the repository:

git clone https://github.com/alirezasayadi/WPForge.git

Enter the directory:

cd WPForge

Create a virtual environment:

Windows
python -m venv .venv

Activate it:

.venv\Scripts\activate
Linux / macOS
python3 -m venv .venv

Activate it:

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run WPForge:

python main.py
🚀 Usage

WPForge supports both:

Interactive mode
Non-interactive mode
🧑‍💻 Interactive Mode

Interactive mode is recommended for beginners.

Simply run:

wpforge

Or:

wpforge new

WPForge will ask you for the required information.

Example:

Plugin name: My Awesome Plugin
Plugin slug: my-awesome-plugin
Plugin URL: https://example.com/my-plugin
Author name: John Doe
Author email: john@example.com
Author URL: https://example.com
Plugin description: My awesome WordPress plugin

After entering the information, WPForge generates the plugin automatically.

📁 Where Is The Plugin Created?

WPForge creates the plugin inside the current directory.

For example:

wordpress/
└── wp-content/
    └── plugins/
        └── my-awesome-plugin/

If you run:

cd /path/to/wordpress/wp-content/plugins

then:

wpforge new

will create:

wp-content/plugins/my-awesome-plugin/

WPForge also checks whether the current directory looks like:

wp-content/plugins

If it does not, WPForge displays a warning.

⚙️ Non-Interactive Mode

Non-interactive mode is useful for:

Scripts
Automation
CI/CD
GitHub Actions
Developers who already know the required values

Use:

wpforge new --non-interactive \
  --plugin-name "My Plugin" \
  --plugin-slug my-plugin \
  --plugin-url https://example.com/my-plugin \
  --author-name "John Doe" \
  --author-email john@example.com \
  --author-url https://example.com \
  --plugin-description "My WordPress plugin"
Windows PowerShell

Use backticks or write the command on one line:

wpforge new --non-interactive `
  --plugin-name "My Plugin" `
  --plugin-slug my-plugin `
  --plugin-url https://example.com/my-plugin `
  --author-name "John Doe" `
  --author-email john@example.com `
  --author-url https://example.com `
  --plugin-description "My WordPress plugin"

Or simply:

wpforge new --non-interactive --plugin-name "My Plugin" --plugin-slug my-plugin --plugin-url https://example.com/my-plugin --author-name "John Doe" --author-email john@example.com --author-url https://example.com --plugin-description "My WordPress plugin"
📋 Command Options

Run:

wpforge new --help

You will see the available options.

Option	Description
--plugin-name	Plugin name
--plugin-slug	Plugin slug
--plugin-url	Plugin URL
--author-name	Author name
--author-email	Author email
--author-url	Author URL
--plugin-description	Plugin description
--non-interactive	Disable interactive prompts
🔤 Plugin Slug

The plugin slug must contain:

Lowercase letters
Numbers
Hyphens
Valid
my-plugin
woocommerce-tools
plugin123
my-plugin-123
advanced-discount
Invalid
My Plugin
my_plugin
My-Plugin
-my-plugin
my--plugin

The slug is also used to generate PHP naming conventions.

For example:

my-awesome-plugin

becomes:

my_awesome_plugin

and:

MyAwesomePlugin
👤 Configuration

WPForge supports a configuration file named:

.wpforge

The file is stored in the user's home directory.

Windows

Usually:

C:\Users\YourName\.wpforge
Linux / macOS

Usually:

~/.wpforge
Configuration Example

Create:

.wpforge

with:

author=John Doe
authorEmail=john@example.com
authorUrl=https://example.com

WPForge will automatically use these values as defaults.

This is especially useful if you create plugins frequently.

🧪 Example

Suppose you run:

wpforge new

and enter:

Plugin name:
Advanced Security


Plugin slug:
advanced-security


Plugin URL:
https://example.com/advanced-security


Author name:
John Doe


Author email:
john@example.com


Author URL:
https://example.com


Plugin description:
Advanced security tools for WordPress.

WPForge creates:

advanced-security/

with the WordPress Plugin Boilerplate structure.

The generated files are automatically updated with the provided information.

🔧 WordPress CLI

After generating the plugin, you can activate it using WP-CLI:

wp plugin activate my-plugin

For example:

wp plugin activate advanced-security

Make sure WP-CLI is installed and you are running the command from your WordPress installation.

📦 Releases

WPForge releases are published on GitHub.

📦 View all releases

Each release may contain builds for:

🪟 Windows
🐧 Linux
🍎 macOS
🐍 Python/source
Recommended Version

For most users, download the latest stable release.

You do not need to download the source code unless you want to develop WPForge itself.

🔄 Updating WPForge
Windows

Download the new Windows release and replace the old executable.

Linux

Download the new binary and replace the existing installation:

sudo mv wpforge-linux-x64 /usr/local/bin/wpforge
macOS

Download the latest macOS binary and replace the previous version.

Python

If running from source:

git pull

Then update dependencies:

pip install -r requirements.txt --upgrade
🛠️ Development

Clone the repository:

git clone https://github.com/alirezasayadi/WPForge.git

Enter the project:

cd WPForge

Create a virtual environment.

Windows
python -m venv .venv
.venv\Scripts\activate
Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run:

python main.py

Show help:

python main.py --help

Create a plugin:

python main.py new
🏗️ Building WPForge

WPForge can be packaged as a standalone executable using PyInstaller.

The generated executable does not require Python to be installed on the target machine.

Build instructions may vary depending on the target operating system.

GitHub Actions automatically builds release packages for supported platforms.

🤖 GitHub Actions

WPForge uses GitHub Actions to automate:

Testing
Building
Packaging
Release creation

The project is designed to produce platform-specific builds for:

Windows
Linux
macOS

Release artifacts are attached automatically to GitHub Releases.

🧩 Project Structure
WPForge/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── templates/
│   └── wordpress-plugin/
│       └── plugin-name/
│
└── .github/
    └── workflows/
        └── test-and-release.yml

The templates/wordpress-plugin/plugin-name directory contains the WordPress Plugin Boilerplate template used by WPForge.

📚 Based On

WPForge is inspired by and based on the work of:

Tmeister's WPPB CLI
WordPress Plugin Boilerplate

WPForge provides its own CLI implementation and tooling around the WordPress Plugin Boilerplate structure.

📄 License

WPForge is licensed under the GNU General Public License v2.0 or later (GPL-2.0-or-later).

See:

LICENSE

for the complete license text.

🤝 Contributing

Contributions are welcome.

If you find a bug or have an idea:

Open an issue.
Describe the problem or feature.
Provide reproduction steps when applicable.
Submit a pull request if you have a fix.
🐛 Bug Reports

When reporting a bug, please include:

Operating system
WPForge version
Python version (if running from source)
Command used
Full error message
Steps to reproduce the problem

Example:

OS: Windows 11
WPForge: v1.0.0
Python: 3.12


Command:
wpforge new


Error:
...
⭐ Support the Project

If WPForge is useful to you:

⭐ Star the repository on GitHub.

You can also report bugs, suggest features, and contribute code.

<p align="center"> Made with ❤️ by <a href="https://github.com/alirezasayadi">Alireza Sayadi</a> </p> ```
