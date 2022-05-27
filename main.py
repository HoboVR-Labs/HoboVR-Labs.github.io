from os import path as os_path

import werkzeug
from flask import Flask, send_from_directory

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def staticHost(path):
    print("path: %s" % path)
    normalized = path.strip("/")
    if os_path.isfile(normalized + ".html"):
        return send_from_directory("", normalized + ".html")
    try:
        return send_from_directory("", path)
    except werkzeug.exceptions.NotFound as e:
        if os_path.isfile(normalized + "/index.html"):
            return send_from_directory("", normalized + "/index.html")
        raise e
