import grpc
import example_pb2
import example_pb2_grpc

def run():
    channel = grpc.insecure_channel("172.16.12.38:8080")
    stub = example_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(example_pb2.Request(message="World"))
    print("Client received: " + response.message)

if __name__ == "__main__":
    run()
