This is a sample `LocustIO` script [MAC]

## Requirements
* Python 2.7 or later
* LocustIO
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
$ <python> -m venv <env>

$ python3 -m venv venvpy3.7 //virtual environment for latest python3 (v3.7 as of this posting)
$ python3.5 -m venv venvpy3.5 //virtual environment for python3.5
```  
`<python>` - select which python version you would want to have for your virtual environment  
`<env>` - name of the virtual environment to be created  
_it will create a virtual environment with your current python installed; if it's `Python 3.7` it will already have `pip` as well_  
_it will be created to the current directory that terminal is in_  
_use as reference https://amaral.northwestern.edu/resources/guides/pyenv-tutorial_

## Activating/Deactivating virtual environment
```
$ source /[env directory]/bin/activate
$ deactivate
```

##### Adding aliases
`$ sudo nano ~/.bash_profile`  
`$ alias venvpy2.7="source /[virtual_env_directory]/bin/activate"`  
`Ctrl+O` to save  
`Ctrl+X` to exit  
`$ source ~/.bash_profile` #to activate your updated `bash_profile`  
`$ venvpy2.7` #[in terminal] will automatically activate your virtual environment  
`(venvpy2.7) $` #virtual environment name should be included in the prompt when it is activated

## Installing Locustio
```
$ pip install locustio
``` 
see [Locustio Installation](https://docs.locust.io/en/stable/installation.html)  
#use Python 2.7 or Python 3.6. Incompatible with Python 3.7 as of July 2018

## Running script
`$ locust` 

_In web browser_

`localhost:8089` is the locust web GUI: input the number of user as well as number of users per second and start swarming  

`$ locust --no-web -c 1 -r 1 --print-stats` #disables GUI and purely outputs in _terminal_  
