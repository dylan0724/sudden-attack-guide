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


if __name__ == "__main__":
    app.run()
