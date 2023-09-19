import socket

# Configuración del cliente
server_host = '172.16.12.38'  # La dirección IP del servidor
server_port = 8080

# Crear un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((server_host, server_port))

# Recibir datos del servidor
data = client_socket.recv(1024)
print(data.decode('utf-8'))

# Cerrar la conexión con el servidor
client_socket.close()
