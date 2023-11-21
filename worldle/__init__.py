from flask import Blueprint

worldle_bp = Blueprint("worldle_bp", __name__)


from . import views  # noqa: E402, F401
