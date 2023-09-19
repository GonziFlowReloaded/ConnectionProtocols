import grpc
import concurrent.futures
import example_pb2
import example_pb2_grpc
from datetime import datetime  # Importar datetime

class GreeterServicer(example_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Obtener la hora actual en formato YYYY-MM-DD HH:MM:SS
        response = example_pb2.Response()
        response.message = f"{current_time} - Grupo Gonzalo Scali, Sebastian Serfaty"
        return response

def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("172.16.12.38:8080")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
