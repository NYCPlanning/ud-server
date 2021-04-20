#!/usr/bin/env bash
# LAYER: DIGITAL ELEVATION RASTER
# not in use, instead use desktop software to obtain integer raster, resample to 10' resolution
# to get DEM_int_10ft.tif
# then upload with the raster2pgsql call below

source ../helpers/downloadlayer.sh

LAYER="elevation"
VERSION="18v1"
SOURCE="https://sa-static-customer-assets-us-east-1-fedramp-prod.s3.amazonaws.com/data.cityofnewyork.us/NYC_DEM_1ft_Int.zip"

download_layer

# raster2pgsql \
#   -s 2263 \
#   -d \
#   -I \
#   -C \
#   -M \
#   -t 512x512 \
#   ~/tmp/*.tif \
#   $LAYER \
#   | psql $PG_CONN

raster2pgsql \
  -s 2263 \
  -I \
  -C \
  -M \
  DEM_int_10ft.tif \
  -t 500x500 \
  "public.${LAYER}" \
  | psql $PG_CONN

# clean up temp folder
rm -rf $TEMP_FOLDER
