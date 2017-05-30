from flask import Flask, request, session, g, redirect, url_for, abort, \
	 render_template, flash

app = Flask(__name__)
app.config.from_object(__name__) # load config from this file, auto_quiz.py


@app.route('/')
def entry():
	return redirect(url_for('welcome'))

@app.route('/welcome', methods=['POST', 'GET'])
@app.route('/welcome/', methods=['POST', 'GET'])
def welcome():
    return render_template('welcome_page.html')


if __name__ == '__main__':
	app.run()