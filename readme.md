This is a sample locustio script for mac

## Requirements
	* Python
	* Locustio
	* Virtualenv

## Installing python
```
brew install python
```

## Installing pip
```
sudo easy_install pip
```

## Creating virtual environment
```
python -m virtual env
```

## Activating/Deactivating virtual environment
```
source /[env directory]/bin/activate
deactivate
```

## Installing Locustio
```
pip install locustio
``` 
see [Locustio Installation](https://docs.locust.io/en/stable/installation.html)

## Running script
`locust` //
	In web browser 

	_localhost:8090_ is the GUI of locust: input the number of user as well as number of users per second and start 
	
`locust --no-web -c 1 -r 1 --print-stats` //disables GUI and purely outputs in _terminal_

##### Adding aliases
```
sudo nano ~/.bash_profile
alias venvpy2.7="source /[env directory]/bin/activate"
//Ctrl+O to save
//Ctrl+X to exit
source ~/.bash_profile //to activate your updated bash_profile

venvpy2.7 [in terminal] will automatically activate your virtual environment
```

