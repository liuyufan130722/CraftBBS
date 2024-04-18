from flask import Flask
from flask import request
from flask_cors import CORS

from database import user
from methods.CreateKey import CreateKey
from methods.downloader import Downloader

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)
CORS(app)

@app.route("/register", methods=["POST"])
def register():
    """注册用户"""
    result = {"code": 404}

    username = request.json.get("username")
    password = request.json.get("password")
    email = request.json.get("email")
    avatar_url = request.json.get("avatar_url")

    # 检查是否存在，用户名，密码，邮件。
    if not all([username, password, email]):
        result['content'] = "参数缺少！"
        return result
    
    # 进行注册
    with user.UserDatabase() as useroper:
        create_result = useroper.create_user(
            username,
            email,
            False,
            password=password,
            key=CreateKey().generate_key(),
            avatar=Downloader.download_file(avatar_url) if avatar_url else b''
        )
    if create_result is False:
        result['content'] = "创建用户失败！"
        return result
    
    result["code"] = 200
    result["content"] = "创建成功！"
    return result


if __name__ in "__main__":
    app.run(
        host="0.0.0.0",
        port=5665,
        debug=True
    )