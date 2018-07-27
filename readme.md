This is a sample locustio script for mac

## Requirements
* Python
* Locustio
* Virtualenv

## Installing python
```
$ brew install python
```

## Installing pip
```
$ sudo easy_install pip
```

## Creating virtual environment
```
$ python -m virtual env
```

## Activating/Deactivating virtual environment
```
$ source /[env directory]/bin/activate
$ deactivate
```

##### Adding aliases
```
$ sudo nano ~/.bash_profile
$ alias venvpy2.7="source /[env directory]/bin/activate"
//Ctrl+O to save
//Ctrl+X to exit
$ source ~/.bash_profile //to activate your updated bash_profile

$ venvpy2.7 [in terminal] will automatically activate your virtual environment
```

## Installing Locustio
```
$ pip install locustio
``` 
see [Locustio Installation](https://docs.locust.io/en/stable/installation.html)
//use python 2.7 or python 3.6. Incompatible with Python 3.7 as of July 2018

## Running script
`$ locust` 

_In web browser_

_localhost:8089_ is the locust web GUI: input the number of user as well as number of users per second and start swarming

`$ locust --no-web -c 1 -r 1 --print-stats` //disables GUI and purely outputs in _terminal_