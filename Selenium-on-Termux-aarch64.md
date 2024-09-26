# Selenium-On-Termux-Android

- This tutorial will help you how to install and use Selenium on Termux for Android.

# Termux

## Installation

* Download from F-Droid: https://f-droid.org/en/packages/com.termux/
* Install the APK file.

## Configuration

### Access to Storage

* Enable access by Termux to Android storage.

```
$ termux-setup-storage

It appears that directory '~/storage' already exists.
This script is going to rebuild its structure from
scratch, wiping all dangling files. The actual storage
content IS NOT going to be deleted.

Do you want to continue? (y/n)
```

# Update Linux Packages

```
$ pkg update
$ pkg upgrade
```

# Chromium Driver

```
pkg install x11-repo -y
pkg install tur-repo -y
pkg install chromium -y
```

# Python

## Installation

```
$ pkg install python
$ pkg install python-pip
```

## Virtual Environment

```
$ python -m venv ~/v311
$ source ~/v311/bin/activate
```

## Pip Packages

```
$ pip install selenium==4.9.1
```


# Python Code

``` python
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
