import json

from flask import Flask, render_template, jsonify
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)

@app.route("/")
def home():
    return "Hello Flask！"


# @app.route("/index")
# def index():
#     return render_template("index.html")


@app.route("/index", methods=["POST"])
def index():
    return "<h1 style=color:green>Hello Flask!</h1>"


@app.route("/goods")
def get_goods():
    goods = ["梨子", "苹果"]
    return render_template("goods.html", \
        goods=goods)


@app.route("/getinfo")
def get_info():
    info = {
        "name": "Tom",
        "age": 18
    }
    # json_data = json.dumps(info)
    # return json_data, 200, \
    #     {"Content-Type": "application/json"}

    return jsonify(info)


if __name__ == "__main__":
    manager.run(debug=True)
