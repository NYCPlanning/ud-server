#!/usr/bin/env bash
# LAYER: FIRE HYDRANTS FROM DEP

LAYER="hydrants"
VERSION="19v1"
SOURCE="https://data.cityofnewyork.us/api/geospatial/6pui-xhxz?method=export&format=Shapefile"

LAYERSTRING="${LAYER}_${VERSION}"
PG_CONN="host=localhost user=${POSTGRES_USER} dbname=${POSTGRES_DBNAME} password=${POSTGRES_PASS}" 

mkdir -p ~/tmp
wget -O ~/tmp/${LAYERSTRING}.zip $SOURCE
unzip -qq ~/tmp/${LAYERSTRING}.zip -d ~/tmp

ogr2ogr -f "PostgreSQL" \
  PG:$PG_CONN \
  -overwrite \
  -select unitid \
  -lco GEOMETRY_NAME=geometry \
  -t_srs "EPSG:2263" \
  -nln $LAYERSTRING \
  ~/tmp/*.shp

# clear tmp folder (turn off for debugging)
rm -rf ~/tmp