from flask_sqlalchemy import SQLAlchemy
from injector import Module, singleton

from .servicio_service import ServicioService
from .consulta_service import ConsultaService
from .empresa_service import EmpresaService

class ServiceModule(Module):
    def configure(self, binder):
        servicio_service = ServicioService()
        consulta_service = ConsultaService()
        empresa_service = EmpresaService()

        binder.bind(ServicioService, to=servicio_service, scope=singleton)
        binder.bind(ConsultaService, to=consulta_service, scope=singleton)
        binder.bind(EmpresaService, to=empresa_service, scope=singleton)
