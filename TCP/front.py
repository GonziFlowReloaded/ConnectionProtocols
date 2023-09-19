import socket

# Configuración del cliente
server_host = '172.16.12.54'  # La dirección IP del servidor
server_port = 8000

# Crear un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((server_host, server_port))

# Enviar una solicitud al servidor
request = "Hola, servidor!"
client_socket.send(request.encode('utf-8'))

# Recibir datos del servidor
response = client_socket.recv(1024).decode('utf-8')

# Cerrar la conexión con el servidor
client_socket.close()

# Mostrar el tiempo de respuesta recibido del servidor
print(f'Tiempo de respuesta del servidor: {response}')
