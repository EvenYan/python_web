# 系统库
# import json

# 第三方库
from flask import Flask

# 自己写的工具库


app = Flask(__name__)


@app.route("/index", methods=["POST", "GET"])
def index():
    a = 10 / 0
    print("This index view!")
    return "Hello Flask!"


@app.before_first_request
def handle_first_request():
    print("In before first request hook!")


@app.before_request
def handle_before_request():
    print("In before request hook!")


@app.after_request
def handle_after_request(response):
    print("In after request hook!")
    return response


@app.teardown_request
def handle_teardown_request(response):
    print("In teardown request hook!")


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=False)
