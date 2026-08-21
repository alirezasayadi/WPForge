# WPForge 🛠️

<p align="center">
  <strong>ابزار خط فرمان چندسکویی برای ساخت سریع افزونه‌های وردپرس بر پایه WordPress Plugin Boilerplate</strong>
</p>

<p align="center">
  <a href="https://github.com/alirezasayadi/WPForge/releases/latest">
    <img src="https://img.shields.io/github/v/release/alirezasayadi/WPForge?label=Latest%20Release" alt="آخرین نسخه">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge/releases">
    <img src="https://img.shields.io/github/downloads/alirezasayadi/WPForge/total?label=Downloads" alt="دانلودها">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge/releases">
    <img src="https://img.shields.io/github/release-date/alirezasayadi/WPForge?label=Released" alt="تاریخ انتشار">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/alirezasayadi/WPForge/test-and-release.yml?label=Build%20%26%20Tests" alt="Build & Tests">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/alirezasayadi/WPForge" alt="مجوز">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge">
    <img src="https://img.shields.io/github/stars/alirezasayadi/WPForge?style=flat" alt="ستاره‌ها">
  </a>
</p>

<p align="center">
  <a href="README.md">🇬🇧 English Documentation</a>
  ·
  <a href="https://github.com/alirezasayadi/WPForge/releases/latest">⬇️ دانلود</a>
  ·
  <a href="https://github.com/alirezasayadi/WPForge/releases">📦 نسخه‌ها</a>
  ·
  <a href="https://github.com/alirezasayadi/WPForge/actions">⚙️ Actions</a>
</p>

---

## 📖 درباره WPForge

**WPForge** یک ابزار خط فرمان چندسکویی است که برای ساخت سریع افزونه‌های وردپرس با استفاده از ساختار **WordPress Plugin Boilerplate (WPPB)** طراحی شده است.

هدف WPForge این است که شروع ساخت یک افزونه جدید وردپرس را سریع‌تر و ساده‌تر کند. این ابزار به‌صورت خودکار ساختار افزونه را ایجاد کرده و اطلاعات رایج Boilerplate را با اطلاعات موردنظر شما جایگزین می‌کند.

اطلاعاتی که WPForge به‌صورت خودکار مدیریت می‌کند:

* نام افزونه
* Slug افزونه
* آدرس افزونه
* نام نویسنده
* ایمیل نویسنده
* آدرس نویسنده
* توضیحات افزونه

WPForge با **Python** نوشته شده و نسخه‌های آماده اجرا برای سیستم‌عامل‌های زیر ارائه می‌دهد:

* 🪟 Windows
* 🐧 Linux
* 🍎 macOS

در صورت استفاده از نسخه‌های آماده، نیازی به نصب Python ندارید.

---

## ✨ امکانات

* 🛠️ ساخت افزونه وردپرس بر پایه WordPress Plugin Boilerplate
* 🪟 پشتیبانی از Windows
* 🐧 پشتیبانی از Linux
* 🍎 پشتیبانی از macOS
* ⚡ حالت تعاملی CLI
* 🤖 حالت غیرتعاملی CLI
* 📝 جایگزینی خودکار اطلاعات افزونه
* 🔤 تبدیل خودکار Slug افزونه
* 📁 تغییر نام خودکار فایل‌ها و پوشه‌های Template
* 👤 پشتیبانی از تنظیمات نویسنده
* 🌐 فایل تنظیمات مشترک بین سیستم‌عامل‌ها
* 📦 فایل اجرایی مستقل
* 🔧 سازگار با WordPress CLI (`wp`)
* 🚀 عدم نیاز به نصب Python در نسخه‌های آماده
* 🔄 ارائه نسخه برای سیستم‌عامل‌ها و معماری‌های مختلف

---

## 📥 دانلود

[آخرین نسخه WPForge](https://github.com/alirezasayadi/WPForge/releases/latest?utm_source=chatgpt.com)

---

## 🪟 Windows

### ۱. دانلود WPForge

آخرین نسخه WPForge را از بخش Releases دانلود کنید و فایل اجرایی Windows را دریافت کنید.

برای مثال:

```text
wpforge.exe
```

### ۲. اجرای WPForge

PowerShell یا Command Prompt را باز کنید و فایل را اجرا کنید:

```powershell
C:\Tools\WPForge\wpforge.exe
```

در صورت اجرای صحیح، باید چیزی مشابه زیر مشاهده کنید:

```text
WPForge - WordPress Plugin Generator
```

### افزودن اختیاری WPForge به PATH

اگر می‌خواهید بتوانید از هر پوشه‌ای فقط با اجرای دستور زیر WPForge را اجرا کنید:

```powershell
wpforge
```

پوشه‌ای که فایل `wpforge.exe` در آن قرار دارد را به `PATH` ویندوز اضافه کنید.

پس از اضافه کردن PATH، PowerShell یا Command Prompt را مجدداً باز کنید.

سپس بررسی کنید:

```powershell
wpforge --version
```

---

## 🐧 Linux

### ۱. دانلود WPForge

به بخش آخرین Release بروید و نسخه Linux متناسب با سیستم خود را دانلود کنید.

برای مثال:

```text
wpforge-linux-x64
```

### ۲. قابل اجرا کردن فایل

ترمینال را باز کرده و اجرا کنید:

```bash
chmod +x wpforge-linux-x64
```

### ۳. اجرای WPForge

```bash
./wpforge-linux-x64
```

### نصب اختیاری به‌صورت سراسری

می‌توانید فایل را به یکی از مسیرهای موجود در `PATH` منتقل کنید:

```bash
sudo mv wpforge-linux-x64 /usr/local/bin/wpforge
```

سپس:

```bash
wpforge --version
```

اکنون می‌توانید WPForge را از هر مسیری اجرا کنید.

---

## 🍎 macOS

### ۱. دانلود WPForge

آخرین Release را باز کرده و نسخه مناسب Mac خود را دانلود کنید.

نسخه‌های قابل ارائه ممکن است شامل موارد زیر باشند:

* Apple Silicon (ARM64)
* Intel (x64)

### ۲. قابل اجرا کردن فایل

برای Apple Silicon:

```bash
chmod +x wpforge-macos-arm64
```

### ۳. اجرای WPForge

```bash
./wpforge-macos-arm64
```

### نصب اختیاری به‌صورت سراسری

```bash
sudo mv wpforge-macos-arm64 /usr/local/bin/wpforge
```

سپس:

```bash
wpforge --version
```

---

## 🐍 اجرای WPForge با Python

اگر ترجیح می‌دهید WPForge را مستقیماً از Source اجرا کنید، باید Python نصب داشته باشید.

### پیش‌نیازها

* Python 3.10 یا بالاتر
* pip

### دریافت Source

```bash
git clone https://github.com/alirezasayadi/WPForge.git
```

وارد پوشه پروژه شوید:

```bash
cd WPForge
```

### ساخت Virtual Environment

#### Windows

```powershell
python -m venv .venv
```

فعال‌سازی:

```powershell
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv
```

فعال‌سازی:

```bash
source .venv/bin/activate
```

### نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

### اجرای WPForge

```bash
python main.py
```

---

## 🚀 نحوه استفاده

WPForge از دو حالت اصلی پشتیبانی می‌کند:

* حالت تعاملی (Interactive)
* حالت غیرتعاملی (Non-Interactive)

---

## 🧑‍💻 حالت تعاملی

حالت تعاملی برای کاربران تازه‌کار پیشنهاد می‌شود.

کافی است دستور زیر را اجرا کنید:

```bash
wpforge
```

یا:

```bash
wpforge new
```

WPForge اطلاعات موردنیاز را از شما دریافت می‌کند.

### نمونه

```text
Plugin name: My Awesome Plugin
Plugin slug: my-awesome-plugin
Plugin URL: https://example.com/my-plugin
Author name: John Doe
Author email: john@example.com
Author URL: https://example.com
Plugin description: My awesome WordPress plugin
```

پس از وارد کردن اطلاعات، WPForge افزونه را به‌صورت خودکار ایجاد می‌کند.

---

## 📁 افزونه کجا ساخته می‌شود؟

WPForge افزونه را در **پوشه فعلی** ایجاد می‌کند.

برای مثال اگر ساختار وردپرس شما به شکل زیر باشد:

```text
wordpress/
└── wp-content/
    └── plugins/
```

و وارد این پوشه شوید:

```bash
cd /path/to/wordpress/wp-content/plugins
```

سپس اجرا کنید:

```bash
wpforge new
```

افزونه در این مسیر ساخته می‌شود:

```text
wp-content/
└── plugins/
    └── my-awesome-plugin/
```

WPForge همچنین بررسی می‌کند که پوشه فعلی شبیه مسیر زیر باشد:

```text
wp-content/plugins
```

اگر مسیر فعلی مناسب نباشد، WPForge یک هشدار نمایش می‌دهد.

---

## ⚙️ حالت غیرتعاملی

حالت غیرتعاملی برای موارد زیر مناسب است:

* Scriptها
* Automation
* CI/CD
* GitHub Actions
* توسعه‌دهندگانی که اطلاعات افزونه را از قبل می‌دانند

### Linux / macOS

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

در PowerShell می‌توانید از Backtick استفاده کنید:

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

یا همه پارامترها را در یک خط بنویسید:

```powershell
wpforge new --non-interactive --plugin-name "My Plugin" --plugin-slug my-plugin --plugin-url https://example.com/my-plugin --author-name "John Doe" --author-email john@example.com --author-url https://example.com --plugin-description "My WordPress plugin"
```

---

## 📋 گزینه‌های دستورات

برای مشاهده گزینه‌های موجود اجرا کنید:

```bash
wpforge new --help
```

| گزینه                  | توضیحات                  |
| ---------------------- | ------------------------ |
| `--plugin-name`        | نام افزونه               |
| `--plugin-slug`        | Slug افزونه              |
| `--plugin-url`         | آدرس افزونه              |
| `--author-name`        | نام نویسنده              |
| `--author-email`       | ایمیل نویسنده            |
| `--author-url`         | آدرس نویسنده             |
| `--plugin-description` | توضیحات افزونه           |
| `--non-interactive`    | غیرفعال کردن حالت تعاملی |

---

## 🔤 قوانین Plugin Slug

Slug افزونه باید شامل موارد زیر باشد:

* حروف کوچک انگلیسی
* اعداد
* خط تیره (`-`)

### نمونه‌های معتبر

```text
my-plugin
woocommerce-tools
plugin123
my-plugin-123
advanced-discount
```

### نمونه‌های نامعتبر

```text
My Plugin
my_plugin
My-Plugin
-my-plugin
my--plugin
```

Slug علاوه بر نام پوشه افزونه، برای تولید برخی نام‌گذاری‌های PHP نیز استفاده می‌شود.

برای مثال:

```text
my-awesome-plugin
```

به:

```text
my_awesome_plugin
```

تبدیل می‌شود.

همچنین:

```text
MyAwesomePlugin
```

---

## 👤 تنظیمات

WPForge از یک فایل تنظیمات با نام زیر پشتیبانی می‌کند:

```text
.wpforge
```

این فایل در Home Directory کاربر ذخیره می‌شود.

### Windows

معمولاً:

```text
C:\Users\YourName\.wpforge
```

### Linux / macOS

معمولاً:

```text
~/.wpforge
```

### نمونه فایل تنظیمات

فایل `.wpforge` را ایجاد کرده و موارد زیر را داخل آن قرار دهید:

```ini
author=John Doe
authorEmail=john@example.com
authorUrl=https://example.com
```

WPForge به‌صورت خودکار از این اطلاعات به‌عنوان مقادیر پیش‌فرض استفاده می‌کند.

این قابلیت برای افرادی که به‌طور مداوم افزونه ایجاد می‌کنند بسیار کاربردی است.

---

## 🧪 مثال کامل

فرض کنید دستور زیر را اجرا می‌کنید:

```bash
wpforge new
```

و اطلاعات زیر را وارد می‌کنید:

```text
Plugin name: Advanced Security
Plugin slug: advanced-security
Plugin URL: https://example.com/advanced-security
Author name: John Doe
Author email: john@example.com
Author URL: https://example.com
Plugin description: Advanced security tools for WordPress.
```

WPForge پوشه زیر را ایجاد می‌کند:

```text
advanced-security/
```

این پوشه شامل ساختار WordPress Plugin Boilerplate خواهد بود.

فایل‌های تولیدشده نیز به‌صورت خودکار با اطلاعات واردشده به‌روزرسانی می‌شوند.

---

## 🔧 استفاده از WordPress CLI

پس از ساخت افزونه، می‌توانید آن را با استفاده از WP-CLI فعال کنید:

```bash
wp plugin activate my-plugin
```

برای مثال:

```bash
wp plugin activate advanced-security
```

اطمینان حاصل کنید که WP-CLI نصب شده باشد و دستور را از داخل نصب وردپرس اجرا کنید.

---

## 📦 نسخه‌ها و Releases

نسخه‌های WPForge در GitHub منتشر می‌شوند.

[مشاهده همه نسخه‌ها](https://github.com/alirezasayadi/WPForge/releases?utm_source=chatgpt.com)

هر Release ممکن است شامل نسخه‌های زیر باشد:

* 🪟 Windows
* 🐧 Linux
* 🍎 macOS
* 🐍 Python / Source

### نسخه پیشنهادی

برای اکثر کاربران، استفاده از آخرین نسخه پایدار پیشنهاد می‌شود.

اگر فقط قصد استفاده از WPForge را دارید، نیازی به دانلود Source Code ندارید.

Source Code بیشتر برای توسعه خود WPForge کاربرد دارد.

---

## 🔄 به‌روزرسانی WPForge

### Windows

نسخه جدید Windows را دانلود کرده و فایل اجرایی قبلی را با نسخه جدید جایگزین کنید.

### Linux

نسخه جدید را دانلود کرده و فایل قبلی را جایگزین کنید:

```bash
sudo mv wpforge-linux-x64 /usr/local/bin/wpforge
```

### macOS

نسخه جدید macOS را دانلود کرده و فایل اجرایی قبلی را جایگزین کنید.

### Python

اگر WPForge را از Source اجرا می‌کنید:

```bash
git pull
```

سپس وابستگی‌ها را به‌روزرسانی کنید:

```bash
pip install -r requirements.txt --upgrade
```

---

## 🛠️ توسعه WPForge

Repository را Clone کنید:

```bash
git clone https://github.com/alirezasayadi/WPForge.git
```

وارد پروژه شوید:

```bash
cd WPForge
```

یک Virtual Environment ایجاد کنید.

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

وابستگی‌ها را نصب کنید:

```bash
pip install -r requirements.txt
```

اجرای پروژه:

```bash
python main.py
```

نمایش راهنما:

```bash
python main.py --help
```

ساخت افزونه:

```bash
python main.py new
```

---

## 🏗️ ساخت فایل اجرایی

WPForge را می‌توان با استفاده از **PyInstaller** به یک فایل اجرایی مستقل تبدیل کرد.

فایل اجرایی تولیدشده برای اجرا روی سیستم مقصد به نصب Python نیاز ندارد.

دستورالعمل Build ممکن است بسته به سیستم‌عامل مقصد متفاوت باشد.

GitHub Actions نیز به‌صورت خودکار Buildهای مربوط به سیستم‌عامل‌های پشتیبانی‌شده را تولید می‌کند.

---

## 🤖 GitHub Actions

WPForge از GitHub Actions برای خودکارسازی موارد زیر استفاده می‌کند:

* تست
* Build
* Package
* ساخت Release

این پروژه برای تولید Buildهای مخصوص سیستم‌عامل‌های زیر طراحی شده است:

* Windows
* Linux
* macOS

فایل‌های خروجی نیز به‌صورت خودکار به GitHub Releases اضافه می‌شوند.

---

## 🧩 ساختار پروژه

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

پوشه:

```text
templates/wordpress-plugin/plugin-name
```

شامل Template مربوط به WordPress Plugin Boilerplate است که WPForge برای ساخت افزونه‌ها از آن استفاده می‌کند.

---

## 📚 بر پایه چه پروژه‌هایی ساخته شده است؟

WPForge از پروژه‌ها و کارهای زیر الهام گرفته و بر پایه ساختار آن‌ها توسعه داده شده است:

* Tmeister's WPPB CLI
* WordPress Plugin Boilerplate

WPForge پیاده‌سازی CLI و ابزارهای اختصاصی خود را برای کار با ساختار WordPress Plugin Boilerplate ارائه می‌دهد.

---

## 📄 مجوز

WPForge تحت مجوز:

**GNU General Public License v2.0 or later (GPL-2.0-or-later)**

منتشر می‌شود.

برای مشاهده متن کامل مجوز:

```text
LICENSE
```

را مشاهده کنید.

---

## 🤝 مشارکت در پروژه

مشارکت در توسعه WPForge آزاد است.

اگر با مشکلی مواجه شدید یا ایده‌ای برای بهبود پروژه دارید:

1. یک Issue ایجاد کنید.
2. مشکل یا قابلیت پیشنهادی را توضیح دهید.
3. در صورت امکان، مراحل بازتولید مشکل را ارائه کنید.
4. اگر راه‌حل یا اصلاحی برای مشکل دارید، یک Pull Request ارسال کنید.

---

## 🐛 گزارش خطا

هنگام گزارش یک Bug، اطلاعات زیر را ارائه کنید:

* سیستم‌عامل
* نسخه WPForge
* نسخه Python در صورت اجرای Source
* دستور استفاده‌شده
* متن کامل خطا
* مراحل بازتولید مشکل

### نمونه

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

## ⭐ حمایت از پروژه

اگر WPForge برای شما مفید است:

⭐ به Repository پروژه در GitHub Star بدهید.

همچنین می‌توانید:

* Bug گزارش کنید.
* قابلیت جدید پیشنهاد دهید.
* در توسعه پروژه مشارکت کنید.

<p align="center">
  ساخته‌شده با ❤️ توسط
  <a href="https://github.com/alirezasayadi">علیرضا صیادی</a>
</p>
