#No me borres guey :V
# from choya.db.model import SessionLocal,  AvaluoCaractetistica, TipoCaracteristicaAvaluo
# from functools import reduce

from choya.config.avaluo_configuration import load_app_properties, load_yaml_second_approach

if __name__ == "__main__":
    #No me borres guey :V
    # db = SessionLocal()
    # zona : AvaluoCaractetistica = AvaluoCaractetistica(titulo = "Alfa",descripcion = "asas",tipo = "OTROS_SERVICIOS", ponderacion  = 0.0)
    # db.add(zona)
    # db.commit()
    # db.refresh(zona)
    
    # zonas = db.query(AvaluoCaractetistica).all()
    # print(zonas)
    
    #Firs approach
    # properties = load_app_properties()
    # for avaluo in properties.AVALUO_CARACTERSITICAS_LIST:
    #     print(avaluo)

    load_yaml_second_approach()

    
