#!/usr/bin/env bash
# LAYER: LINKNYC locations from DOITT

# version by release month
LAYER="linknyc"
VERSION="19v9"
SOURCE="https://data.cityofnewyork.us/api/geospatial/7b32-6xny?method=export&format=Original"

LAYERSTRING="${LAYER}_${VERSION}"
PG_CONN="host=localhost user=${POSTGRES_USER} dbname=${POSTGRES_DBNAME} password=${POSTGRES_PASS}" 

mkdir -p ~/tmp
wget -O ~/tmp/${LAYERSTRING}.zip $SOURCE
unzip -qq ~/tmp/${LAYERSTRING}.zip -d ~/tmp

ogr2ogr -f "PostgreSQL" \
  PG:$PG_CONN \
  -overwrite \
  -select site_id \
  -lco GEOMETRY_NAME=geometry \
  -t_srs "EPSG:2263" \
  -nln $LAYERSTRING \
  ~/tmp/*.shp

rm -rf ~/tmp