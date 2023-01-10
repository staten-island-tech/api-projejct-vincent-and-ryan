import os
from urllib import request

from flask import Flask, render_template 
import json
import requests
## Open the JSON file of pokemon data


r = requests.get("https://pokeapi.co/api/v2/pokemon/charmander").json()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('index.html')
    
    
    @app.route('/', methods=('GET', 'POST'))
    def getPost():
        if request.method == 'POST':
            title = request.form['title']
            body = request.form['body']
            data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{title}").json()

            print(request.form)
            print('abc')
            return render_template('test.html',data=data)
        else:
            return render_template('index.html')

    return app