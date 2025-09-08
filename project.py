import http.server
import socketserver
import requests

# List of backend servers
BACKEND_SERVERS = [
    "http://localhost:8001",
    "http://localhost:8002",
    "http://localhost:8003"
]

# Keep track of which server to use next
current_server = 0

class LoadBalancerHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global current_server

        # Choose the next server in round-robin fashion
        target =
