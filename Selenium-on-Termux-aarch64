# Selenium-On-Termux-Android

- This tutorial will help you how to install and use Selenium on Termux for Android.

# Termux

## Installation

* Download from F-Droid: https://f-droid.org/en/packages/com.termux/
* Install the APK file.

## Configuration

### Access to Storage

Enable access by Termux to Android storage.

```
$ termux-setup-storage
```

# Linux Packages

```
$ pkg update
$ pkg upgrade
```

# Python

```
$ pkg install python
$ 
```

The version number is important.

```
$ pip install selenium==4.9.1
```

# Chromium Driver

```
pkg install x11-repo -y
pkg install tur-repo -y
pkg install chromium -y
```

# Python Code

```
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
driver.save_screenshot("/sdcard/download/screenshot.png")
print("Please check screenshot image")
driver.quit()
```

# Credits

* https://github.com/luanon404/Selenium-On-Termux-Android/blob/main/README.md
