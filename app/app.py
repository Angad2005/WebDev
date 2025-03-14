from flask import Flask, render_template, redirect, url_for, request, session, flash
import bcrypt
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong key

# Create database if it doesn't exist
def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_database()

# Home route
@app.route('/')
def home():
    return render_template('home.html')


# Authentication route (Login & Signup)
@app.route('/authenticate', methods=["GET", "POST"])
def authenticate():
    if request.method == "GET":
        return render_template('authenticate.html')

    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    record = cursor.fetchone()

    if record:
        if bcrypt.checkpw(password.encode('utf-8'), record[0]):
            session['logged_in'] = True
            session['username'] = username
            flash("Login successful!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid password!", "danger")
            return redirect(url_for('authenticate'))
    else:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        flash("Signup successful! Please log in.", "success")
        return redirect(url_for('authenticate'))


# Logout Route
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('authenticate'))


# Login required decorator
def login_required(f):
    def wrap(*args, **kwargs):
        if 'logged_in' not in session:
            flash("You must log in first.", "warning")
            return redirect(url_for('authenticate'))
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__  # Fix for Flask's route decorators
    return wrap


# Protected product pages
@app.route("/zephyrus")
@login_required
def zephyrus():
    return render_template("zephyrus.html")

@app.route("/zenbook")
@login_required
def zenbook():
    return render_template("zenbook.html")

@app.route("/vivobook")
@login_required
def vivobook():
    return render_template("vivobook.html")

@app.route("/tuf")
@login_required
def tuf():
    return render_template("tuf.html")

@app.route("/strix")
@login_required
def strix():
    return render_template("strix.html")


if __name__ == '__main__':
    app.run(debug=True)
