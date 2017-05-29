from flask import Flask, request, session, g, redirect, url_for, abort, \
	 render_template, flash
	 
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()