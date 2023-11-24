from datetime import datetime, timezone
from pathlib import Path

from flask import Flask, render_template
from flask_caching import Cache
from werkzeug.exceptions import HTTPException


FILE_PATH = Path(__file__).resolve().parent
CONFIG_FILE_PATH = FILE_PATH.parent / "config.py"

cache = Cache(config={"CACHE_TYPE": "SimpleCache"})


def create_app(config_filename=CONFIG_FILE_PATH):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    @app.context_processor
    def inject_utcnow():
        return {"utcnow": datetime.now(timezone.utc)}

    @app.errorhandler(HTTPException)
    def custom_error_page(e):
        return render_template("main/errors.html", error_message=e), e.code

    app.template_folder = "../templates"
    app.static_folder = "../static"

    cache.init_app(app)

    from .main.views import main
    from .worldle.views import worldle

    app.register_blueprint(main)
    app.register_blueprint(worldle, url_prefix="/worldle/")

    return app
