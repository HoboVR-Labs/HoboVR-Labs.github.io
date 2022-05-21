from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/")
def show_root():
    return send_from_directory("", "index.html")


@app.route("/<path>")
def show(path):
    return send_from_directory("", path)


# @app.route("/contact/")
# def show_contacts():
#     return send_from_directory("", "contact.html")


# @app.route("/team/")
# def show_team():
#     return send_from_directory("", "team.html")


@app.route("/style.css")
def show_style():
    return send_from_directory("", "style.css")


@app.route("/img/<path>")
def show_img(path):
    return send_from_directory("img", path)


@app.route("/docs/html/")
def show_docs():
    return send_from_directory("./docs/html/", "index.html")


@app.route("/docs/html/<path>")
def show_docs2(path):
    return send_from_directory("./docs/html/", path)


# @app.route("/favicon.png")
# def show_favicon():
#     return send_from_directory("img", "favicon.png")
