from flask import abort
from ..repository import ConsultaRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class ConsultaService:

    def get_consulta(self, consulta_repository: ConsultaRepository, idServicio):
        consulta = []
        data = consulta_repository.get_consulta_bd(idServicio)
        for result in data:
            consulta.append(
                {
                    'value':result[0],
                    'option':result[1]
                }
            )
        return consulta
    
    def get_consulta_detalle(self, consulta_repository: ConsultaRepository, idCategoria):
        data = consulta_repository.get_consulta_detalle_bd(idCategoria)
        OutputArray = []
        for row in data:
            outputObj = {
                'id_detalle': row[0],
                'desc_det_consulta': row[1],
                'procedimiento': row[2]
                }
            OutputArray.append(outputObj)               
        return OutputArray
    
    # def get_shortexecution(self, consulta_repository: ConsultaRepository, procedimiento, ano, mes, idempresa, idconsulta):
    #     obj = {'procedimiento': procedimiento, 'ano': ano, 'mes': mes, 'idempresa': idempresa, 'idconsulta': idconsulta}
    #     data = consulta_repository.get_shortexecution_bd(obj)            
    #     return data
    
    def get_shortexecution(self, consulta_repository: ConsultaRepository, model):
        data = consulta_repository.get_shortexecution_bd(model)
        return data
