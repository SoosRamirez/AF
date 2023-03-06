from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super secret key'

users = {'soos': '1234',
         'alex': '4321'}
posts = {'firstPost': 'Post about web security'}
comments = {'firstPost': 'Web security is very important'}


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
                    # print(session)
                    return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/index', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        postName = request.form['post']
        comment = request.form['comment']
        comments[postName] = comment
    return render_template('first.html', posts=posts, comments=comments)


if __name__ == '__main__':
    app.run()
