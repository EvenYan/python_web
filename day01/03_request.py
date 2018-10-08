# 系统库
import json

# 第三方库
from flask import Flask, request, render_template

# 自己写的工具库


app = Flask(__name__)


@app.route("/index", methods=["POST", "GET"])
def index():
    data = json.loads(request.data)
    name = data['name']
    age = data["age"]
    # request.form提取请求体中的表单数据，是一个类字典的对象
    # name = request.form.get("name")
    # age = request.form.get("age")
    # args = request.args.get("name")
    # print(args)
    return "Hello %s, your are %s years old" % (name, age)


# @app.route("/upload", methods=["POST"])
# def upload():
#     file = request.files.get("pic")
#     if file:
#         file.save("./1.jpg")
#         # data = file.read()
#         # f = open("./test.jpg", "wb")
#         # f.write(data)
#         # f.close
#         return "上传成功"
#     return "上传失败"


# 改写upload接口，判断请求，如果是get请求，则返回上传页面，如果是post请求，
# 则保存文件（在前端表单的action里复用upload接口）
@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        file = request.files.get("pic")
        if file:
            file.save("./1.jpg")
            # data = file.read()
            # f = open("./test.jpg", "wb")
            # f.write(data)
            # f.close
            return "上传成功"
        return "上传失败"
    return render_template("upload.html")


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
