# Selenium on WSL Ubuntu

## Uninstall Ubuntu
```
> wsl --list
> wsl --unregister Ubuntu
```

## Install Ubuntu

Go to Windows Store and install or launch Ubuntu or Ubuntu 18.04 LTS or Ubuntu 20.04 LTS. 


## Update apt Repositories

The Deadsnakes PPA contains Python 3.7.
```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo add-apt-repository ppa:deadsnakes/ppa
```

## Install Python
```
$ sudo apt-get install python3.7
$ sudo apt-get install python3.7-venv
$ sudo apt install python3-pip
```

## Create venv and Add Packages
```
$ cd /mnt/e/linux_venvs
$ sudo python3.7 -m venv venv001
$ cd bin
$ source activate
$ sudo ./python -m pip install --upgrade pip
$ sudo ./pip install selenium
```

## Check that Packages were Installed to venv
```
$ python
```

``` python
import os
os.getcwd()
quit()
```

## Work with Scraper
```
$ cd /mnt/e/linux_git/selenium-termux
$ cd daily_logins
```

## Dependencies

```
$ sudo apt install libnss3
```

## Run

```
$ python app.py
```

## Alternative
```
$ sudo apt install chromium-chromedriver
```
