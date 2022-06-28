from flask import Blueprint
from flask_cors import CORS

controller = Blueprint('controller', __name__, url_prefix='/')
# src.controller

from . import \
front_controller, \
servicio_controller, \
consulta_controller, \
empresa_controller
