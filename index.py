import socketserver

import http.server

# Define the server address and port
host = "localhost"
port = 8000

# Create a request handler class
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, World!")
        elif self.path == "/about":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"About page")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Page not found")

# Create the server object
with socketserver.TCPServer((host, port), MyRequestHandler) as server:
    print(f"Server running at http://{host}:{port}")
    server.serve_forever()