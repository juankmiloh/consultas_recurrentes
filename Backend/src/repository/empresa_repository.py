class EmpresaRepository:
    def __init__(self, db):
        self.db = db

    def get_empresa_bd(self, idServicio):
        connection = self.db.acquire()
        cursor = connection.cursor()
        For_Empresas = connection.cursor()
        cursor.callproc('SP_CONS_EMPRESAS_SERVICIOS', [idServicio, For_Empresas])
        vemp = For_Empresas.fetchall()    
        connection.close()

        return vemp
