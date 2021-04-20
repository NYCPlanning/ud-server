#!/usr/bin/env bash
# LAYER: TAX LOTS FROM DCP MAPPLUTO
source ../helpers/downloadlayer.sh

LAYER="streetcenterline"
VERSION="20v10"
SOURCE="https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/dcm_20201031fgdb.zip"
QUERY="
  SELECT
    shape as geometry,
    Street_NM as name,
    Streetwidth as width
  FROM 
    DCM_StreetCenterLine"

download_layer

ogr2ogr -f "PostgreSQL" \
  PG:$PG_CONN \
  -overwrite \
  -sql $QUERY \
  -t_srs "EPSG:2263" \
  -nln $LAYER \
  -nlt "MULTILINESTRING Z" \
  $TEMP_FOLDER/*.gdb

# clear tmp folder (turn off for debugging)
rm -rf $TEMP_FOLDER
