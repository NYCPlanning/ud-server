SELECT
  bbl,
  geometry as geom_sp,
  ST_AsText(
    ST_Translate(
      geometry,
      -{{ center_x }},
      -{{ center_y }}
    )
  ) as geomwkt,
  ST_Area(geometry) as lotarea,
  block,
  lot,
  address,
  ownername,
  bldgclass,
  landmark,
  landuse as landusecode,
  concat_ws(' ', zonedist1, zonedist2, zonedist3, zonedist4) as zonesexisting,
  resarea,
  unitsres,
  garagearea,
  retailarea,
  officearea,
  (officearea + garagearea + retailarea) as commercialarea,
  factryarea,
  strgearea,
  (strgearea + factryarea) as manufacturingarea,
  bldgarea
FROM
  dcp_taxlots
WHERE
  ST_Intersects(geometry, 'SRID=2263;{{ bounds | safe }}'::geometry)
LIMIT
  10000;