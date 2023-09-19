import socket

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

    # Manejar la conexión, procesar datos, etc.
    # Ejemplo: enviar un mensaje al cliente
    client_socket.send(b'Hola, cliente!')

    # Cerrar la conexión con el cliente
    client_socket.close()
