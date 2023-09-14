import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    # Query database for stocks and cash
    stocks = db.execute(
        "SELECT stock, symbol, SUM(shares) as shares, price FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

    return render_template("index.html", stocks=stocks, cash=cash, usd=usd)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()

        # Checks if shares is a positive integer
        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("Invalid number")

        if shares <= 0:
            return apology("Invalid number")

        # Check if symbol is valid
        if not symbol:
            return apology("Must provide a symbol")

        stock = lookup(symbol.upper())
        if not stock:
            return apology("Invalid symbol")

        user_id = session["user_id"]
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        stock_name = stock["name"]
        stock_price = stock["price"]
        transaction_value = stock_price * shares

        if user_cash < transaction_value:
            return apology("Not affordable")
        else:
            db.execute("UPDATE users SET cash = ? WHERE id = ?", user_cash - transaction_value, user_id)
            db.execute("INSERT INTO transactions (user_id, stock, symbol, shares, price, type) VALUES (?, ?, ?, ?, ?, ?)",
                       user_id, stock_name, symbol, shares, stock_price, 'Bought')

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]

    # Query database for transactions
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?", user_id)
    return render_template("history.html", transactions=transactions, usd=usd)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Must provide a symbol")

        stock = lookup(symbol.upper())
        if not stock:
            return apology("Invalid symbol")
        else:
            return render_template("quoted.html", stock=stock, usd_function=usd)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Must provide username")
        elif not password:
            return apology("Must provide password")
        elif not confirmation:
            return apology("Must confirm the password")

        if password != confirmation:
            return apology("Passwords do not match")

        try:
            hash = generate_password_hash(password)
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            return redirect("/")
        except:
            return apology("Username already exists")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        user_id = session["user_id"]
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        if not symbol:
            return apology("Must select a stock")

        if not shares:
            return apology("Must provide number of shares")
        elif shares <= 0:
            return apology("Invalid number")

        stock_price = lookup(symbol)["price"]
        stock_name = lookup(symbol)["name"]
        price = shares * stock_price

        ownedShares = db.execute(
            "SELECT SUM(shares) AS shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol", user_id, symbol)[0]["shares"]
        if shares > ownedShares:
            return apology("You don't have that amount of shares")

        current_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        db.execute("UPDATE users SET cash = ? WHERE id = ?", price + current_cash, user_id)
        db.execute("INSERT INTO transactions (user_id, stock, symbol, shares, price, type) VALUES (?, ?, ?, ?, ?, ?)",
                   user_id, stock_name, symbol, -shares, price, 'Sold')

        return redirect('/')

    else:
        user_id = session["user_id"]
        symbols = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
        return render_template("sell.html", symbols=symbols)


@app.route("/change", methods=["GET", "POST"])
def change():
    """Change password"""
    if request.method == "POST":
        user_id = session["user_id"]
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not password:
            return apology("Must provide password")
        elif not confirmation:
            return apology("Must confirm the password")

        if password != confirmation:
            return apology("Passwords do not match")

        db.execute("UPDATE users SET hash = ? WHERE id = ?", password, user_id)
        return redirect('/')

    else:
        return render_template("change.html")

