"""AstroBoy — simple Python HTTP server serving the Three.js space boy."""
import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        print(f"[AstroBoy] {self.address_string()} - {format % args}")


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"AstroBoy serving at http://localhost:{PORT}")
        httpd.serve_forever()
