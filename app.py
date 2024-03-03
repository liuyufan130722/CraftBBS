from flask import Flask
from flask import render_template

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)


@app.route("/")
def index():
    """home"""
    return render_template("index.html")


if __name__ in "__main__":
    app.run(
        host="0.0.0.0",
        port=5665,
        debug=True
    )