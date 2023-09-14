import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///mail.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def inbox():
    """Show mails"""
    user_id = session["user_id"]
    recipientdb = db.execute("SELECT username FROM users WHERE id=?", user_id)
    recipient = recipientdb[0]['username']

    if request.method == "GET":
        mails = db.execute(
            "SELECT * FROM mail WHERE recipient=?", recipient)
        return render_template("inbox.html", mails=mails)


@app.route("/sent")
@login_required
def sent():
    """Show mails sent"""
    user_id = session["user_id"]
    senderdb = db.execute("SELECT username FROM users WHERE id=?", user_id)
    sender = senderdb[0]['username']

    if request.method == "GET":
        mails = db.execute(
            "SELECT * FROM mail WHERE sender=?", sender)
        return render_template("sent.html", mails=mails)


@app.route("/mail", methods=["POST"])
def mail():
    """View mail"""
    if request.method == "POST":
        mail_id = request.form.get("mail_id")
        mail_full = db.execute("SELECT * FROM mail WHERE id=?", mail_id)

    return render_template("mail.html", mail_full=mail_full)


@app.route("/send", methods=["GET", "POST"])
@login_required
def send():
    """Writes an email"""
    if request.method == "POST":
        user_id = session["user_id"]
        senderdb = db.execute("SELECT username FROM users WHERE id=?", user_id)
        sender = senderdb[0]['username']
        recipient = request.form.get("mail")
        subject = request.form.get("subject")
        body = request.form.get("body")

        # Asks user for a subject, recipient and body
        if not subject:
            return render_template("send.html", info="Must provide a subject")
        elif not recipient:
            return render_template("send.html", info="Must provide a recipient")
        elif not body:
            return render_template("send.html", info="Must provide a message")

        # Inserts mail to database
        try:
            db.execute("INSERT INTO mail (sender, recipient, subject, body) VALUES (?, ?, ?, ?)", sender, recipient, subject, body)
        finally:
            return redirect("/")

    return render_template("send.html")


@app.route("/reply", methods=["POST"])
@login_required
def reply():
    """Replies to an email"""
    if request.method == "POST":
        mail_id = request.form.get("mail_id")
        mail_full = db.execute("SELECT * FROM mail WHERE id=?", mail_id)

        return render_template("reply.html", mail_full=mail_full)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("mail"):
            return render_template("login.html", info='Must provide mail')

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("login.html", info='Must provide password')

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("mail"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("login.html", info='Invalid username and/or password')

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        mail = request.form.get("mail")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Make sure user provides a username and a password
        if not mail:
            return render_template("register.html", info='Must provide mail')
        elif not password:
            return render_template("register.html", info='Must provide password')
        elif not confirmation:
            return render_template("register.html", info="Must confirm the password")

        # Make sure passwords match
        if password != confirmation:
            return render_template("register.html", info="Passwords do not match")

        # Store password in database
        try:
            hash = generate_password_hash(password)
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", mail, hash)
            return redirect("/")
        except:
            return render_template("register.html", info="Mail address already exists")

    else:
        return render_template("register.html")


@app.route("/change", methods=["GET", "POST"])
def change():
    """Change password"""
    if request.method == "POST":
        user_id = session["user_id"]
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Requires input for password and it checks if the confirmation matches
        if not password:
            return apology("Must provide password")
        elif not confirmation:
            return apology("Must confirm the password")

        if password != confirmation:
            return apology("Passwords do not match")

        # Updates database
        db.execute("UPDATE users SET hash = ? WHERE id = ?", password, user_id)
        return redirect('/')

    else:
        return render_template("change.html")
