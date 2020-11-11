# Using virtual Env in python

## Listing the list of libraries installed in the python by defualt 
```
C:\Users\MrMe>pip list

Package              Version
-------------------- -------
appdirs              1.4.4
Appium-Python-Client 1.0.2
atomicwrites         1.4.0
attrs                20.3.0
bcrypt               3.2.0
cffi                 1.14.3
colorama             0.4.4
cryptography         3.2.1
distlib              0.3.1
filelock             3.0.12
iniconfig            1.1.1
packaging            20.4
paramiko             2.7.2
pip                  20.2.4
pluggy               0.13.1
py                   1.9.0
pycparser            2.20
PyNaCl               1.4.0
pyparsing            2.4.7
pytest               6.1.2
selenium             3.141.0
setuptools           41.2.0
six                  1.15.0
toml                 0.10.2
urllib3              1.25.11
virtualenv           20.1.0
```


## Go the direcotry where you want to create the virtual env
C:\Users\MrMe>cd Desktop


## Create the virtual env
C:\Users\MrMe\Desktop>python -m venv test_project_env

## If you want to create the virtual env which can also use the system packages add: venv --system-site-packages
C:\Users\MrMe\Desktop>python -m venv venv --system-site-packages

## Check if the virtual env is created
```
C:\Users\MrMe\Desktop>dir

Directory of C:\Users\MrMe\Desktop

11/11/2020  12:07 PM    <DIR>          test_project_env
               0 File(s)        0 bytes
               1 Dir(s)  5,037,184 bytes free


```
## Activate the Virtual Environment
```
C:\Users\MrMe\Desktop>test_project_env\Scripts\activate.bat

> (test_project_env) C:\Users\MrMe\Desktop>where python
C:\Users\MrMe\Desktop\test_project_env\Scripts\python.exe
D:\Programs\Python\Python38\python.exe
C:\Users\MrMe\AppData\Local\Microsoft\WindowsApps\python.exe
```
## Check the files in the directory

```
(test_project_env) C:\Users\MrMe\Desktop>cd test_project_env

(test_project_env) C:\Users\MrMe\Desktop\test_project_env>dir

 Directory of C:\Users\MrMe\Desktop\test_project_env

11/11/2020  12:07 PM    <DIR>          .
11/11/2020  12:07 PM    <DIR>          ..
11/11/2020  12:07 PM    <DIR>          Include
11/11/2020  12:07 PM    <DIR>          Lib
11/11/2020  12:07 PM                91 pyvenv.cfg
11/11/2020  12:07 PM    <DIR>          Scripts
               1 File(s)             91 bytes
               5 Dir(s)  159,391,850,496 bytes free
```
## List of Libraries installed in the environment (By default it's 2)
```
(test_project_env) C:\Users\MrMe\Desktop\test_project_env>pip list
Package    Version
---------- -------
pip        19.2.3
setuptools 41.2.0
```
## List the packages installed only the VirtualEnv 

D:\Programs\sdk-manager\bin>pip list --local


## Installed the library only in the environment (test_project_env)
> When you are in the virtual environment, packages installed here are bound only to the specific environment
```
(test_project_env) C:\Users\MrMe\Desktop\test_project_env>pip install requests
Collecting requests
  Downloading requests-2.24.0-py2.py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 88 kB/s
Collecting chardet<4,>=3.0.2
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 469 kB/s
Collecting certifi>=2017.4.17
  Downloading certifi-2020.11.8-py2.py3-none-any.whl (155 kB)
     |████████████████████████████████| 155 kB 2.2 MB/s
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
  Using cached urllib3-1.25.11-py2.py3-none-any.whl (127 kB)
Collecting idna<3,>=2.5
  Downloading idna-2.10-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 3.8 MB/s
Installing collected packages: chardet, certifi, urllib3, idna, requests
Successfully installed certifi-2020.11.8 chardet-3.0.4 idna-2.10 requests-2.24.0 urllib3-1.25.11

```
## Now if you list the library you will be the installed packages and the dependencies (test_project_env)
```
(test_project_env) C:\Users\MrMe\Desktop\test_project_env>pip list
Package    Version
---------- ---------
certifi    2020.11.8
chardet    3.0.4
idna       2.10
pip        20.2.4
requests   2.24.0
setuptools 41.2.0
urllib3    1.25.11
```
## Create the requirements files by pip freeze and copying it to the requirements.txt
```
(test_project_env) C:\Users\MrMe\Desktop\test_project_env>pip freeze
certifi==2020.11.8
chardet==3.0.4
idna==2.10
requests==2.24.0
urllib3==1.25.11
```
## This code will create a new file for your in the current working directory
(test_project_env) C:\Users\MrMe\Desktop\test_project_env>pip freeze > requirements.txt



## Install the required libraries using requirements.txt
(test_project_env) C:\Users\MrMe\Desktop\test_project_env>pip install -r requirements.txt


## Get out the Virtual environment
(test_project_env) C:\Users\MrMe\Desktop\test_project_env>deactivate

## Delete the virtual environment project as a whole
```
C:\Users\MrMe\Desktop>rmdir test_project_env /s
test_project_env, Are you sure (Y/N)? Y
```
