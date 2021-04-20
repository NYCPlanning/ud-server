#!/usr/bin/env bash
# LAYER: TAX LOTS FROM DCP MAPPLUTO
source ../helpers/downloadlayer.sh

LAYER="dcp_taxlots"
VERSION="20v7"
SOURCE="https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyc_mappluto_${VERSION}_fgdb.zip"
QUERY="
  SELECT
    shape as geometry,
    bbl,
    block,
    lot,
    address,
    ownername,
    bldgclass,
    landmark,
    landuse,
    zonedist1,
    zonedist2,
    zonedist3,
    zonedist4,
    bldgarea,
    comarea,
    resarea,
    unitsres,
    officearea,
    retailarea,
    garagearea,
    strgearea,
    factryarea,
    otherarea
  FROM 
    MapPLUTO_${VERSION}_clipped"

download_source

ogr2ogr -f "PostgreSQL" \
  PG:$PG_CONN \
  -overwrite \
  -sql $QUERY \
  -t_srs "EPSG:2263" \
  -nln $LAYER \
  $TEMP_FOLDER/*.gdb

# create indexes
psql $PG_CONN -c "CREATE UNIQUE INDEX bbl_idx ON ${LAYER}(bbl);"

# clear tmp folder (turn off for debugging)
rm -rf $TEMP_FOLDER