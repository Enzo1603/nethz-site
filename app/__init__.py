from datetime import datetime, timezone
from pathlib import Path

from flask import Flask, render_template
from flask_caching import Cache
from werkzeug.exceptions import HTTPException


FILE_PATH = Path(__file__).resolve().parent
PROJECT_ROOT_PATH = FILE_PATH.parent


cache = Cache(config={"CACHE_TYPE": "SimpleCache"})


def create_app(config_filename=PROJECT_ROOT_PATH / "config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    try:
        app.config.from_pyfile(PROJECT_ROOT_PATH / "instance" / "config.py")
    except FileNotFoundError:
        pass

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
