from injector import Module, singleton

from .servicio_repository import ServicioRepository
from .consulta_repository import ConsultaRepository
from .empresa_repository import EmpresaRepository


class RepositoryModule(Module):
    def __init__(self, db):
        self.db = db

    def configure(self, binder):
        servicio_repository = ServicioRepository(self.db)
        consulta_repository = ConsultaRepository(self.db)
        empresa_repository = EmpresaRepository(self.db)

        binder.bind(ServicioRepository, to=servicio_repository, scope=singleton)
        binder.bind(ConsultaRepository, to=consulta_repository, scope=singleton)
        binder.bind(EmpresaRepository, to=empresa_repository, scope=singleton)
