import secrets

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = secrets.token_hex(64)

users = {'soos': '1234',
         'alex': '4321'}
posts = {'firstPost': 'Post about web security'}
comments = {'firstPost': ['Web security is very important']}


@app.after_request
def add_header(response):
    response.headers[
        'Content-Security-Policy'] = "default-src 'self'; script-src * data: blob: 'unsafe-inline' 'unsafe-eval'; style-src 'self'; img-src 'self'; form-action 'self'"
    return response


@app.route('/', methods=('GET', 'POST'))
def hello_world():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for i in users:
            if i == username:
                if users[i] == password:
                    session.clear()
                    session['user_id'] = i
                    return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/index', methods=('GET', 'POST'))
def index():
    for i in users:
        if 'user_id' in session:
            if i == session['user_id']:
                if request.method == 'POST':
                    postName = request.form['post']
                    comment = request.form['comment']
                    comments[postName].append(comment)
                return render_template('post.html', posts=posts, comments=comments)
    return redirect(url_for('hello_world'))


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.debug = True
    app.run()
