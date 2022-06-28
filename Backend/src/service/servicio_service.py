from flask import abort
from ..repository import ServicioRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class ServicioService:

    def get_servicio(self, servicio_repository: ServicioRepository):
        servicio = []
        data = servicio_repository.get_servicio_bd()
        for result in data:
            servicio.append(
                {
                    'value':result[0],
                    'option':result[1]
                }
            )
        return servicio