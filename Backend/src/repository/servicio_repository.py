class ServicioRepository:
    def __init__(self, db):
        self.db = db

    def get_servicio_bd(self):
        connection = self.db.acquire()
        cursor = connection.cursor()
        refCursor = connection.cursor()
        cursor.callproc('SP_CONS_SERVICIOS', [refCursor])
        vser = refCursor.fetchall()
        connection.close()

        return vser
