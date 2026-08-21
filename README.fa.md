# WPForge 🛠️

<p align="center">
  <strong>ابزار CLI چندسکویی برای ساخت افزونه‌های وردپرس بر پایه WordPress Plugin Boilerplate</strong>
</p>

<p align="center">
  <a href="https://github.com/alirezasayadi/WPForge/releases/latest">
    <img src="https://img.shields.io/github/v/release/alirezasayadi/WPForge?label=Latest%20Release" alt="آخرین نسخه">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge/releases">
    <img src="https://img.shields.io/github/downloads/alirezasayadi/WPForge/total?label=Downloads" alt="تعداد دانلودها">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge/releases">
    <img src="https://img.shields.io/github/release-date/alirezasayadi/WPForge?label=Released" alt="تاریخ انتشار">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/alirezasayadi/WPForge/test-and-release.yml?label=Build%20%26%20Tests" alt="ساخت و تست‌ها">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/alirezasayadi/WPForge" alt="مجوز">
  </a>
  <a href="https://github.com/alirezasayadi/WPForge">
    <img src="https://img.shields.io/github/stars/alirezasayadi/WPForge?style=flat" alt="ستاره‌های GitHub">
  </a>
</p>

<p align="center">
  <a href="README.md">🇬🇧 English</a>
  ·
  <a href="https://github.com/alirezasayadi/WPForge/releases/latest">⬇️ دانلود</a>
  ·
  <a href="https://github.com/alirezasayadi/WPForge/releases">📦 نسخه‌ها</a>
  ·
  <a href="https://github.com/alirezasayadi/WPForge/actions">⚙️ Actions</a>
</p>

---

## 📖 درباره WPForge

**WPForge** یک ابزار خط فرمان (CLI) چندسکویی است که برای ساخت سریع افزونه‌های وردپرس با استفاده از ساختار **WordPress Plugin Boilerplate (WPPB)** طراحی شده است.

هدف WPForge این است که شروع یک پروژه جدید افزونه وردپرس را سریع‌تر و ساده‌تر کند. این ابزار به‌صورت خودکار ساختار افزونه را ایجاد کرده و اطلاعات رایج موجود در Boilerplate را با اطلاعات موردنظر شما جایگزین می‌کند، از جمله:

* نام افزونه
* اسلاگ افزونه
* آدرس افزونه
* اطلاعات نویسنده
* ایمیل نویسنده
* آدرس نویسنده
* توضیحات افزونه

WPForge با **Python** نوشته شده و فایل‌های اجرایی آماده برای سیستم‌عامل‌های زیر ارائه می‌دهد:

* 🪟 Windows
* 🐧 Linux
* 🍎 macOS

در صورت استفاده از نسخه‌های اجرایی آماده، نیازی به نصب Python ندارید.

---

## ✨ امکانات

* 🛠️ ساخت افزونه‌های وردپرس بر اساس WordPress Plugin Boilerplate
* 🪟 پشتیبانی از Windows
* 🐧 پشتیبانی از Linux
* 🍎 پشتیبانی از macOS
* ⚡ رابط تعاملی خط فرمان
* 🤖 حالت غیرتعاملی CLI
* 📝 جایگزینی خودکار اطلاعات افزونه
* 🔤 تبدیل خودکار اسلاگ افزونه
* 📁 تغییر نام خودکار فایل‌ها و پوشه‌های Template
* 👤 پشتیبانی از تنظیمات نویسنده
* 🌐 فایل تنظیمات چندسکویی
* 📦 فایل‌های اجرایی مستقل
* 🔧 سازگار با WordPress CLI (`wp`)
* 🚀 بدون نیاز به نصب Python در نسخه‌های اجرایی آماده
* 🔄 ارائه نسخه‌های مختلف برای سیستم‌عامل‌ها و معماری‌های گوناگون

---

## 📥 دانلود

[آخرین نسخه](https://github.com/alirezasayadi/WPForge/releases/latest)

### 🪟 Windows

آخرین فایل اجرایی Windows را از بخش Releases دانلود کرده و آن را از طریق PowerShell یا Command Prompt اجرا کنید.

برای مثال:

```powershell
C:\Tools\WPForge\wpforge.exe
```

پس از اجرا باید چیزی مشابه زیر مشاهده کنید:

```text
WPForge - WordPress Plugin Generator
```

#### اختیاری — اضافه کردن WPForge به PATH

اگر می‌خواهید بتوانید دستور زیر را:

```powershell
wpforge
```

از هر پوشه‌ای اجرا کنید، مسیر پوشه WPForge را به متغیر `PATH` در Windows اضافه کنید.

پس از اضافه کردن مسیر، PowerShell یا Command Prompt را مجدداً باز کنید.

سپس اجرا کنید:

```powershell
wpforge --version
```

---

### 🐧 Linux

#### 1. دانلود WPForge

آخرین Release را باز کرده و فایل اجرایی Linux را دانلود کنید.

برای مثال:

```text
wpforge-linux-x64
```

#### 2. اجرایی کردن فایل

ترمینال را باز کرده و اجرا کنید:

```bash
chmod +x wpforge-linux-x64
```

#### 3. اجرای WPForge

```bash
./wpforge-linux-x64
```

#### اختیاری — نصب به‌صورت سراسری

می‌توانید فایل اجرایی را به یکی از مسیرهای موجود در `PATH` منتقل کنید:

```bash
sudo mv wpforge-linux-x64 /usr/local/bin/wpforge
```

سپس:

```bash
wpforge --version
```

اکنون می‌توانید WPForge را از هر مسیری اجرا کنید.

---

### 🍎 macOS

#### 1. دانلود WPForge

آخرین Release را باز کرده و نسخه مناسب Mac خود را دانلود کنید.

نسخه‌های موجود ممکن است شامل موارد زیر باشند:

* Apple Silicon (ARM64)
* Intel (x64)

#### 2. اجرایی کردن فایل

ترمینال را باز کرده و اجرا کنید:

```bash
chmod +x wpforge-macos-arm64
```

#### 3. اجرای WPForge

```bash
./wpforge-macos-arm64
```

#### اختیاری — نصب به‌صورت سراسری

```bash
sudo mv wpforge-macos-arm64 /usr/local/bin/wpforge
```

سپس:

```bash
wpforge --version
```

---

## 🐍 نصب Python

اگر ترجیح می‌دهید WPForge را مستقیماً از Source اجرا کنید، نصب Python ضروری است.

### پیش‌نیازها

* Python 3.10+
* pip

### دریافت Repository

```bash
git clone https://github.com/alirezasayadi/WPForge.git
```

وارد پوشه پروژه شوید:

```bash
cd WPForge
```

### ایجاد محیط مجازی

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

WPForge از دو حالت پشتیبانی می‌کند:

* حالت تعاملی
* حالت غیرتعاملی

---

## 🧑‍💻 حالت تعاملی

حالت تعاملی برای کاربران مبتدی پیشنهاد می‌شود.

کافی است اجرا کنید:

```bash
wpforge
```

یا:

```bash
wpforge new
```

WPForge اطلاعات موردنیاز را از شما دریافت می‌کند.

### مثال

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

## 📁 افزونه در کجا ایجاد می‌شود؟

WPForge افزونه را داخل پوشه‌ای که در حال حاضر در آن قرار دارید ایجاد می‌کند.

برای مثال:

```text
wordpress/
└── wp-content/
    └── plugins/
        └── my-awesome-plugin/
```

اگر اجرا کنید:

```bash
cd /path/to/wordpress/wp-content/plugins
```

سپس:

```bash
wpforge new
```

ساختار زیر ایجاد خواهد شد:

```text
wp-content/
└── plugins/
    └── my-awesome-plugin/
```

WPForge همچنین بررسی می‌کند که آیا مسیر فعلی شبیه مسیر زیر است یا خیر:

```text
wp-content/plugins
```

اگر مسیر فعلی این ساختار را نداشته باشد، WPForge یک هشدار نمایش می‌دهد.

---

## ⚙️ حالت غیرتعاملی

حالت غیرتعاملی برای موارد زیر مناسب است:

* اسکریپت‌ها
* اتوماسیون
* CI/CD
* GitHub Actions
* توسعه‌دهندگانی که مقادیر موردنیاز را از قبل می‌دانند

استفاده:

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

در PowerShell برای ادامه دادن دستور در خط بعد از Backtick استفاده کنید:

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

یا می‌توانید کل دستور را در یک خط بنویسید:

```powershell
wpforge new --non-interactive --plugin-name "My Plugin" --plugin-slug my-plugin --plugin-url https://example.com/my-plugin --author-name "John Doe" --author-email john@example.com --author-url https://example.com --plugin-description "My WordPress plugin"
```

---

## 📋 گزینه‌های دستورات

برای مشاهده راهنمای دستور اجرا کنید:

```bash
wpforge new --help
```

گزینه‌های موجود:

| گزینه                  | توضیحات                       |
| ---------------------- | ----------------------------- |
| `--plugin-name`        | نام افزونه                    |
| `--plugin-slug`        | اسلاگ افزونه                  |
| `--plugin-url`         | آدرس افزونه                   |
| `--author-name`        | نام نویسنده                   |
| `--author-email`       | ایمیل نویسنده                 |
| `--author-url`         | آدرس نویسنده                  |
| `--plugin-description` | توضیحات افزونه                |
| `--non-interactive`    | غیرفعال کردن ورودی‌های تعاملی |

---

## 🔤 اسلاگ افزونه

اسلاگ افزونه باید شامل موارد زیر باشد:

* حروف کوچک انگلیسی
* اعداد
* خط تیره (`-`)

### معتبر

```text
my-plugin
woocommerce-tools
plugin123
my-plugin-123
advanced-discount
```

### نامعتبر

```text
My Plugin
my_plugin
My-Plugin
-my-plugin
my--plugin
```

اسلاگ برای ایجاد نام‌گذاری‌های PHP نیز استفاده می‌شود.

برای مثال:

```text
my-awesome-plugin
```

به:

```text
my_awesome_plugin
```

و:

```text
MyAwesomePlugin
```

تبدیل می‌شود.

---

## 👤 تنظیمات

WPForge از یک فایل تنظیمات با نام زیر پشتیبانی می‌کند:

```text
.wpforge
```

این فایل در پوشه Home کاربر ذخیره می‌شود.

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

فایل زیر را ایجاد کنید:

```text
.wpforge
```

و داخل آن قرار دهید:

```ini
author=John Doe
authorEmail=john@example.com
authorUrl=https://example.com
```

WPForge به‌صورت خودکار از این مقادیر به‌عنوان مقادیر پیش‌فرض استفاده خواهد کرد.

این قابلیت مخصوصاً برای افرادی که به‌طور مداوم افزونه ایجاد می‌کنند بسیار کاربردی است.

---

## 🧪 مثال

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

و ساختار WordPress Plugin Boilerplate را داخل آن قرار می‌دهد.

فایل‌های ایجادشده نیز به‌صورت خودکار با اطلاعات واردشده به‌روزرسانی می‌شوند.

---

## 🔧 WordPress CLI

پس از ایجاد افزونه، می‌توانید آن را با استفاده از WP-CLI فعال کنید:

```bash
wp plugin activate my-plugin
```

برای مثال:

```bash
wp plugin activate advanced-security
```

اطمینان حاصل کنید که WP-CLI نصب شده باشد و دستور را از داخل نصب WordPress اجرا کنید.

---

## 📦 نسخه‌ها

نسخه‌های WPForge در GitHub منتشر می‌شوند.

[مشاهده تمام نسخه‌ها](https://github.com/alirezasayadi/WPForge/releases)

هر Release ممکن است شامل Buildهای زیر باشد:

* 🪟 Windows
* 🐧 Linux
* 🍎 macOS
* 🐍 Python/Source

### نسخه پیشنهادی

برای اکثر کاربران، دانلود آخرین نسخه پایدار پیشنهاد می‌شود.

در صورتی که قصد توسعه خود WPForge را ندارید، نیازی به دانلود Source Code نخواهید داشت.

---

## 🚀 ایجاد Release

WPForge از Git Tagها برای ایجاد نسخه‌های جدید استفاده می‌کند.

هنگامی که یک Tag جدید مانند `v1.0.0` به GitHub Push شود، GitHub Actions به‌صورت خودکار موارد زیر را انجام می‌دهد:

* 🪟 ساخت نسخه Windows x64
* 🐧 ساخت نسخه Linux x64
* 🍎 ساخت نسخه macOS ARM64
* 🍎 ساخت نسخه macOS Intel x64
* 🔐 ایجاد Checksumهای SHA-256
* 📦 ایجاد GitHub Release
* ⬆️ آپلود تمام فایل‌های کامپایل‌شده در Release
* 📝 ایجاد Release Notes

بنابراین نیازی نیست برنامه را برای هر سیستم‌عامل به‌صورت دستی Build کنید.

---

### 📋 پیش‌نیازهای انتشار Release

قبل از ایجاد Release، مطمئن شوید:

1. Working Tree شما تمیز است.
2. تمام تغییرات Commit شده‌اند.
3. روی Branch صحیح قرار دارید.
4. پروژه با موفقیت Build می‌شود.
5. شماره نسخه صحیح است.

وضعیت Git را بررسی کنید:

```bash
git status
```

در حالت ایده‌آل باید چیزی مشابه زیر مشاهده کنید:

```text
nothing to commit, working tree clean
```

---

### 🪟 Windows

WPForge شامل فایل زیر است:

```text
scripts/release.bat
```

این Script برای کاربران Windows طراحی شده است.

### 1. باز کردن Command Prompt

**Command Prompt (CMD)** را باز کرده و وارد پوشه WPForge شوید:

```bat
cd D:\WPForge
```

در صورتی که WPForge در مسیر دیگری قرار دارد، می‌توانید مسیر مربوط به خودتان را استفاده کنید.

### 2. اجرای Release Script

برای مثال، برای انتشار نسخه `1.0.0`:

```bat
scripts\release.bat 1.0.0
```

این Script، Tag زیر را ایجاد و به GitHub Push می‌کند:

```text
v1.0.0
```

### 3. بعد از آن چه اتفاقی می‌افتد؟

پس از Push شدن Tag:

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

می‌توانید فرآیند Build را از قسمت زیر مشاهده کنید:

**GitHub → Actions**

---

### 🐧 Linux / 🍎 macOS

WPForge همچنین شامل فایل زیر است:

```text
scripts/release.sh
```

این Script در Linux و macOS قابل استفاده است.

### 1. باز کردن Terminal

وارد پوشه WPForge شوید:

```bash
cd /path/to/WPForge
```

برای مثال:

```bash
cd ~/WPForge
```

### 2. اجرایی کردن Script

این کار را فقط یک بار انجام دهید:

```bash
chmod +x scripts/release.sh
```

### 3. ایجاد Release

برای مثال:

```bash
./scripts/release.sh 1.0.0
```

این دستور:

```text
v1.0.0
```

را ایجاد کرده و Tag را به GitHub Push می‌کند.

پس از آن GitHub Actions به‌صورت خودکار تمام Platformهای پشتیبانی‌شده را Build خواهد کرد.

---

### 🔢 نسخه‌بندی

نسخه‌های WPForge از فرمت زیر استفاده می‌کنند:

```text
MAJOR.MINOR.PATCH
```

برای مثال:

```text
1.0.0
1.0.1
1.1.0
2.0.0
```

Git Tag به‌صورت خودکار دارای پیشوند `v` خواهد بود:

```text
v1.0.0
v1.0.1
v1.1.0
v2.0.0
```

### مثال‌های نسخه‌بندی

رفع Bug:

```text
1.0.0 → 1.0.1
```

افزودن قابلیت جدید بدون ایجاد تغییر ناسازگار:

```text
1.0.0 → 1.1.0
```

تغییر ناسازگار (Breaking Change):

```text
1.0.0 → 2.0.0
```

---

### ⚠️ مهم

هنگام استفاده از Release Scriptها، **به‌صورت دستی GitHub Release ایجاد نکنید.**

فرآیند انتشار به‌صورت خودکار انجام می‌شود.

تنها کاری که باید انجام دهید، ایجاد و Push کردن Version Tag است.

GitHub Actions به‌صورت خودکار Release را ایجاد خواهد کرد.

---

### 🛠️ انتشار دستی

اگر نمی‌خواهید از Scriptهای ارائه‌شده استفاده کنید، می‌توانید Release را به‌صورت دستی ایجاد کنید.

ابتدا تغییرات خود را Commit کنید:

```bash
git add .
git commit -m "Release v1.0.0"
```

Tag را ایجاد کنید:

```bash
git tag v1.0.0
```

Branch را Push کنید:

```bash
git push origin main
```

سپس Tag را Push کنید:

```bash
git push origin v1.0.0
```

پس از Push شدن Tag، GitHub Actions به‌صورت خودکار Workflow مربوط به Release را اجرا می‌کند.

---

### 🔍 بررسی Release

پس از Push کردن Tag، Repository را در GitHub باز کرده و وارد بخش:

```text
Actions
```

شوید.

باید Workflow زیر را مشاهده کنید:

```text
Build and Release WPForge
```

صبر کنید تا تمام Jobها با موفقیت به پایان برسند.

Workflow باید فایل‌های زیر را تولید کند:

```text
Windows x64
Linux x64
macOS ARM64
macOS Intel x64
SHA256SUMS.txt
```

فایل‌های نهایی در مسیر زیر در دسترس خواهند بود:

```text
GitHub
  → Releases
    → WPForge v1.0.0
```

---

### 📦 فایل‌های Release

یک Release معمولی WPForge شامل فایل‌های زیر است:

```text
WPForge-v1.0.0-Windows-x64.exe
WPForge-v1.0.0-Linux-x64
WPForge-v1.0.0-macOS-arm64
WPForge-v1.0.0-macOS-x64
SHA256SUMS.txt
```

### Windows

دانلود کنید:

```text
WPForge-v1.0.0-Windows-x64.exe
```

نیازی به نصب Python نیست.

### Linux

دانلود کنید:

```text
WPForge-v1.0.0-Linux-x64
```

سپس:

```bash
chmod +x WPForge-v1.0.0-Linux-x64
```

اجرا:

```bash
./WPForge-v1.0.0-Linux-x64
```

### macOS Apple Silicon

برای Macهای مجهز به Apple Silicon مانند M1، M2، M3 و M4:

```text
WPForge-v1.0.0-macOS-arm64
```

اجرا:

```bash
chmod +x WPForge-v1.0.0-macOS-arm64
./WPForge-v1.0.0-macOS-arm64
```

### macOS Intel

برای Macهای مجهز به پردازنده Intel:

```text
WPForge-v1.0.0-macOS-x64
```

اجرا:

```bash
chmod +x WPForge-v1.0.0-macOS-x64
./WPForge-v1.0.0-macOS-x64
```

---

### 🔐 Checksumهای SHA-256

هر Release شامل فایل زیر است:

```text
SHA256SUMS.txt
```

این فایل شامل Hashهای SHA-256 فایل‌های اجرایی Release است.

با استفاده از این Hashها می‌توانید بررسی کنید که فایل دانلودشده خراب یا تغییر داده نشده باشد.

### Windows

در PowerShell:

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

Hash تولیدشده را با مقدار مربوط به همان فایل در:

```text
SHA256SUMS.txt
```

مقایسه کنید.

---

### ❌ اگر Release با خطا مواجه شد

اگر GitHub Actions با خطا مواجه شد:

1. Repository را در GitHub باز کنید.
2. وارد بخش **Actions** شوید.
3. Workflow ناموفق را باز کنید.
4. Job ناموفق را انتخاب کنید.
5. پیام خطا را بررسی کنید.

بلافاصله یک Tag دیگر با همان Version ایجاد نکنید.

برای مثال، اگر:

```text
v1.0.0
```

با خطا مواجه شد، ابتدا مشکل را برطرف کنید.

سپس از یک نسخه Patch جدید استفاده کنید:

```text
v1.0.1
```

مگر اینکه Tag قبلی را به‌صورت ایمن حذف و دوباره ایجاد کنید.

---

### 💡 فرآیند پیشنهادی انتشار

برای توسعه معمول، فرآیند زیر پیشنهاد می‌شود:

```text
1. ایجاد تغییرات
      ↓
2. تست محلی
      ↓
3. Commit کردن تغییرات
      ↓
4. اجرای release.bat / release.sh
      ↓
5. Push شدن Tag با نام vX.Y.Z
      ↓
6. Build تمام Platformها توسط GitHub Actions
      ↓
7. ایجاد GitHub Release
      ↓
8. دانلود فایل‌های اجرایی توسط کاربران
```

این روش باعث می‌شود فرآیند Release در Windows، Linux و macOS ساده و یکسان باقی بماند.

---

## 🔄 به‌روزرسانی WPForge

### Windows

نسخه جدید Windows را دانلود کرده و فایل اجرایی قبلی را با نسخه جدید جایگزین کنید.

### Linux

آخرین Binary را دانلود کرده و نصب فعلی را جایگزین کنید:

```bash
sudo mv wpforge-linux-x64 /usr/local/bin/wpforge
```

### macOS

آخرین Binary مربوط به macOS را دانلود کرده و نسخه قبلی را جایگزین کنید.

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

## 🛠️ توسعه

Repository را دریافت کنید:

```bash
git clone https://github.com/alirezasayadi/WPForge.git
```

وارد پروژه شوید:

```bash
cd WPForge
```

یک محیط مجازی ایجاد کنید.

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

اجرا:

```bash
python main.py
```

نمایش راهنما:

```bash
python main.py --help
```

ایجاد افزونه:

```bash
python main.py new
```

---

## 🏗️ ساخت WPForge

WPForge را می‌توان با استفاده از **PyInstaller** به یک فایل اجرایی مستقل تبدیل کرد.

فایل اجرایی ایجادشده برای اجرا روی سیستم مقصد نیازی به نصب Python ندارد.

دستورالعمل Build ممکن است بسته به سیستم‌عامل مقصد متفاوت باشد.

GitHub Actions به‌صورت خودکار Packageهای Release را برای Platformهای پشتیبانی‌شده ایجاد می‌کند.

---

## 🤖 GitHub Actions

WPForge از GitHub Actions برای خودکارسازی موارد زیر استفاده می‌کند:

* تست
* Build
* Package کردن
* ایجاد Release

این پروژه برای تولید Buildهای اختصاصی سیستم‌عامل‌های زیر طراحی شده است:

* Windows
* Linux
* macOS

Artifactهای Release به‌صورت خودکار به GitHub Releases اضافه می‌شوند.

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

شامل Template مربوط به WordPress Plugin Boilerplate است که توسط WPForge استفاده می‌شود.

---

## 📚 بر پایه

WPForge از پروژه‌ها و کارهای زیر الهام گرفته و بر پایه ساختار آن‌ها توسعه یافته است:

* Tmeister's WPPB CLI
* WordPress Plugin Boilerplate

WPForge پیاده‌سازی CLI و ابزارهای اختصاصی خود را در کنار ساختار WordPress Plugin Boilerplate ارائه می‌دهد.

---

## 📄 مجوز

WPForge تحت مجوز زیر منتشر شده است:

**GNU General Public License v2.0 or later (GPL-2.0-or-later)**

برای مشاهده متن کامل مجوز، فایل زیر را ببینید:

```text
LICENSE
```

---

## 🤝 مشارکت

از مشارکت شما در توسعه پروژه استقبال می‌شود.

اگر Bug پیدا کردید یا ایده‌ای برای بهبود پروژه دارید:

1. یک Issue ایجاد کنید.
2. مشکل یا قابلیت پیشنهادی را توضیح دهید.
3. در صورت امکان، مراحل بازتولید مشکل را ارائه دهید.
4. اگر راه‌حل مشکل را دارید، یک Pull Request ارسال کنید.

---

## 🐛 گزارش Bug

هنگام گزارش Bug، اطلاعات زیر را ارائه دهید:

* سیستم‌عامل
* نسخه WPForge
* نسخه Python، در صورت اجرای پروژه از Source
* دستوری که اجرا کرده‌اید
* متن کامل خطا
* مراحل بازتولید مشکل

مثال:

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

⭐ به Repository در GitHub Star بدهید.

همچنین می‌توانید Bugها را گزارش کنید، قابلیت‌های جدید پیشنهاد دهید و در توسعه پروژه مشارکت کنید.

<p align="center">
  ساخته‌شده با ❤️ توسط
  <a href="https://github.com/alirezasayadi">علیرضا صیادی</a>
</p>
