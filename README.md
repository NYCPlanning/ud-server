# UD Server

Web services to support UDTools and other DCP Urban Design products, using:

- [PostGIS](https://postgis.net/)
- [Geoserver](https://github.com/geoserver/geoserver)
- [Hasura GraphQL Engine](https://github.com/hasura/graphql-engine)
- [Strapi CMS](https://github.com/strapi/strapi)

## Setup

Create a `.env` from `.env.template` at the repository root, then run `docker-compose up`. `SERVER_HOST` can be either your local machine for testing or a remote server such as a Digital Ocean Droplet, and needs to have Docker installed and running.

Once the server is online, run various `scripts` to load/update data from different sources, for example...

```sh
$ bash scripts/layers/streettrees.sh
```

...will import the latest street tree census to PostGIS.

At this time, Geoserver and Hasura endpoints for individual database layers still need to be configured manually, access their web dashboards at `{SERVER_HOST}:8881/geoserver/web/` and `{SERVER_HOST}:8882/console/login` and follow the appropriate setup instructions for each service. The CMS web dashboard is at `{SERVER_HOST}:8883/admin/`.

Scripts under `layers` point to the following City of New York spatial data products:

| Layer | Source | Metadata |
|---|---|---|
| `boardwalk` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `buildings` | DOITT [NYC 3-D Building Model](https://www1.nyc.gov/site/doitt/initiatives/3d-building.page) | [link](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_3DBuildingModel.md) |
| `elevation` | DOITT [1 Foot Digital Elevation Model (Integer)](https://data.cityofnewyork.us/City-Government/1-foot-Digital-Elevation-Model-DEM-Integer-Raster/7kuu-zah7) | [link](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_DigitalElevationModel.md) |
| `hydrography` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `hydrostructure` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `median` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `miscstructurepoly` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `openspacenopark` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `park` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `parkinglot` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `plaza` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `railroadstructure` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `retainingwall` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `roadbed` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `shoreline` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `sidewalk` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `streetcenterline` | DCP [Digital City Map](https://www1.nyc.gov/site/planning/data-maps/open-data.page#digitalcitymap) | [link](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-digital-city-map.page#metadata) |
| `streettrees` | DPR [Street Tree Census](https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh) | [link](https://data.cityofnewyork.us/api/views/uvpi-gqnh/files/8705bfd6-993c-40c5-8620-0c81191c7e25?download=true&filename=StreetTreeCensus2015TreesDataDictionary20161102.pdf) |
| `swimmingpool` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `taxlots` | DCP [MapPLUTO](https://www1.nyc.gov/site/planning/data-maps/open-data.page#pluto) | [link](https://www1.nyc.gov/assets/planning/download/pdf/data-maps/open-data/meta_mappluto.pdf?r=20v6) |
| `transportstructure` | DOITT [Planimetrics](https://data.cityofnewyork.us/Transportation/NYC-Planimetrics/wt4d-p43d) | [link](https://github.com/CityOfNewYork/nyc-planimetrics/blob/master/Capture_Rules.md) |
| `zoning` | DCP [NYC GIS Zoning Features](https://www1.nyc.gov/site/planning/data-maps/open-data.page#zoning_related) | [link](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-gis-zoning.page#metadata) |
