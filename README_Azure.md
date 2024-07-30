# Selenium on Azure Webapp _without Docker File_

## Navigate to the directory containing app.py 
```
> E:
E:\Development\Git\AzureSelenium
```

## Browse to Webapp
[jquisenberry-hello.azurewebsites.net](jquisenberry-hello.azurewebsites.net)



## List Webapps
```
> az webapp list
-> ..."name": "jquisenberry-hello"...
```

## Create New App
Notice `--sku F1`, which indicates free tier.
```
> az webapp up --sku F1 --name jquisenberry-hello
```

## Update App
```
> az webapp up --logs
```

## View Log without Updating App

```
> az webapp log tail
```

# How to Install Linux Package within Python
This logic is key to running chromedriver without configuring chromium with a Docker file. The downside is that the resulting container has a lifetime of about 75 minutes.
``` python
# Detect whether package is already installed.
retval = subprocess.call(["dpkg", "-s", package_name], stdout=devnull, stderr=subprocess.STDOUT)
# Run installation process
subprocess.Popen('apt-get install -y libnss3', shell=True, stdin=None, stdout=None, stderr=None)
```

# How to Install Linux Packages Manually

## Start SSH to Container

List web apps. Start container.
```
> az webapp list
> az webapp create-remote-connection --name jquisenberry-hello --resource-group jquisenberry_rg_Linux_centralus
```

## Open SSH
Browse to `https://jquisenberry-hello.scm.azurewebsites.net/webssh/host`.

## Within SSH
```
> apt-get install chromium
```



