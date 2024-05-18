from flask import Flask
from flask import request, render_template
from flask_cors import CORS

from database import user, verification_code
from VerificationCode import VerificationCodeService
from methods.CreateKey import CreateKey
from methods.downloader import Downloader

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    """Home"""
    return render_template("index.html")


@app.route("/above", methods=["GET"])
def above():
    """Above"""
    return render_template("above.html")


@app.route("/login", methods=["GET"])
def login():
    """Login"""
    return render_template("login.html")


@app.route("/send_code", methods=["POST"])
def send_code():
    """对指定邮件发送验证码"""
    result = {
        "code": 404,
        "content": "error"
    }
    email = request.json.get('email')
    username = request.json.get('username')
    
    if not all([email, username]):
        result["content"] = "参数错误！"
        return result
    
    VCS = VerificationCodeService(verification_code.VerificationCodeDataBase)
    send_result = VCS.send_code(email, username)
    if send_result is False:
        result['content'] = "发送失败！请检查邮件是否填写正确！"
    
    result['code'] = 200
    result["content"] = "发送成功！"
    return result


@app.route("/register", methods=["POST"])
def register():
    """注册用户"""
    result = {"code": 404}

    username = request.json.get("username")
    password = request.json.get("password")
    email = request.json.get("email")
    code = request.json.get("code")
    avatar_url = request.json.get("avatar_url")

    # 检查是否存在，用户名，密码，邮件。
    if not all([username, password, email, code]):
        result['content'] = "参数缺少！"
        return result
    
    # 验证验证码
    VCS = VerificationCodeService(verification_code.VerificationCodeDataBase)
    verify_result = VCS.verify_code(username, email, code)
    if verify_result['code'] != 200:
        result["content"] = verify_result['content']
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