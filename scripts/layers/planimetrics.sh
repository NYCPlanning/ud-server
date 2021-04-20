#!/usr/bin/env bash
# MULTIPLE LAYERS: DOITT PLANIMETRICS
# metadata: https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md

source ../helpers/downloadsource.sh
source ../helpers/importplanimetric.sh

VERSION="19v2" # version by updated month
SOURCE="https://data.cityofnewyork.us/download/wt4d-p43d/application%2Fzip"

download_source

import_planimetric "boardwalk"
# CURB (3D Multi Line String)*
# ELEVATION (3D Point)*
import_planimetric "hydro_structure"
import_planimetric "hydrography"
import_planimetric "median"
import_planimetric "misc_structure_poly"
import_planimetric "open_space_no_park"
import_planimetric "park"
import_planimetric "parking_lot"
# PAVEMENT_EDGE (3D Multi Line String)*
import_planimetric "plaza"
# RAILROAD (3D Multi Line String)*
import_planimetric "railroad_structure"
import_planimetric "retainingwall"
import_planimetric "roadbed"
import_planimetric "shoreline"
import_planimetric "sidewalk"
# SIDEWALK_LINE (Multi Line String)
import_planimetric "swimming_pool"
import_planimetric "transport_structure"

# clear tmp folder (turn off for debugging)
rm -rf $TEMP_FOLDER
