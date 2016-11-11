from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)

@app.route('/version')
def version():
	return "2.2.16.1110"

@app.route('/')
@app.route('/index')
def home():
	return render_template('home.html')

@app.route('/admin')
def admin():
	data = {"version":version()}
	data["x"] = "y"
	return render_template('admin.html', data=data)

@app.route('/pages')
def pages():
	return render_template('pages.html')

def lists_data():
	data = []
	con = sql.connect('db/data.db');

	cur = con.cursor()
	cur.execute('SELECT name from name;')

	rows = cur.fetchall()
	for row in rows:
		data.append(row[0])	
	con.close()
	return data


@app.route('/lists')
def lists():
	return render_template('lists.html', data=lists_data())

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

