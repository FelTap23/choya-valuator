# choya-valuator
Choyita valuacion


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
