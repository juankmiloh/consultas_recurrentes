
from itsdangerous import json
from ..util.constants import API_ROOT_PATH
from ..controller import controller
from ..service import PruebaService
from ..repository import PruebaRepository

@controller.route(API_ROOT_PATH + 'prueba', methods=['GET'])

def prueba(prueba_service: PruebaService, prueba_repository: PruebaRepository):
    return json.dumps(prueba_service.get_prueba(prueba_repository))
