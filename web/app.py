"""
John Doe's Flask API.
"""
#Took code from DockerFlask example, then modified it.
#Also took code from hello.py from project-0 for the parsing.
from flask import Flask, abort, send_from_directory, render_template
import os
import configparser

def parse_config(config_paths): #WHAT DO I DO WITH THIS?
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

app = Flask(__name__)

@app.route("/")
def index():
    return "UOCIS docker demo!\n"

#@app.route("/trivia.css")
#def css_file():
#    return send_from_directory('pages/', 'trivia.css')

@app.route("/<string:name>")
def hello(name):
    if ("~" in name or ".." in name):
        abort(403)
    elif (os.path.isfile("pages/" + name)):
        return send_from_directory('pages/', name), 200
    else:
        abort(404)

@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('pages/', '403.html'), 403

@app.errorhandler(404)
def notfound(e):
    return send_from_directory('pages/', '404.html'), 404

if __name__ == "__main__":
    config = parse_config(["credentials.ini", "default.ini"])
    Port = int(config["SERVER"]["PORT"])
    Debug = config["SERVER"]["DEBUG"]
    if Debug == 'True':
        Debug = True
    else:
        Debug = False
    app.run(debug=Debug, host='0.0.0.0', port=Port)
    #app.run(debug=True, host='0.0.0.0', port=5001)