#!/usr/bin/env bash
# LAYER: 3D BUILDINGS FROM DOITT

# inputs: update these when new data available
LAYER="buildings"
VERSION="16v1"
SOURCE="http://maps.nyc.gov/download/3dmodel/DA_WISE_Multipatch.zip"
QUERY="
  SELECT 
    shape as geometry,
    bin 
  FROM 
    Buildings_3D_Multipatch"

# download source file to temporary
mkdir -p $TEMP_FOLDER
wget -O "$TEMP_FOLDER/${LAYER}.zip" $SOURCE
unzip -qq "$TEMP_FOLDER/${LAYER}.zip" -d $TEMP_FOLDER

# drop table if exists
psql $PG_CONN -c "DROP TABLE IF EXISTS ${LAYER}"

# loop over downloaded+extracted files, send contents to database
for f in $TEMP_FOLDER/DA_WISE_Multipatch/*.gdb
do
    ogr2ogr -f "PostgreSQL" \
      PG:$PG_CONN \
      -append \
      -sql $QUERY \
      -lco GEOMETRY_NAME=geometry \
      -t_srs "EPSG:2263" \
      -nlt "POLYHEDRALSURFACE Z" \
      -nln $LAYER \
      $f
done

# deal with data issues

# delete ~4k records from bin without any results in BISweb
psql $PG_CONN -c "DELETE FROM doitt_buildings WHERE bin=3000000;"

# create indexes
psql $PG_CONN -c "CREATE INDEX bin_idx ON ${LAYER}(bin);"

# clear tmp folder
rm -rf $TEMP_FOLDER