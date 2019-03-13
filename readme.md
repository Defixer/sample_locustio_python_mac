**Edit a file, create a new file, and clone from Bitbucket in under 2 minutes**

When you're done, you can delete the content in this README and update the file with details for others getting started with your repository.

*We recommend that you open this README in another tab as you perform the tasks below. You can [watch our video](https://youtu.be/0ocf7u76WSo) for a full demo of all the steps in this tutorial. Open the video in a new tab to avoid leaving Bitbucket.*

---

## Edit a file

You’ll start by editing this README file to learn how to edit a file in Bitbucket.

1. Click **Source** on the left side.
2. Click the README.md link from the list of files.
3. Click the **Edit** button.
4. Delete the following text: *Delete this line to make a change to the README from Bitbucket.*
5. After making your change, click **Commit** and then **Commit** again in the dialog. The commit page will open and you’ll see the change you just made.
6. Go back to the **Source** page.

---

## Create a file

Next, you’ll add a new file to this repository.

1. Click the **New file** button at the top of the **Source** page.
2. Give the file a filename of **contributors.txt**.
3. Enter your name in the empty file space.
4. Click **Commit** and then **Commit** again in the dialog.
5. Go back to the **Source** page.

Before you move on, go ahead and explore the repository. You've already seen the **Source** page, but check out the **Commits**, **Branches**, and **Settings** pages.

---

## Clone a repository

Use these steps to clone from SourceTree, our client for using the repository command-line free. Cloning allows you to work on your files locally. If you don't yet have SourceTree, [download and install first](https://www.sourcetreeapp.com/). If you prefer to clone from the command line, see [Clone a repository](https://confluence.atlassian.com/x/4whODQ).

1. You’ll see the clone button under the **Source** heading. Click that button.
2. Now click **Check out in SourceTree**. You may need to create a SourceTree account or log in.
3. When you see the **Clone New** dialog in SourceTree, update the destination path and name if you’d like to and then click **Clone**.
4. Open the directory you just created to see your repository’s files.

Now that you're more familiar with your Bitbucket repository, go ahead and add a new file locally. You can [push your change back to Bitbucket with SourceTree](https://confluence.atlassian.com/x/iqyBMg), or you can [add, commit,](https://confluence.atlassian.com/x/8QhODQ) and [push from the command line](https://confluence.atlassian.com/x/NQ0zDQ).

---
## Requirements
* Python 2.7
* Pip
* Virtual Environment

## Creating virtual environment
```
$ python -m virtual [environment_name] 
```  
_it will create a virtual environment with your current python installed_
_it will be created to the current directory that terminal is in_  

## Activating/Deactivating virtual environment
```
$ source /[virtual_env_directory]/bin/activate
$ deactivate
```  

## Installing Locustio
```
$ pip install locustio
``` 
see [Locustio Installation](https://docs.locust.io/en/stable/installation.html)  
_use Python 2.7 or Python 3.6. Incompatible with Python 3.7 as of July 2018_

## Running script
`$ locust -f [locust_python_file]` #resets the `success` and `fails` upon successful hatch of all users indicated  
`$ locust -f [locust_python_file] --no-reset-stats` #continuously logs all `success` and `fails` from user hatching until concurrent submission of requests
`$ locust -f [locust_filename] --no-web -c 1 -r 1 --print-stats` #disables GUI and purely outputs in _terminal_  

_In web browser_  
`localhost:8089` is the locust web GUI  
  
input the ff and start swarming:  
  
1. Number of Users  
2. Hatchrate

##### Adding aliases
```
$ sudo nano ~/.bash_profile
$ alias venvpy2.7="source /[virtual_env_directory]/bin/activate"
#Ctrl+O to save
#Ctrl+X to exit
$ source ~/.bash_profile #to activate your updated bash_profile

$ venvpy2.7 will automatically activate your virtual environment
(venvpy2.7) $ #virtual environment name should be included in the prompt when it is activated
```