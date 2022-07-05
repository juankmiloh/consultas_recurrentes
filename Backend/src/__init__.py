import os
import logging
from pickle import NONE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector
from flask_cors import CORS
from injector import Module, Injector, singleton
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import yaml
import cx_Oracle

from .service import ServiceModule
from .repository import RepositoryModule

il = logging.getLogger('injector')
il.addHandler(logging.StreamHandler())
il.level = logging.DEBUG

Base = declarative_base()


class AppModule(Module):
    def __init__(self, db, postgresdb):
        self.db = db
        self.postgresdb = postgresdb

    def configure(self, binder):
        binder.bind(SQLAlchemy, to=self.db, scope=singleton)


def create_app():

    config_name = os.environ.get('FLASK_ENV', 'production')
    app = Flask(__name__,
                static_folder="../front",
                template_folder="../front"
                )
    app.config.from_object('config_' + config_name)

    postgresdb = create_engine(app.config.get("SQLALCHEMY_DATABASE_POSTGRES_URI")).connect() # Comentar esta línea para omitir conexion con gestor
    # postgresdb = None # Descomentar esta línea para omitir conexion con gestor

    db = start_pool(3) # Comentar esta línea para utilizar conexion con gestor en pruebas
    # db = None # Descomentar esta línea para utilizar conexion con gestor

    injector = Injector([AppModule(db, postgresdb), RepositoryModule(db, postgresdb), ServiceModule()])

    from .controller import controller as controller_blueprint
    app.register_blueprint(controller_blueprint)

    if app.config.get("ENV") == 'development' or app.config.get("ENV") == 'production':
        CORS(app, resources={r"*": {"origins": "*", "supports_credentials": True}})

    FlaskInjector(app=app, injector=injector)

    return app

def start_pool(p):
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
                                sessionCallback=init_session)
    return pool

def init_session(connection, requestedTag_ignored):
    cursor = connection.cursor()
    cursor.execute("""
        ALTER SESSION SET
        TIME_ZONE = 'UTC'
        NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI'""")
