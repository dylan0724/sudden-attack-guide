# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'aewfawelkalejtali3tjliejglajitalijtojtiaijtlwaij'
app.config['DEBUG'] = True


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/term")
def term():
    return render_template("term.html")


@app.route("/weepok")
def weepoklist():
    return render_template("weepoklist.html")


@app.route("/weepok/headpok")
def weepoklist_headpok():
    return render_template("weepok/headpok.html")


@app.route("/weepok/suldae")
def weepoklist_suldae():
    return render_template("weepok/suldae.html")


@app.route("/weepok/behind")
def weepoklist_container():
    return render_template("weepok/behind.html")


@app.route("/weepok/threecan")
def weepoklist_three_can():
    return render_template("weepok/threecan.html")


@app.route("/weepok/3mm")
def weepoklist_three_mm():
    return render_template("weepok/3mm.html")


@app.route("/sniper")
def sniperlist():
    return render_template("sniperlist.html")


@app.route("/sniper/backshot")
def sniperlist_backshot():
    return render_template("sniper/backshot.html")


@app.route("/sniper/breaking")
def sniperlist_breaking():
    return render_template("sniper/breaking.html")


@app.route("/sniper/burning")
def sniperlist_burning():
    return render_template("sniper/burning.html")


@app.route("/sniper/ragshot")
def sniperlist_ragshot():
    return render_template("sniper/ragshot.html")


@app.route("/sniper/twojump")
def sniperlist_twojump():
    return render_template("sniper/twojump.html")


if __name__ == "__main__":
    app.run()
