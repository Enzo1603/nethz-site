from . import main
from .. import cache

from flask import abort, render_template


@main.route("/")
@cache.cached()
def home():
    return render_template("main/home.html")


@main.route("/technische_mechanik/<string:semester>/")
@cache.memoize()
def technische_mechanik(semester: str):
    template_name = f"TM_{semester}"

    valid_template_names = {"TM_HS23"}
    if template_name not in valid_template_names:
        abort(404)

    return render_template(f"technische_mechanik/{template_name}.html")
