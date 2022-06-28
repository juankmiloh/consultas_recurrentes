from sqlalchemy.sql import text


class EmpresaRepository:
    def __init__(self, db):
        self.db = db

    def get_empresa_bd(self, idServicio):
        cursor = self.db.engine.raw_connection().cursor()
        refCursor = self.db.engine.raw_connection().cursor()
        cursor.callproc('SP_CONS_EMPRESAS_SERVICIOS', [idServicio, refCursor])

        return refCursor.fetchall()
