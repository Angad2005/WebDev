from flask import Flask, render_template, redirect, url_for, request, session, flash
import bcrypt    # this is used for passward hashing
import sqlite3   # allows us to use sql databases 
import re        # allows us to use regular expressions used for email validation

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong key


#=================================== Create database if it doesn't exist =====================================
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

def create_feedback_database():
    conn = sqlite3.connect('feedback.db')  # Create feedback.db
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Call the function to create the database
create_feedback_database()



# ===================================== THIS IS ROUTING OF PAGES ======================================

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



@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    email = request.form.get('email')
    message = request.form.get('message')

    # ✅ Email validation regex
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not email or not message:
        flash("❌ Please fill in all fields.", "danger")
    elif not re.match(email_pattern, email):  # Validate email format
        flash("❌ Invalid email format. Please enter a valid email address.", "danger")
    else:
        # ✅ Save valid feedback to the database
        conn = sqlite3.connect('feedback.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (email, message) VALUES (?, ?)", (email, message))
        conn.commit()
        conn.close()
        flash("✅ Feedback sent successfully!", "success")

    return redirect(url_for('feedback'))

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')



if __name__ == '__main__':
    app.run(debug=True)
    