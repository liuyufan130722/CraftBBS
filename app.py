from flask import Flask
from flask import send_from_directory
from flask_cors import CORS

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)
CORS(app)


@app.route("/")
def index():
    """home"""
    return send_from_directory("static/vue", "index.html")


if __name__ in "__main__":
    app.run(
        host="0.0.0.0",
        port=5665,
        debug=True
    )