from flask import Flask
from flask import render_template
app = Flask(__name__)


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

""" 각자 파일 만들어 주고 이 부위 완성해주세요 """

@app.route("/weepok/suldae")
def weepoklist_suldae():
    return render_template("weepoklist.html")


@app.route("/weepok/behind-container")
def weepoklist_container():
    return render_template("weepoklist.html")


@app.route("/weepok/three-can")
def weepoklist_three_can():
    return render_template("weepoklist.html")


@app.route("/weepok/three-mm")
def weepoklist_three_mm():
    return render_template("weepoklist.html")

""" 여기까지 """

@app.route("/sniper")
def sniperlist():
    return render_template("sniperlist.html")


if __name__ == "__main__":
    app.run()
