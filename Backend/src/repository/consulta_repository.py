import yaml
import os
import csv
from sqlalchemy import create_engine
from flask import send_file
import cx_Oracle


class ConsultaRepository:
    def __init__(self, db):
        self.db = db

    def get_consulta_bd(self, idServicio):
        cursor = self.db.engine.raw_connection().cursor()
        refCursor = self.db.engine.raw_connection().cursor()
        cursor.callproc('SP_CONS_RECURRENTES', [idServicio, refCursor])

        return refCursor.fetchall()
    
    def get_consulta_detalle_bd(self, idCategoria):
        cursor = self.db.engine.raw_connection().cursor()
        refCursor = self.db.engine.raw_connection().cursor()
        cursor.callproc('SP_CONS_DETALLES', [idCategoria, refCursor])

        return refCursor.fetchall()

    def start_pool(self, p):
        # Generally a fixed-size pool is recommended, i.e. pool_min=pool_max.
        # Here the pool contains 4 connections, which is fine for 4 conncurrent
        # users.
        # The "get mode" is chosen so that if all connections are already in use, any
        # subsequent acquire() will wait for one to become available.
        yaml_file = open("src/sources/config.yaml", 'r')
        parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)
        pool_min = 4
        pool_max = 4
        pool_inc = 0
        pool_gmd = cx_Oracle.SPOOL_ATTRVAL_WAIT
    
        if p==1:
            oracle=parsed_yaml_file["oracle_parametros"]

        if p==2:
            oracle=parsed_yaml_file["oracle_formatos"]

        if p==3:
            oracle=parsed_yaml_file["oracle_server"]

        dns=oracle['host']
        userdb=oracle['user']
        passw=oracle['passwd']

        pool = cx_Oracle.SessionPool(user=userdb,  #os.environ.get("PYTHON_USERNAME"),
                                    password=passw, #os.environ.get("PYTHON_PASSWORD"),
                                    dsn=dns, #os.environ.get("PYTHON_CONNECTSTRING"),
                                    min=pool_min,
                                    max=pool_max,
                                    increment=pool_inc,
                                    threaded=True,
                                    getmode=pool_gmd,
                                    sessionCallback=self.init_session)
        return pool

    def init_session(self, connection, requestedTag_ignored):
        cursor = connection.cursor()
        cursor.execute("""
            ALTER SESSION SET
            TIME_ZONE = 'UTC'
            NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI'""")
    
    def get_shortexecution_bd(self, items):
        # print('-------------------------------------')
        # print('* items -> ', items)
        # print('-------------------------------------')
        yaml_file = open("src/sources/config.yaml", 'r')
        parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)
        pool = self.start_pool(3)
        connection = pool.acquire()
        cursor = connection.cursor()
        refCursorfor = connection.cursor()  

        cursor.callproc('SP_CONS_PAR_CONSULTAS', [items['idconsulta'],refCursorfor])
        vpar = refCursorfor.fetchall()

        for row in vpar:
            proceso=row[0]
            prefijo=row[1]

        refCursorProc = connection.cursor()

        if proceso==1:
            cursor.callproc(items['procedimiento'], [items['ano'], items['mes'] ,refCursorProc])
            filename=prefijo+str(items['ano'])+'_'+str(items['mes'])
            vser = refCursorProc.fetchall()

        if proceso==2:
            cursor.callproc(items['procedimiento'], [items['idempresa'], items['mes'], items['ano'], refCursorProc])
            filename=prefijo+str(items['idempresa'])+'_'+str(items['ano'])+'_'+str(items['mes'])
            vser = refCursorProc.fetchall()
                
        pathfile=parsed_yaml_file["path"]["dir_target"]
        header=parsed_yaml_file["headers"][items['procedimiento']]
        header_mat=header.split(';')
        OutputArray=[]

        file = pathfile + '\\' + filename + '.csv'

        with open('src\\' + file,'w', newline='') as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=header_mat,delimiter=";")
            writer.writeheader()
         
            for i in range(0, len(vser)):
                Dict={}
                OutputArray=[]
                for j in range(0, len(header_mat)):
                    Dict[header_mat[j]]=vser[i][j]
            
                OutputArray.append(Dict)
                writer.writerows(OutputArray)
                
        # return OutputArray
        # http://localhost:5055/recurrentes/api/shortexecution?procedimiento=SP_CONS_COMPONENTES_TARIFARIOS&ano=2021&mes=1&idempresa=22910&idconsulta=5
        return send_file(file, as_attachment=True)
