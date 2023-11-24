from flask import Blueprint

worldle = Blueprint("worldle", __name__)


from . import views
