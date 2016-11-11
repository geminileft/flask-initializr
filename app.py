from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
	return render_template('home.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/pages')
def pages():
	return render_template('pages.html')

@app.route('/lists')
def lists():
	con = sql.connect('db/data.db');

	cur = con.cursor()
	cur.execute('SELECT name from name;')

	rows = cur.fetchall()
	data = []
	for row in rows:
		data.append(row[0])	
	con.close()


	return render_template('lists.html', data=data)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

