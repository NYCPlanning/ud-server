#!/usr/bin/env bash
# LAYER: DOT Bike Racks
# comments: needs -skipfailures flag as some features in source fail reproject

# inputs: update these when new data available
LAYER="bikeparking"
VERSION="19v1"
SOURCE="https://data.cityofnewyork.us/api/geospatial/yh4a-g3fj?method=export&format=Shapefile"

LAYERSTRING="${LAYER}_${VERSION}"

mkdir -p ~/tmp
wget -O ~/tmp/${LAYERSTRING}.zip $SOURCE
unzip -qq ~/tmp/${LAYERSTRING}.zip -d ~/tmp

ogr2ogr -f "PostgreSQL" \
  PG:$PG_CONN \
  -overwrite \
  -skipfailures \
  -select bbl \
  -lco GEOMETRY_NAME=geometry \
  -t_srs "EPSG:2263" \
  -nln $LAYERSTRING \
  ~/tmp/*.shp

# clear tmp folder (turn off for debugging)
rm -rf ~/tmp