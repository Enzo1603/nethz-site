import os
from datetime import datetime
from dotenv import load_dotenv

from flask import Flask, abort, render_template
from flask_caching import Cache
from werkzeug.exceptions import HTTPException

load_dotenv()
DEBUG: bool = bool(os.getenv("DEBUG") or False)
HOST: str | None = os.getenv("HOST") or None


cache = Cache(config={"CACHE_TYPE": "SimpleCache"})
TIMEOUT: int = 60 * 60 * 24 * 365  # 365 days

app = Flask(__name__)
cache.init_app(app)

from worldle import worldle_bp as worldle_blueprint
app.register_blueprint(worldle_blueprint, url_prefix="/worldle")

def bypass_caching():
    return DEBUG


@app.context_processor
def inject_utcnow():
    return {"utcnow": datetime.utcnow()}


@app.errorhandler(HTTPException)
def custom_error_page(e):
    return render_template("main/errors.html", error_message=e), e.code


@app.route("/")
@cache.cached(timeout=TIMEOUT, unless=bypass_caching)
def home():
    return render_template("main/home.html")


@app.route("/technische_mechanik/<string:semester>")
@cache.memoize(timeout=TIMEOUT, unless=bypass_caching)
def technische_mechanik(semester: str):
    template_name = f"TM_{semester}"

    valid_template_names = {"TM_HS23"}
    if template_name not in valid_template_names:
        abort(404)

    return render_template(f"technische_mechanik/{template_name}.html")


if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST)
