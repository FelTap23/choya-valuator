Choyita valuacion


1. turn on your virtual env. .venv :
 source .venv/bin/activate 
2. run the app : 
 python -m uvicorn main:app --reload
3. send a curl:

curl -i -H "Content-Type: application/json" -X POST  http://localhost:8000/antecedentes -d '{
    "solicitante" : "Fulanito de tal",
    "perito_valuador" : "Ignacio Lopez",
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