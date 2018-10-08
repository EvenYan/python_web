from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route("/index")
def index():
    return render_template("home.html")


@app.route("/ajax")
def get_data():
    return render_template("ajax.html")


@app.route("/getdata")
def get_json():
    info = {
        "name": "Tom",
        "age": 18
    }
    return jsonify(info)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
