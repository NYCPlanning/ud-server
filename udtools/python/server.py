from concurrent import futures
import grpc
import logging

import generated.site_pb2_grpc as site_grpc
from models.site import SiteService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    site_grpc.add_SiteServiceServicer_to_server(SiteService(), server)
    server.add_insecure_port('0.0.0.0:9090')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
