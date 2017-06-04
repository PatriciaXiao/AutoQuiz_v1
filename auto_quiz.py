from flask import Flask, request, session, g, redirect, url_for, abort, \
	 render_template, flash
from python_lib.database.sqliteDB import hello_db

app = Flask(__name__)
app.config.from_object(__name__) # load config from this file, auto_quiz.py


@app.route('/')
def entry():
	return redirect(url_for('welcome'))

@app.route('/welcome', methods=['POST', 'GET'])
@app.route('/welcome/', methods=['POST', 'GET'])
def welcome():
	login_error = True
	logged_in = False
	return render_template('welcome_page.html', \
		logged_in=logged_in, \
		login_error=login_error)

@app.teardown_appcontext
def wrap_up(error):
	print "close application"
	hello_db()
	# close database

if __name__ == '__main__':
	app.run()