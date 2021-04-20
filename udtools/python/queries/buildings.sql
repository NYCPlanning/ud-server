SELECT
  bin,
  ST_AsText(
    ST_Translate(
      geometry,
      -{{ center_x }},
      -{{ center_y }}
    ) 
  ) as geomwkt,
  ST_Area(geometry) as footprint
FROM
  doitt_buildings
WHERE
  ST_3DIntersects(
    geometry, 
    'SRID=2263;{{ bounds | safe }}'::geometry
  )
LIMIT
    10000;