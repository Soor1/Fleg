from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def query_db(query, args=(), one=False):
    con = sqlite3.connect('data/FamilyTree.db')
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    con.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    search_type = request.args.get('type')

    if search_type == "name":
        sql_query = "SELECT * FROM students WHERE name LIKE ?"
        results = query_db(sql_query, ('%' + query + '%',))
    elif search_type == "family":
        sql_query = "SELECT * FROM students WHERE family LIKE ?"
        results = query_db(sql_query, ('%' + query + '%',))
    elif search_type == "year":
        sql_query = "SELECT * FROM students WHERE year LIKE ?"
        results = query_db(sql_query, ('%' + query + '%',))
    elif search_type == "major":
        sql_query = "SELECT * FROM students WHERE major LIKE ?"
        results = query_db(sql_query, ('%' + query + '%',))
    elif search_type == "minor":
        sql_query = "SELECT * FROM students WHERE minor LIKE ?"
        results = query_db(sql_query, ('%' + query + '%',))
    else:
        sql_query = "SELECT * FROM students WHERE name LIKE ? OR family LIKE ? OR year LIKE ? OR major LIKE ? OR minor LIKE ?"
        results = query_db(sql_query, ('%' + query + '%', '%' + query + '%', '%' + query + '%', '%' + query + '%', '%' + query + '%'))

    return jsonify(results=[dict(id=row[0], name=row[1], family=row[2], year=row[3], major=row[4], minor=row[5], linkedin=row[6]) for row in results])

if __name__ == '__main__':
    app.run(debug=True)
