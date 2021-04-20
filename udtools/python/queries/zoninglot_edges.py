template = '''
SELECT
e.edge_id as id,
ST_AsText(
  ST_Translate(
    e.geom,
    -{{ center_x }},
    -{{ center_y }}
  )
) as geom,
ST_Azimuth(
  ST_LineInterpolatePoint(e.geom, 0.0),
  ST_LineInterpolatePoint(e.geom, 1.0)
) as azimuth,
ST_Length(e.geom) as length,
coalesce(s.front, False) as front,
s.name as streetname,
s.width as streetwidth
FROM
topo_land.edge AS e
-- spatial join streets
LEFT OUTER JOIN (
  SELECT
  TRUE as front,
  (GetTopoGeomElements(topo))[1] AS face,
  *
  FROM
  public.streets
) AS s
ON s.face IN (e.left_face, e.right_face)
WHERE edge_id in {{ edge_array | inclause }}
;
'''