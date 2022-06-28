import json

from flask import request

from ..controller import controller
from ..service import EmpresaService
from ..repository import EmpresaRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'empresa', methods=['GET'])
def empresa(empresa_service: EmpresaService, empresa_repository: EmpresaRepository):
    idServicio = request.args.get('servicio_id', default=0, type=int)
    return json.dumps(empresa_service.get_empresa(empresa_repository, idServicio))
