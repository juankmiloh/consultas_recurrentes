import yaml
import csv
from flask import send_file


class ConsultaRepository:
    def __init__(self, db):
        self.db = db

    def get_consulta_bd(self, idServicio):
        connection = self.db.acquire()
        cursor = connection.cursor()
        For_Consultas = connection.cursor()    
        cursor.callproc('SP_CONS_RECURRENTES', [idServicio, For_Consultas])
        vcon = For_Consultas.fetchall()
        connection.close()

        return vcon
    
    def get_consulta_detalle_bd(self, idCategoria):
        connection = self.db.acquire()
        cursor = connection.cursor()
        refCursorfor = connection.cursor()    
        cursor.callproc('SP_CONS_DETALLES', [idCategoria, refCursorfor])
        vcon = refCursorfor.fetchall()
        connection.close()

        return vcon
    
    def get_shortexecution_bd(self, items):
        # print('-------------------------------------')
        # print('* items -> ', items)
        # print('-------------------------------------')
        yaml_file = open("src/sources/config.yaml", 'r')
        parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)
        connection = self.db.acquire()
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

        file = pathfile + filename + '.csv'

        with open('src/' + file,'w', newline='') as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=header_mat,delimiter=";")
            writer.writeheader()
         
            for i in range(0, len(vser)):
                Dict={}
                OutputArray=[]
                for j in range(0, len(header_mat)):
                    Dict[header_mat[j]]=vser[i][j]
            
                OutputArray.append(Dict)
                writer.writerows(OutputArray)

        connection.close()
                
        # return OutputArray
        print(file)
        return send_file(file, as_attachment=True)
