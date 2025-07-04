from pydantic import BaseModel, field_validator, model_validator
from pydantic_core.core_schema import FieldValidationInfo
from typing import Literal

from choya.validator.advanced_field_validator import AdvancedFieldValidator
from choya.validator.in_memory_validator import InMemoryValidator

from typing import Literal

class Servicio(BaseModel):
    ponderacion: float
    comentario: str


class ServiciosPublicos(BaseModel):
    class AguaNode(Servicio):
        codigo: Literal[
            "red_de_distribucion_y_suministro_mediante_tomas_domiciliarias",
            "mediante_pipas_de_agua",
            "pozo_medio",
            "pozo_profundo",
            "no_tiene",
        ]

    class DrenajeNode(Servicio):
        codigo: Literal[
            "redes_de_recuperacion_de_aguas_negras_y_pluviales",
            "fosa_septica",
            "sumidero",
            "biodigestor",
            "no_tiene",
        ]

    class ElectrificacionNode(Servicio):
        codigo: Literal[
            "suministro_a_traves_de_redes_aereas_postes_de_concreto_y_luminarias",
            "suministro_subterraneo",
            "paneles_solares",
            "no_tiene",
        ]

    class BanquetaNode(Servicio):
        codigo: Literal[
            "jardinada_ancha", "jardinada_chica", "ancha", "regular", "angosta"
        ]

    class AlumbradoNode(Servicio):
        codigo: Literal[
            "cableado_aereo_concreto_yodo_sodio",
            "suministro_subterraneo",
            "sin_suministro",
        ]

    class PavimentoNode(Servicio):
        codigo: Literal["adoquin", "asfalto", "hidraulico", "terraceria", "empedrado"]

    class CamellonNode(Servicio):
        codigo: Literal["jardinado", "concreto"]

    agua_potable: AguaNode
    drenaje_y_alcantarillado: DrenajeNode
    red_de_electrificacion: ElectrificacionNode
    alumbrado_publico: AlumbradoNode
    vialidades: str
    banquetas: BanquetaNode
    pavimentos: PavimentoNode
    camellones: CamellonNode


class OtrosServicios(BaseModel):
    class RedTelfonicaeNode(Servicio):
        codigo: Literal["si", "no"]

    class RecoleccionDeDesechosNode(Servicio):
        codigo: Literal["si", "no"]

    class TransporteUrbanoNode(Servicio):
        codigo: Literal["si", "no"]

    red_telefonica: RedTelfonicaeNode
    recoleccion_de_desechos: RecoleccionDeDesechosNode
    transporte_urbano: TransporteUrbanoNode


class EquipamientoUrbano(BaseModel):
    class EscuelaNode(Servicio):
        codigo: Literal["si", "no"]

    class SaludNode(Servicio):
        codigo: Literal["si", "no"]

    class ComercialNode(Servicio):
        codigo: Literal["si", "no"]

    escuelas: EscuelaNode
    salud: SaludNode
    comercial: ComercialNode


class CaracteristicasUrbanas(BaseModel):

    # Closed values
    clasificacion_de_la_zona: Literal[
        "habitacional_de_primer_orden",
        "habitacional_de_segundo_orden",
        "habitacional_de_tercer_orden",
        "habitacional_de_interes_social",
        "habitacional_popular",
        "habitacional_residencial",
        "comercial",
        "de_oficinas",
        "industrial",
        "comercial_de_segundo_orden",
        "habitacional_de_primer_orden_y_semi_comercial",
        "habitacional_de_segundo_orden_y_semi_comercial",
        "habitacional_de_tercer_orden_y_semi_comercial",
        "habitacional_de_interes_social_y_semi_comercial",
        "habitacional_popular_y_semi_comercial",
    ]
    tipo_construccion_zona: Literal[
        "casas_habitacion_1_2_niveles_regular_calidad",
        "casas_habitacion_1_2_niveles_buena_calidad",
        "casas_habitacion_1_2_niveles_regular_calidad_locales_pb",
        "casas_habitacion_1_2_niveles_buena_calidad_locales_pb",
        "casas_habitacion_1_2_niveles_regular_calidad_edificios",
        "casas_habitacion_1_2_niveles_buena_calidad_edificios",
        "casas_habitacion_regular_calidad_edificios_comercios",
        "casas_habitacion_buena_calidad_edificios_comercios",
        "edificio_departamentos_buena_calidad",
    ]
    uso_de_suelo: Literal[
        "habitacional",
        "comercial",
        "oficinas",
        "industrial",
        "habitacional_mixto",
        "sin_uso_destinado",
    ]
    poblacion: Literal["normal", "media", "escasa", "alta"]
    saturacion: int
    via_accesso: str

    servicios_publicos: ServiciosPublicos
    otros_servicios: OtrosServicios
    equipamiento_urbano: EquipamientoUrbano
