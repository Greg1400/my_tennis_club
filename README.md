
[![CodeQL](https://github.com/Greg1400/my_tennis_club/actions/workflows/github-code-scanning/codeql/badge.svg?branch=main)](https://github.com/Greg1400/my_tennis_club/actions/workflows/github-code-scanning/codeql)

[![Create Release](https://github.com/Greg1400/my_tennis_club/actions/workflows/create-release.yml/badge.svg?branch=main)](https://github.com/Greg1400/my_tennis_club/actions/workflows/create-release.yml)

[![Django CI](https://github.com/Greg1400/my_tennis_club/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Greg1400/my_tennis_club/actions/workflows/ci.yml)

my_tennis_club
==============

## Virtual Environment

### Create venv
`python -m venv <environment name`

Activate the venv
-----------------
`source <environment name>/bin/activate`

Django
------

To install Django, use the following command `python3 -m pip install Django` 

> You have to be in the venv to install Django into the virtual environment.

### Create a project

The previous commands were : 

```bash
ghe@L39189:~/my_tennis_club$ python -m venv .venv
ghe@L39189:~/my_tennis_club$ source .venv/bin/activate
(.venv) ghe@L39189:~/my_tennis_club$ python3 -m pip install Django
```
Now we create the project with the following command :  

`django-admin startproject my_tennis_club`

To run the project (have access via a browser) : `python3 manage.py runserver`

And we've acces by the following url : http://127.0.0.1:8000

### Create App

`python3 manage.py startapp members`