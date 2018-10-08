from flask import Flask, redirect, url_for
from flask_script import Manager
from werkzeug.routing import BaseConverter

app = Flask(__name__)
manager = Manager(app)


@app.route("/", methods=["POST"])
def index():
    return "<h1 style='color:red'> \
            Hello Flask</h1>"


@app.route("/hello", methods=["POST"])
def hello1():
    return "Hello 1"


@app.route("/")
@app.route("/hello", methods=["GET"])
def hello2():
    return "Hello 2"


@app.route("/login")
def login():
    # 硬编码
    # url = "/"
    # 反向解析
    url = url_for("hello2")
    return redirect(url)


@app.route("/goods/<int:goods_id>")
def goods_detail(goods_id):
    return "Goods id is %s" % goods_id


class PhoneConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super().__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        return "131"

    def to_url(self, value):
        return "18111111111"


app.url_map.converters['re'] = PhoneConverter


@app.route("/call/<re(r'1\d{10}'):phone_number>")
def call_phone(phone_number):
    return "Call to %s" % phone_number


@app.route("/home")
def home():
    url = url_for("call_phone", phone_number=135888888888)
    return redirect(url)


if __name__ == "__main__":
    print(app.url_map)
    # app.run(debug=True)
    manager.run()
