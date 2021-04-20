template = '''
SELECT
array_agg(DISTINCT b.bin) AS buildings, -- building ids
array_agg(DISTINCT e.edge_id) as edges, -- lot edges from topo
ST_AsText(
  ST_Translate(
    tl.geom,
    -{{ center_x }},
    -{{ center_y }}
  )
) AS geom, -- zoning lot bounds as wkb in local coords
MAX(tl.area) as area
FROM
(
  select
  ST_Union(geom) as geom,
  SUM(ST_Area(geom)) as area
  from 
  public.taxlots
  where
  "BBL" in {{ bbl_array | inclause }}
) as tl
-- spatial join buildings
INNER JOIN public.buildings as b
on ST_Contains(
  tl.geom,
  ST_Centroid(
    ST_SetSRID(
      Box2D(b.geom)::geometry,
      2263
    )
  )
)
-- spatial join topo edges
INNER JOIN (
  select 
  *
  from
  topo_land.edge
) as e
ON ST_DWithin(
  ST_ExteriorRing(tl.geom), 
  ST_Centroid(e.geom),
  1.0
)
GROUP BY tl.geom
'''