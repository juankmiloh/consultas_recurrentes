from injector import Module, singleton

from .servicio_repository import ServicioRepository
from .consulta_repository import ConsultaRepository
from .empresa_repository import EmpresaRepository
from .usuarios_repository import UsuariosRepository
from .dependencia_repository import DependenciaRepository
from .prueba_repository import PruebaRepository


class RepositoryModule(Module):
    def __init__(self, db, postgresdb):
        self.db = db
        self.postgresdb = postgresdb

    def configure(self, binder):
        servicio_repository = ServicioRepository(self.db)
        consulta_repository = ConsultaRepository(self.db)
        empresa_repository = EmpresaRepository(self.db)
        usuarios_repository = UsuariosRepository(self.postgresdb)
        dependencia_repository = DependenciaRepository(self.postgresdb)
        prueba_repository = PruebaRepository(self.db)

        binder.bind(ServicioRepository, to=servicio_repository, scope=singleton)
        binder.bind(ConsultaRepository, to=consulta_repository, scope=singleton)
        binder.bind(EmpresaRepository, to=empresa_repository, scope=singleton)
        binder.bind(UsuariosRepository, to=usuarios_repository, scope=singleton)
        binder.bind(DependenciaRepository, to=dependencia_repository, scope=singleton)
        binder.bind(PruebaRepository, to=prueba_repository, scope=singleton)
