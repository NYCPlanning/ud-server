#!/usr/bin/env bash
# LAYER: building footprints from DOF

# inputs: update these when new data available
LAYER="buildingfootprint"
SOURCE="https://data.cityofnewyork.us/api/geospatial/nqwf-w8eh?method=export&format=Original"
QUERY="
  SELECT 
    Geometry as geometry,
    bin,
    lstmoddate as modified
  FROM 
    building"


# download source file to temporary folder
if [ -f "$TEMP_FOLDER/${LAYER}.zip" ]; then
  echo "already downloaded"
else
  mkdir -p $TEMP_FOLDER
  wget -O "$TEMP_FOLDER/${LAYER}.zip" $SOURCE
  unzip -qq "$TEMP_FOLDER/${LAYER}.zip" -d $TEMP_FOLDER/$LAYER
fi


# drop table if exists
psql $PG_CONN -c "DROP TABLE IF EXISTS ${LAYER}"


# import to database
ogr2ogr -f "PostgreSQL" \
  PG:$PG_CONN \
  -append \
  -sql $QUERY \
  -dialect sqlite \
  -lco GEOMETRY_NAME=geometry \
  -t_srs "EPSG:2263" \
  -nlt "POLYHEDRALSURFACE Z" \
  -nln $LAYER \
  $TEMP_FOLDER/$LAYER/building.shp


# clear downloaded files
# rm $TEMP_FOLDER/$LAYER.zip
# rm -rf $TEMP_FOLDER/$LAYER
