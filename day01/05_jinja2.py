from flask import Flask, render_template, redirect, request, g

app = Flask(__name__)


@app.route("/template")
def template():
    dic = {"height": 180, "weight": 70}
    data = ["Tom", "Jim", "Alice"]
    return render_template("jinja.html", name="Tom", age=18, dic=dic, data=data)


@app.route("/login", methods=["GET"])
def login_form():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    # form表单数据get一次后就不能在接收
    username = request.form.get("username")
    passwd = request.form.get("passwd")
    if username == 'admin' and passwd == '123456':
        return render_template("user.html", username=username)
    else:
        message = "账号或者密码错误"
        return render_template("login.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
