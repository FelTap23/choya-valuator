Choyita valuacion


1. turn on your virtual env. .venv :
 source .venv/bin/activate 
2. run the app : 
 python -m uvicorn main:app --reload
3. send a curl:

curl -i -H "Content-Type: application/json" -X POST  http://localhost:8000/antecedentes -d '{
    "solicitante" : "Fulanito de tal",
    "perito_valuador" : { 
      "nombre" : "Ignacio Lopez",
      "credencial_bienes_inmuebles" : "392/015",
      "registro_INADEJ" : "IND990305-4G50013",
      "cedula_profesional" : "12069869"
      },
    "asesor_valuador" : "Maria Eugenia Lopez",
    "fecha_del_avaluo" : "2023-10-26",
    "tipo_inmueble_a_valuar" :"CASA_HABITACIÓN",
    "regimen_de_propiedad" : "PRIVADA_INDIVIDUAL",
    "propietario_del_inmueble" : "Maria Angelica de la concepcion Lopez Ramirez",
    "proposito_de_avaluo" : "ESTIMAR_SU_VALOR_COMERCIAL",
    "ubicacion_del_inmueble" : "Ildefonso Green",
    "numero_de_cuenta_predial" : "5000-1234-4455-3455",
    "numero_de_cuenta_de_agua" : "4569-5478"
    }'

Payload terreno
curl -X POST \
  "http://localhost:8000/terreno" \
  -H "Content-Type: application/json" \
  -d '{
  "descripcion": "Terreno urbano en zona residencial",
  "medidas_del_terreno_segun": "ESCRITURAS",
  "norte": {
    "medida": 34,
    "descripcion_colindancia": "Calle Emiliano Zapata"
  },
  "sur": {
    "medida": 25.5,
    "descripcion_colindancia": "Propiedad de Juan Pérez Hernández"
  },
  "este": {
    "medida": 12.75,
    "descripcion_colindancia": "Vereda municipal"
  },
  "oeste": {
    "medida": 12.75,
    "descripcion_colindancia": "Con calle morelos"
  },
  "superficie_total_terreno": 325.125,
  "topografia": {
    "aspecto_topografico": "RECTANGULO_REGULAR",
    "incidencia": "NINGUNA",
    "caracteristicas_panoramicas": "SIN_RELEVANCIA",
    "servidumbres_resctricciones": null
  }
}'


Payload Urbanismo 
curl -i -X POST -H "Content-Type: application/json"  "http://localhost:8000/urbanismo" -d '
{
  "clasificacion_de_la_zona": "habitacional_de_primer_orden",
  "tipo_construccion_zona": "casas_habitacion_1_2_niveles_buena_calidad_locales_pb",
  "saturacion": 75,
  "uso_de_suelo": "habitacional",
  "poblacion": "media",
  "via_accesso": "Avenida Principal",

  "servicios_publicos": {
    "agua_potable": {
      "codigo": "AG001",
      "ponderacion": 0.9,
      "comentario": "Servicio adecuado"
    },
    "drenaje_Y_alcantarillado": {
      "codigo": "DR001",
      "ponderacion": 0.8,
      "comentario": "Funciona correctamente"
    },
    "red_electrificacion": {
      "codigo": "EL001",
      "ponderacion": 1.0,
      "comentario": "Sin fallas"
    },
    "alumbrado": {
      "codigo": "AL001",
      "ponderacion": 0.85,
      "comentario": "Bien iluminado"
    },
    "vialidades": {
      "codigo": "VI001",
      "ponderacion": 0.75,
      "comentario": "Algunas calles con baches"
    },
    "banquetas": {
      "codigo": "BA001",
      "ponderacion": 0.7,
      "comentario": "Algunas obstrucciones"
    },
    "pavimentos": {
      "codigo": "PA001",
      "ponderacion": 0.8,
      "comentario": "En mantenimiento"
    },
    "camellones": {
      "codigo": "CA001",
      "ponderacion": 0.6,
      "comentario": "Poco mantenimiento"
    }
  },

  "otros_servicios": {
    "red_telefonica": {
      "codigo": "RT001",
      "ponderacion": 0.9,
      "comentario": "Buena cobertura"
    },
    "servicio_de_limpia": {
      "codigo": "SL001",
      "ponderacion": 0.95,
      "comentario": "Recolección diaria"
    },
    "transporte_urbano": {
      "codigo": "TU001",
      "ponderacion": 0.8,
      "comentario": "Frecuencia adecuada"
    }
  },

  "equipamiento_urbano": {
    "escuelas": {
      "codigo": "ES001",
      "ponderacion": 1.0,
      "comentario": "Diversas opciones educativas"
    },
    "salud": {
      "codigo": "SA001",
      "ponderacion": 0.85,
      "comentario": "Clínicas cercanas"
    },
    "comercial": {
      "codigo": "CO001",
      "ponderacion": 0.9,
      "comentario": "Zonas comerciales accesibles"
    }
  }
}'
