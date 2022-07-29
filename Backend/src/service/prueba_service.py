from flask import abort
from ..repository import PruebaRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class PruebaService:

    def get_prueba(self, prueba_repository: PruebaRepository):
        prueba = []
        #data = prueba_repository.get_prueba_bd()
       
        prueba.append(
            {
                'value':'1',
                'option':'haciendo prueba'
            }
        )
        return prueba