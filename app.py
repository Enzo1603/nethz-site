from datetime import datetime

from flask import Flask, render_template
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.context_processor
def inject_utcnow():
    return {"utcnow": datetime.utcnow()}


@app.errorhandler(HTTPException)
def custom_error_page(e):
    return render_template("main/errors.html", error_message=e), e.code


@app.route("/")
def home():
    return render_template("main/home.html")


@app.route("/technische_mechanik/<string:semester>")
def technische_mechanik(semester: str):
    return render_template(f"technische_mechanik/TM_{semester}.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
