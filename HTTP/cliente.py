import http.client

# Conectar al servidor HTTP
conn = http.client.HTTPConnection("localhost", 8080)  # Cambia "localhost" al dominio o IP del servidor si es necesario

# Realizar una solicitud GET
conn.request("GET", "/")

# Obtener la respuesta
response = conn.getresponse()

# Leer y mostrar la respuesta
data = response.read()
print(data.decode("utf-8"))

# Cerrar la conexión
conn.close()
