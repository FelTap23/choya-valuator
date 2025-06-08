import json

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, CheckConstraint, Integer, String, Double, create_engine
from enum import Enum


Base  = declarative_base()

class TipoCaracteristicaAvaluo(str, Enum):
    CLASIFICACION_DE_LA_ZONA = 'CLASIFICACION_DE_LA_ZONA'
    TIPO_CONSTRUCCION_ZONA = 'TIPO_CONSTRUCCION_ZONA'
    USO_DE_SUELO = 'USO_DE_SUELO'
    
    ABASTECIMIENTO_DE_AGUA_POTABLE = 'ABASTECIMIENTO_DE_AGUA_POTABLE'
    DRENAJE_Y_ACANTARILLADO = 'DRENAJE_Y_ACANTARILLADO'
    RED_DE_ELECTRIFICACION = 'RED_DE_ELECTRIFICACION'
    ALUMBRADO_PUBLICO = 'ALUMBRADO_PÚBLICO'
    PARAMENTOS_DE_VIALIDADES = 'PARAMENTOS_DE_VIALIDADES'
    BANQUETAS_O_ACERAS="BANQUETAS_O_ACERAS"
    VIALIDADES = "VIALIDADES"
    PAVIMENTOS = "PAVIMENTOS"
    MATERIALES_EMPLEADOS_EN_LOS_CAMELLONES = "MATERIALES_EMPLEADOS_EN_LOS_CAMELLONES"
    OTROS_SERVICIOS = "OTROS_SERVICIOS"
    EQUIPAMENTO_Y_MOBILIARIO_URBANO = "EQUIPAMENTO_Y_MOBILIARIO_URBANO"
    NOMENCLATURA_DE_CALLES_Y_SEÑALIZACIÓN  =  "NOMENCLATURA_DE_CALLES_Y_SEÑALIZACIÓN"
    

tipos = ", ".join([ f"'{v.value}'" for v in TipoCaracteristicaAvaluo ])
sql_set_str =  f"({tipos})"

class User(Base):
    __tablename__ ="user"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __str__(self):
        return  json.dumps({"id": self.id, "name": self.name})
    
    def __repr__(self):
        return self.__str__()

class AvaluoCaractetistica(Base):
    __tablename__ ="caracteristica"
    
    id = Column(Integer, primary_key=True)
    titulo  = Column(String(50), unique=True, nullable=False )
    descripcion=  Column(String(250), nullable=False)
    tipo = Column(String(10),nullable=False, index=True)
    ponderacion = Column(Double, nullable=False)

    __table_args__ = (
                CheckConstraint(f"""tipo IN {sql_set_str}"""
                , name='valid_status'),
    )

    def __str__(self):
        return json.dumps({ "id": self.id,"titulo": self.titulo, "descripcion": self.descripcion,"tipo": self.tipo , "ponderacion": self.ponderacion})
    def __repr__(self):
        return self.__str__()
    
        
DATABASE_URL = "sqlite:///./test.db"
#Connect to the database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

#Sesion creation step 
#Esta es una sesion sincrona
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Delete all the tables
Base.metadata.drop_all(bind=engine)
#Create all the tables
Base.metadata.create_all(bind=engine)