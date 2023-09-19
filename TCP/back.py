import socket
import time

# Configuración del servidor
host = '172.16.12.38'  # Puedes usar cualquier dirección IP o dejarlo en blanco para escuchar en todas las interfaces
port = 8080

# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket al host y puerto
server_socket.bind((host, port))

# Escuchar conexiones entrantes
server_socket.listen(5)

while True:
    # Aceptar la conexión entrante
    client_socket, addr = server_socket.accept()
    print(f'Conexión entrante de {addr}')

    # Medir el tiempo de respuesta
    start_time = time.time()

    # Manejar la conexión, procesar datos, etc.
    # Ejemplo: recibir una solicitud del cliente
    request = client_socket.recv(1024).decode('utf-8')
    print(f'Solicitud del cliente: {request}')

    # Simular un procesamiento demorado (para demostración)
    time.sleep(2)

    # Enviar el tiempo de respuesta al cliente
    end_time = time.time()
    response_time = end_time - start_time
    response_message = f'Tiempo de respuesta: {response_time:.2f} segundos'
    client_socket.send(response_message.encode('utf-8'))

    # Cerrar la conexión con el cliente
    client_socket.close()