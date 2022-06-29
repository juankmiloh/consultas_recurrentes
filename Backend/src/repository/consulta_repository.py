import yaml
import os
import csv
from sqlalchemy import create_engine
from flask import send_file


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
    
    def get_shortexecution_bd(self, items):
        # print('-------------------------------------')
        # print('* items -> ', items)
        # print('-------------------------------------')
        yaml_file = open("src/sources/config.yaml", 'r')
        parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)
        conn = create_engine('oracle://super:Veri1234@172.16.32.117:1521/xe').connect()
        conn1 = create_engine('oracle://super:Veri1234@172.16.32.117:1521/xe').connect()

        cursor = conn.engine.raw_connection().cursor()
        refCursorfor = conn.engine.raw_connection().cursor()

        cursor.callproc('SP_CONS_PAR_CONSULTAS', [items['idconsulta'], refCursorfor])
        vpar = refCursorfor.fetchall()

        for row in vpar:
            proceso=row[0]
            prefijo=row[1]

        cursor1 = conn1.engine.raw_connection().cursor()
        refCursorProc = conn1.engine.raw_connection().cursor()

        if proceso==1:
            cursor1.callproc(items['procedimiento'], [items['ano'], items['mes'] ,refCursorProc])
            filename=prefijo+str(items['ano'])+'_'+str(items['mes'])
            vser = refCursorProc.fetchall()

        if proceso==2:
            cursor1.callproc(items['procedimiento'], [items['idempresa'], items['mes'], items['ano'], refCursorProc])
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

        conn.close()
        conn1.close()
        
        # return OutputArray
        # http://localhost:5055/recurrentes/api/shortexecution?procedimiento=SP_CONS_COMPONENTES_TARIFARIOS&ano=2021&mes=1&idempresa=22910&idconsulta=5
        return send_file(file, as_attachment=True)
