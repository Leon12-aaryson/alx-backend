#!/usr/bin/env python3
'''
basic python flask app
'''

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    '''
    render basic app
    '''
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(debug=True)
