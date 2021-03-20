from flask import Flask, render_template
import json
from random import choice

app = Flask(__name__)

@app.route("/member")
def member():
    with open("static/json/pilots.json", "rt", encoding="utf8") as file:
        pilots_list = json.loads(file.read())
    return render_template("pilots.html", pilots=pilots_list)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
