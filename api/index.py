from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        payload = {
            "status": "success",
            "project": "Barnaby's Peaceful Days",
            "niche": "Bold & Easy Cozy Capybara",
            "specs": {
                "pages": 64,
                "trim_size": "8.5x8.5 inches",
                "dpi": 300
            }
        }
        self.wfile.write(json.dumps(payload).encode('utf-8'))
        return
