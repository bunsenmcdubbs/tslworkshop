# Welcome!

**Ayyyyyy.**

Welcome to the HackGT/Tech Square Labs Python/Flask workshop. We will be building a
Twitter-like web app using Python with the Flask web framework. Along the way, we will be
using HTML, CSS, a lil drop of Javascript and some dark, dark magic to grease the wheels of
technology and apease the programming gods.

# I don't like snakes. Why are you drinking on a weekday? What are this?

Don't worry. It's not that crazy. [Flask] (http://flask.pocoo.org) is a simple and
straightforward web framework for Python that is also extremely powerful. We will start by
building a simple website that keeps track of a todo list and then move on to building the
Twitter clone.

# Getting Started

## Installation

 - [Python 2.7](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/#upgrading-pip)

 After installing Python:
  >  On Linux or OS X:
  >  ```
  >  pip install -U pip
  >  ```
  >  On Windows:
  >  ```
  >  python -m pip install -U pip
  >  ```

 - [Flask](http://flask.pocoo.org/) `pip install Flask`

 - text editor such as [Atom](https://atom.io/) or [Sublime](https://www.sublimetext.com/)

 - (Optional) [ngrok](https://ngrok.io)


## Hello Flask


In `hello.py`:
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

Then start the web application with:
```
python hello.py
```

You can stop the program by pressing <kbd>Control</kbd>+<kbd>C</kbd>

# Todo Application

The structure of the todo list application will remind you of the helloflask
app. The difference here is that I put the HTML/CSS/JavaScript code into a
separate folder called `client`. This is purely for organizational purposes
as our project grows (it won't for this example but you can see how
more complex sites could have multiple files of each type etc...).

```
todo/
├── client
│   ├── index.html
│   ├── main.js
│   └── style.css
└── server.py
```

We do have to make a small change to the code in order to serve the files
from this new location.

```
...
def index(filepath="index.html"):
    return send_from_directory("", filepath)
...
```
Becomes
```
...
def index(filepath="index.html"):
    return send_from_directory("client", filepath)
...
```

## New Flask Functionality

In order to add more functionality into our web application, we need to use
more of Flask's features!

Before (in the helloflask app) we only had `Flask` and `send_from_directory`
in our import statement. We will now need `json` and `request` as well.

```
from flask import Flask, json, send_from_directory, request
```

### `json`
[JSON](https://json.org) is popular format for sending data across the web.
XML is the other popular format. We've already seen a type of XML when we wrote
our HTML. We are using JSON now because it is easier for humans to read and
write and tends to be simpler to use as well.

JSON has the added benefit very closely resembling the notation that Python
uses for dictionaries.

Our application is only using `json` in one place... can you find it?

### `request`
This allows us to interact with the content of the request in Python. Open up
the "Network" tab of your browser's developer tools and look at the request for
creating new events.

Do you notice anything different from the `GET` requests we've been making?
How does the server find and use this data? Where is `request` being used?

# Resources
 - [Flask documentation](http://flask.pocoo.org/docs/0.11/)
 - [Flask tutorial](http://flask.pocoo.org/docs/0.11/tutorial/)
 - [Slides from workshop](https://docs.google.com/presentation/d/1dEiIpEVzzM-szNwicFLBs2sPd8K9pZJRcnIuAG3hUzU/edit?usp=sharing)
 - [MiniTwit](https://github.com/pallets/flask/tree/master/examples/minitwit) a Twitter-clone written with Flask
