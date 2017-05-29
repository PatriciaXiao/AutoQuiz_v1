from flask import Flask, request, session, g, redirect, url_for, abort, \
	 render_template, flash

app = Flask(__name__)
app.config.from_object(__name__) # load config from this file, auto_quiz.py

@app.route('/')
def hello():
    return render_template('welcome_page.html')


if __name__ == '__main__':
	app.run()