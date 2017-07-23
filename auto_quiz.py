from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from python_lib.database.sqliteDB import sqlite3DB, hello_db

app = Flask(__name__)
app.config.from_object(__name__) # load config from this file, auto_quiz.py
app.config.update(dict(
    SECRET_KEY='BJC2017Fall'
))

@app.route('/')
def entry():
    return redirect(url_for('welcome'))

@app.route('/welcome', methods=['POST', 'GET'])
@app.route('/welcome/', methods=['POST', 'GET'])
def welcome():
    if request.method == 'POST':
        # print "button: '" + request.form['button'] + "'"
        if request.form['button'] == 'log_in':
            print "log in"
            '''
            login_error = True
            session['logged_in'] = not login_error
            session['user_info'] = {
                "name": "Patricia",
                "student id": "24965096"
            }
            '''
            db = sqlite3DB("my folder", "hello world")
            login_error, user_info = db.is_valid_user(request.form['email'], request.form['password'])
            session['logged_in'] = not login_error
            session['user_info'] = user_info
        elif request.form['button'] == 'log_out':
            print "log out"
            login_error = False
            session['logged_in'] = False
    else:
        login_error = False
        session['logged_in'] = False
    return render_template('/welcome/welcome_page.html', \
        login_error=login_error)

@app.route('/login', methods=['POST', 'GET'])
@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return redirect(url_for('start'))
    return render_template('/signin/login.html')

@app.route('/dashboard', methods=['POST', 'GET'])
@app.route('/dashboard/', methods=['POST', 'GET'])
def start():
    return render_template('/start/dashboard.html')

@app.route('/section/data_structure', methods=['POST', 'GET'])
def section_datastruct():
    session['section_name'] = "datastruct"
    return render_template('/start/section.html', section_name='Data Structure')

@app.route('/section/data_structure/exercise', methods=['POST', 'GET'])
def exercise_datastruct():
    return render_template('/start/section.html', section_name='Data Structure Exercise')

@app.before_request
def before_request():
    session.permanent = True
    # app.permanent_session_lifetime = timedelta(minutes=5)

@app.teardown_request
def teardown_request(exception):
    hello_db()
    print "end"

if __name__ == '__main__':
    app.run()