import http.server
import socketserver
import time

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Registrar la hora de recepción de la solicitud
        start_time = time.time()

        # Construir la respuesta con el mensaje del grupo
        response_message = "Grupo: Gonzalo Scali, Sebastian Serfaty"

        # Calcular el tiempo de respuesta
        end_time = time.time()
        response_time = end_time - start_time

        # Agregar el tiempo de respuesta a la respuesta HTTP
        response_message += f"\nTiempo de respuesta: {response_time:.4f} segundos"
        current_time = time.strftime("%H:%M:%S", time.localtime())

        response_message += f"\nTiempo actual: {current_time}"

        # Responder con el mensaje del grupo y el tiempo de respuesta
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response_message.encode("utf-8"))

# Definir el puerto en el que se ejecutará el servidor
puerto = 8080

# Crear el servidor con el manejador personalizado
with socketserver.TCPServer(("172.16.12.38", puerto), MyHandler) as httpd:
    print("Servidor en el puerto", puerto)

    # Iniciar el servidor
    httpd.serve_forever()
