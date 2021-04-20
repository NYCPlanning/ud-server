#!/usr/bin/env bash
# LAYER: DPR STREET TREES

source ../helpers/downloadsource.sh

LAYER="dpr_streettree"
VERSION="19v1"
SOURCE="https://data.cityofnewyork.us/api/views/5rq2-4hqu/rows.csv?accessType=DOWNLOAD"

download_source_csv

ogr2ogr -f "PostgreSQL" \
  PG:$PG_CONN \
  -overwrite \
  -s_srs "EPSG:2263" \
  -select tree_id \
  -lco PRECISION=NO \
  -lco GEOMETRY_NAME=geometry \
  -oo X_POSSIBLE_NAMES=x_sp \
  -oo Y_POSSIBLE_NAMES=y_sp \
  -oo KEEP_GEOM_COLUMNS=no \
  -t_srs "EPSG:2263" \
  -nln $LAYER \
  $TEMP_FOLDER/*.csv

rm -rf $TEMP_FOLDER
