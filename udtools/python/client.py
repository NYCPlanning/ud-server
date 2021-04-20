from __future__ import print_function
import grpc
import logging
from shapely import wkt, wkt

import generated.site_pb2_grpc as site_grpc
import generated.site_pb2 as site
# import generated.model_base_pb2 as model
from generated.tax_lot_pb2 import TaxLotMessage
# from models.taxlot import TaxLot
# from models.taxlot import TaxLot

def run():
  with grpc.insecure_channel('0.0.0.0:9090') as channel:
    geom = wkt.loads('POLYGON ((51.0 3.0, 51.3 3.61, 51.3 3.0, 51.0 3.0))')
    taxlot = TaxLotMessage(bbl='1001230001', geom=geom.wkb)
    stub = site_grpc.SiteServiceStub(channel)
    response = stub.MakeSite(taxlot)
    print('received response')
    print(response.id)

if __name__ == '__main__':
  logging.basicConfig()
  run()
