from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


from python_lib.database.sqliteDB import hello_db

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
        print "button: '" + request.form['button'] + "'"
    login_error = True
    session['logged_in'] = True
    user_info = {
        "name": "Patricia",
        "student id": "24965096"
    }
    return render_template('/welcome/welcome_page.html', \
        login_error=login_error, user_info = user_info)

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