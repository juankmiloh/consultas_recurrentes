from sqlalchemy.sql import text


class ServicioRepository:
    def __init__(self, db):
        self.db = db

    def get_servicio_bd(self):
        cursor = self.db.engine.raw_connection().cursor()
        refCursor = self.db.engine.raw_connection().cursor()
        cursor.callproc('SP_CONS_SERVICIOS', [refCursor])

        return refCursor.fetchall()
