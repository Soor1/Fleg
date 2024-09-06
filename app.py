from flask import Flask, render_template, jsonify, request, session, g
import sqlite3
import json

app = Flask(__name__)

@app.route('/api')
def getData():
    filter = request.args.get('filter')
    userSearch = request.args.get('userSearch')

    conn = sqlite3.connect('familyTree.db')
    cursor = conn.cursor()

    if filter == "name":
        pass
    elif filter == "family":
        pass
    elif filter == "year":
        pass
    elif filter == "major":
        pass
    elif filter == "committee":
        pass

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
