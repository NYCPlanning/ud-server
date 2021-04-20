#!/usr/bin/env bash
# LAYER: ZONING LAYERS FROM DCP

source ../helpers/downloadlayer.sh

LAYER="dcp_zoning"
VERSION="20v10" # version by month of release
SOURCE="https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycgiszoningfeatures_202010fgdb.zip"

# download geodatabase from source
download_layer

# import zoning districts
QUERY="
  SELECT 
    shape as geometry,
    zonedist as name,
    'zd' as type
  FROM 
    nyzd"

ogr2ogr -f "PostgreSQL" \
  PG:$PG_CONN \
  -overwrite \
  -sql $QUERY \
  -t_srs "EPSG:2263" \
  -nln $LAYER \
  -nlt MULTIPOLYGON \
  $TEMP_FOLDER/zoning.gdb

# import commercial overlays
QUERY="
  SELECT
    shape as geometry,
    overlay as name,
    'co' as type
  FROM 
    nyco"

ogr2ogr -f "PostgreSQL" \
  PG:$PG_CONN \
  -append \
  -sql $QUERY \
  -t_srs "EPSG:2263" \
  -nln $LAYER \
  -nlt MULTIPOLYGON \
  $TEMP_FOLDER/zoning.gdb

# import special purpose districts
# note that these tables use 'name' to refer to the machine-readable district code
# while 'label' denotes a human-readable string
QUERY="
  SELECT 
    shape as geometry,
    sdlbl as name,
    sdname as label,
    'sp' as type
  FROM 
    nysp"

ogr2ogr -f "PostgreSQL" \
  PG:$PG_CONN \
  -append \
  -sql $QUERY \
  -t_srs "EPSG:2263" \
  -nln $LAYER \
  -nlt MULTIPOLYGON \
  $TEMP_FOLDER/zoning.gdb

# clear tmp folder 
rm -rf $TEMP_FOLDER

# not yet implemented: 
# nysp_sd - special purpose districts w subdistricts
# nylh - limited ht districts
# nyzma - zoning map amendments
