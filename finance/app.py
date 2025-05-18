import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


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
    total2 = 0
    table = db.execute("SELECT * FROM current WHERE users_id = ?", session["user_id"])
    for row in table:
        stock = lookup(row['stock'])
        row["name"] = stock['name']
        row["price"] = usd(stock['price'])
        row["total"] = usd(stock['price']*int(row['shares']))
        total2 += stock['price']*int(row['shares'])

    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    return render_template("index.html", rows = table, cash = usd(cash[0]['cash']), total2 = usd(total2+cash[0]['cash']))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        if not request.form.get("symbol"):
            return apology("must provid symbol", 400)
        if not lookup(request.form.get("symbol")):
            return apology("symbol doesn't exist", 400)
        if float(request.form.get("shares")) <= 0:
            return apology("Have to buy more than 0 shares", 400)

        if '.' in request.form.get("shares"):
            integer_part, decimal_part = request.form.get("shares").split('.')
            if decimal_part.isdigit():
                return apology("Have to buy a integer amount", 400)


        stock = lookup(request.form.get("symbol"))
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        if rows[0]['cash'] < int(request.form.get("shares"))*stock['price']:
            return apology("Not enough in your Balance", 400)

        rows = db.execute("SELECT stock FROM current WHERE users_id = ? AND stock = ?", session["user_id"], request.form.get("symbol"))
        if len(rows) != 1:
            db.execute("INSERT INTO current (users_id, stock, shares) VALUES (?, ?, ?)", session["user_id"], request.form.get("symbol"), request.form.get("shares"))
        else:
            db.execute("UPDATE current SET shares = shares + ? WHERE users_id = ? AND stock = ?", request.form.get("shares"), session["user_id"], request.form.get("symbol"))

        db.execute("INSERT INTO history (users_id, stock, shares, statue) VALUES (?, ?, ?, ?)", session["user_id"], request.form.get("symbol"), int(request.form.get("shares")), "buy")

        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", int(request.form.get("shares"))*stock['price'], session["user_id"])

        return redirect("/")

    if request.method == "GET":
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    table = db.execute("SELECT * FROM history WHERE users_id = ?", session["user_id"])
    for row in table:
        stock = lookup(row['stock'])
        row["price"] = usd(stock['price'])

    return render_template("history.html", table = table)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

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
        if not request.form.get("symbol"):
            return apology("must provid symbol", 400)
        if not lookup(request.form.get("symbol")):
            return apology("symbol doesn't exist", 400)

        stock = lookup(request.form.get("symbol"))
        return render_template("quoted.html",name = stock['name'],price = stock['price'],symbol = stock['symbol'])
    if request.method == "GET":
        return render_template("/quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    result = db.execute("SELECT username FROM users")
    usernames = [row['username'] for row in result]

    if request.method == "POST":
         # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        elif request.form.get("username") in usernames:
            return apology("username already exists", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        db.execute("INSERT INTO users (username, hash) VALUES ( ?, ?)", request.form.get("username"), generate_password_hash(request.form.get("password"), method='pbkdf2', salt_length=16))

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        session["user_id"] = rows[0]["id"]

        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":

        table = db.execute("SELECT * FROM current")
        stock = lookup(request.form.get("symbol"))

        if not request.form.get("symbol"):
            return apology("No stock selected", 400)
        if not request.form.get("shares"):
            return apology("Number of shares required", 400)
        if int(request.form.get("shares")) <= 0:
            return apology("Must input positive number", 400)
        for row in table:
            if request.form.get("symbol") in row['stock']:
                if row['shares'] > int(request.form.get("shares")):
                    db.execute("UPDATE current SET shares = shares - ? WHERE users_id = ? AND stock = ?", request.form.get("shares"), session["user_id"], request.form.get("symbol"))
                    db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", int(request.form.get("shares"))*stock['price'], session["user_id"])
                    db.execute("INSERT INTO history (users_id, stock, shares, statue) VALUES (?, ?, ?, ?)", session["user_id"], request.form.get("symbol"), request.form.get("shares"), "sell")

                    return redirect("/")

        return apology("Not enough shares", 400)
    if request.method == "GET":
        table = db.execute("SELECT stock FROM current WHERE users_id = ?", session["user_id"])

        return render_template("sell.html", table = table)
