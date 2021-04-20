#!/usr/bin/env bash
# LAYER: DOT Bike Routes

# versioning by release year/month
LAYER="bikeroutes"
VERSION="20v3"
SOURCE="https://data.cityofnewyork.us/api/geospatial/7vsa-caz7?method=export&format=Original"

LAYERSTRING="${LAYER}_${VERSION}"

mkdir -p ~/tmp
wget -O ~/tmp/${LAYERSTRING}.zip $SOURCE
unzip -qqj ~/tmp/${LAYERSTRING}.zip -d ~/tmp

ogr2ogr -f "PostgreSQL" \
  PG:$PG_CONN \
  -overwrite \
  -select bikedir \
  -lco GEOMETRY_NAME=geometry \
  -t_srs "EPSG:2263" \
  -nln $LAYERSTRING \
  -nlt PROMOTE_TO_MULTI \
  ~/tmp/*.shp

rm -rf ~/tmp