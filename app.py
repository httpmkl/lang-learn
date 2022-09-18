# import database
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    # connection object used to connect with the database
    return conn


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/feed')
def about():
    return render_template('feed.html')


@app.route('/message')
def message():
    return render_template('message.html')


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        lanKnow = request.form['lanKnow']

        if not title:
            flash('Username is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content, lanKnow) VALUES (?, ?, ?)',
                         (title, content, lanKnow))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')
