from flask import Flask
import flask
import selenium
import sys
import html
import os
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if not os.path.exists('./bin/headless-chromium'):
    print("UNPACKING headless-chromium")
    import zipfile
    with zipfile.ZipFile('./bin/headless-chromium.zip', 'r') as zip_ref:
        zip_ref.extractall('./bin')
    print("UNPACKED headless-chromium")
else:
    print("UNPACKED headless-chromium")

if not os.path.exists('./bin/chromedriver'):
    print("UNPACKING chromedriver")
    import zipfile
    with zipfile.ZipFile('./bin/chromedriver.zip', 'r') as zip_ref:
        zip_ref.extractall('./bin')
    print("UNPACKED chromedriver")
else:
    print("UNPACKED chromedriver")




print(os.environ)


app = Flask(__name__)

@app.route("/")
def hello():
    return_value = get_page()
    return return_value
    #return "Hello, World!" + ' ' + flask.__version__ + ' ' + selenium.__version__ + ' ' + sys.platform + ' ' + get_page()


def get_page():
    print("START get_page()")
    print("HEADLESS", os.path.abspath('./bin/headless-chromium'))
    print("CHROMEDRIVER", os.path.abspath('./bin/chromedriver'))


    # package_name = 'libnss3'
    package_name = 'chromium'
    devnull = open(os.devnull, "w")
    retval = subprocess.call(["dpkg", "-s", package_name], stdout=devnull, stderr=subprocess.STDOUT)
    print(retval)
    if retval != 0:
        print("Package {0} not installed.".format(package_name))
        try:
            subprocess.Popen('apt-get install -y {0}'.format(package_name), shell=True, stdin=None, stdout=None, stderr=None)
        except Exception as e:
            print("Package {0} is FAILED.".format(package_name))
            pass
    else:
        print("Package {0} is installed.".format(package_name))



    options = Options()
    options.binary_location = './bin/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path='./bin/chromedriver', chrome_options=options)
    driver.get('https://www.google.com/')
    source =  driver.page_source
    escaped_source = html.escape(source)
    print(source[:300])
    driver.close()
    driver.quit()

    return '<html><body>{0}</body></html>'.format(escaped_source[:300])


if __name__ == '__main__':
    print("__name__ == '__main__'")
    app.run('127.0.0.1', 5000)