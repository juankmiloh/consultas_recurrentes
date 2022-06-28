import json

from flask import request

from ..controller import controller
from ..service import ServicioService
from ..repository import ServicioRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'servicio', methods=['GET'])
def servicio(servicio_service: ServicioService, servicio_repository: ServicioRepository):
    return json.dumps(servicio_service.get_servicio(servicio_repository))
