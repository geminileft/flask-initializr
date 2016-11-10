from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
	return render_template('index.html')

@app.route('/admin')
def admin():
	return render_template('admin.html')

@app.route('/pages')
def pages():
	return render_template('pages.html')

@app.route('/lists')
def lists():
	return render_template('lists.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

