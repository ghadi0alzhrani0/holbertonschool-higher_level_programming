#!/usr/bin/python3
"""A simple API using the http.server module."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle GET requests for the simple API."""

    def do_GET(self):
        """Send a response depending on the requested endpoint."""

        if self.path == "/":
            message = "Hello, this is a simple API!"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json_data.encode("utf-8"))

        elif self.path == "/status":
            message = "OK"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            json_info = json.dumps(info)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json_info.encode("utf-8"))

        else:
            message = "Endpoint not found"

            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(message.encode("utf-8"))


if __name__ == "__main__":
    server_address = ("", 8000)
    server = HTTPServer(server_address, SimpleAPIHandler)

    print("Server running on http://localhost:8000")
    server.serve_forever()
