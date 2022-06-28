from flask import abort
from ..repository import EmpresaRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class EmpresaService:

    def get_empresa(self, empresa_repository: EmpresaRepository, idServicio):
        empresa = []
        data = empresa_repository.get_empresa_bd(idServicio)
        for result in data:
            empresa.append(
                {
                    'value':result[0],
                    'option':result[1]
                }
            )
        return empresa