import simplejson as json
from flask import request

from ..controller import controller
from ..service import ConsultaService
from ..repository import ConsultaRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'consulta', methods=['GET'])
def consulta(consulta_service: ConsultaService, consulta_repository: ConsultaRepository):
    idServicio = request.args.get('servicio_id', default=0, type=int)
    return json.dumps(consulta_service.get_consulta(consulta_repository, idServicio))

@controller.route(API_ROOT_PATH + 'consulta_detalle', methods=['GET'])
def consulta_detalle(consulta_service: ConsultaService, consulta_repository: ConsultaRepository):
    idCategoria = request.args.get('category_id', default=0, type=int)
    return json.dumps(consulta_service.get_consulta_detalle(consulta_repository, idCategoria))

@controller.route(API_ROOT_PATH + 'shortexecution', methods=['GET'])
def shortexecution(consulta_service: ConsultaService, consulta_repository: ConsultaRepository):
    procedimiento = request.args.get('procedimiento', default=0, type=str)
    ano = request.args.get('ano', default=0, type=int)
    mes = request.args.get('mes', default=[], type=str)
    
    idempresa = request.args.get('idempresa', default=0, type=int)
    idconsulta = request.args.get('idconsulta', default=0, type=int)
    # return json.dumps(consulta_service.get_shortexecution(consulta_repository, procedimiento, ano, mes, idempresa, idconsulta))
    return consulta_service.get_shortexecution(consulta_repository, procedimiento, ano, mes, idempresa, idconsulta)
