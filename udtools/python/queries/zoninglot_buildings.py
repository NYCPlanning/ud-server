template = '''
SELECT
b.bin,
ST_AsText(
  ST_Translate(
    b.envelope_geom,
    -{{ center_x }},
    -{{ center_y }}
  )
) as envelope,
MAX(ST_Area(b.geom)) as footprint,
json_agg(
  json_build_object(
    'index', b.path[1],
    'geom', ST_AsText(
      ST_Translate(
        b.geom,
        -{{ center_x }},
        -{{ center_y }}
      )
    ),
    'lot_edge', e.edge_id,
    'wall', COALESCE(ST_Area(b.geom) < 1.0, false)
    -- possible/useful to also get azimuth?
  )
) as faces
FROM (
  select
  bin,
  geom as envelope_geom,
  (ST_Dump(geom)).* -- gives both path and geom
  from
  public.buildings
  where
  bin in {{ bldg_array | inclause }}
) b-- building faces
LEFT OUTER JOIN (
  select * from topo_land.edge
  where edge_id in {{ edge_array | inclause }}
) as e
ON ST_DWithin(
  e.geom,
  ST_Centroid(
  -- ST_ApproximateMedialAxis(
    b.geom
  ),
  3.0 -- 1ft tolerance to detect intersecting
)
GROUP BY b.bin, b.envelope_geom
;
'''