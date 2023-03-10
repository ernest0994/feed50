# Feed50
#### Video Demo:  https://youtu.be/FVtLRK5iIsQ
#### Description: Final Project for CS50 Introduction for Computer Science in EdX.

Feed50 is an online RSS Feed Reader developed with Flask that adds and manages RSS feeds. 
It's a very simple application that leverages the acquired skills in the CS50 course 
"Introduction to computer science" https://www.edx.org/course/introduction-computer-science-harvardx-cs50x.

Stack:

```
Python3
Flask
SQLite3
Jinja2
Bootrsap
HTML5
CSS
Javascript
```

Some features added to the app worth mentioning are: Security, mainly with the help of the "password_strength"
module which helps with password security, mostly defining policies such as minimum amount of
character, at least X letters, X uppercase and X special character, and can determine password complexity.

Also, "feedparser" a module designed to make the use of feeds easy.

Using an SQLite3 simple database, users are being stored and are related to their added feeds from which
we can pull data and show it in the home page. This data is pulled from every feed associated
with a user and then is sorted by "published" date and then is displayed in the front end which is based
on HTML and Jinja logic also, leveraging Bootstrap.

If Using PyCharm just clone project and go directly to "Instantiate Database" step, otherwise do everything as follows:

Run the followings commands to install the virtual environment (Windows). Python 3 is required to be set up in path

```
py -m pip install --upgrade pip

py -m venv venv

venv\Scripts\activate
```

Install flask

``pip install flask``

Install password_strength

``pip install password_strength``

Install feedparser

``pip install feedparser``

Install db package

``pip install db``

Instantiate Database

``flask init-db``

Run the application

```flask run```

### That is it! have fun!