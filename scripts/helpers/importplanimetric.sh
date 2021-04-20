#!/usr/bin/env bash

import_planimetric() {
  LAYER="doitt_${1//_/}"

  QUERY="
    SELECT 
      shape as geometry
    FROM 
      ${1}"
  
  psql $PG_CONN -c "DROP TABLE ${LAYER};"

  ogr2ogr -f "PostgreSQL" \
    PG:$PG_CONN \
    -overwrite \
    -sql $QUERY \
    -lco GEOMETRY_NAME=geometry \
    -t_srs "EPSG:2263" \
    -nln $LAYER \
    -nlt CONVERT_TO_LINEAR \
    $TEMP_FOLDER/*.gdb
  echo "imported ${LAYER}"
}