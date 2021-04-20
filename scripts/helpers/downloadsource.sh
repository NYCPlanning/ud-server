#!/usr/bin/env bash

download_source () {
  mkdir -p $TEMP_FOLDER
  wget -O $TEMP_FOLDER/${LAYER}.zip $SOURCE
  unzip -qq $TEMP_FOLDER/${LAYER}.zip -d $TEMP_FOLDER
}

download_source_csv () {
  mkdir -p $TEMP_FOLDER
  wget -O $TEMP_FOLDER/${LAYER}.csv $SOURCE
}