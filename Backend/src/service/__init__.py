from flask_sqlalchemy import SQLAlchemy
from injector import Module, singleton

from .servicio_service import ServicioService
from .consulta_service import ConsultaService
from .empresa_service import EmpresaService
from .usuarios_service import UsuariosService
from .dependencia_service import DependenciaService


class ServiceModule(Module):
    def configure(self, binder):
        servicio_service = ServicioService()
        consulta_service = ConsultaService()
        empresa_service = EmpresaService()
        usuarios_service = UsuariosService()
        dependencia_service = DependenciaService()

        binder.bind(ServicioService, to=servicio_service, scope=singleton)
        binder.bind(ConsultaService, to=consulta_service, scope=singleton)
        binder.bind(EmpresaService, to=empresa_service, scope=singleton)
        binder.bind(UsuariosService, to=usuarios_service, scope=singleton)
        binder.bind(DependenciaService, to=dependencia_service, scope=singleton)
