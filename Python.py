from flask import Flask, request, session, redirect, url_for
import json, os, hashlib

app = Flask(__name__)
app.secret_key = "secret"
DB = "data.json"

# ---------- Helpers ----------
def hp(p): return hashlib.sha256(p.encode()).hexdigest()

def load():
    if not os.path.exists(DB):
        data = {
            "users": {"admin": {"password": hp("admin123"), "is_admin": True}},
            "seats": {str(i): None for i in range(1, 21)}
        }
        save(data)
    return json.load(open(DB))

def save(d): json.dump(d, open(DB, "w"), indent=2)

# ---------- Routes ----------
@app.route("/")
def home():
    d = load()
    seats = d["seats"]
    user = session.get("user")

    html = "<h2>Seat Booking</h2><br>"
    for i in range(1, 21):
        s = str(i)
        if seats[s] is None:
            html += f"<a href='/book/{s}'>[{s}]</a> "
        elif seats[s] == user:
            html += f"<a href='/cancel/{s}'>[Y{s}]</a> "
        else:
            html += f"[X{s}] "
    html += "<br><br><a href='/logout'>Logout</a>"
    return html

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        u, p = request.form["u"], request.form["p"]
        d = load()
        if u in d["users"] and d["users"][u]["password"] == hp(p):
            session["user"] = u
            session["admin"] = d["users"][u].get("is_admin", False)
            return redirect("/")
        return "Invalid login"
    return '''<form method=post>
    User:<input name=u><br>Pass:<input type=password name=p><br>
    <button>Login</button></form>'''

@app.route("/register", methods=["GET","POST"])
def reg():
    if request.method == "POST":
        u, p = request.form["u"], request.form["p"]
        d = load()
        if u in d["users"]: return "User exists"
        d["users"][u] = {"password": hp(p), "is_admin": False}
        save(d)
        return redirect("/login")
    return '''<form method=post>
    User:<input name=u><br>Pass:<input type=password name=p><br>
    <button>Register</button></form>'''

@app.route("/book/<sid>")
def book(sid):
    if "user" not in session: return redirect("/login")
    d = load()
    if d["seats"][sid] is None:
        d["seats"][sid] = session["user"]
        save(d)
    return redirect("/")

@app.route("/cancel/<sid>")
def cancel(sid):
    if "user" not in session: return redirect("/login")
    d = load()
    if d["seats"][sid] == session["user"] or session.get("admin"):
        d["seats"][sid] = None
        save(d)
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ---------- Run ----------
if __name__ == "__main__":
    app.run(debug=True)
