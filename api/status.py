from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        payload = {
            "status": "success",
            "series": "Commercial Coloring Book Pipeline",
            "books": [
                {
                    "id": "capybara",
                    "title": "Barnaby's Peaceful Days",
                    "niche": "Bold & Easy Cozy Capybara",
                    "status": "completed"
                },
                {
                    "id": "canada",
                    "title": "Autumn in Canada: A Scenic Journey Across Provinces & Territories",
                    "niche": "30 Scenic Landscapes in Dong Ho Multi-Layer Woodblock",
                    "status": "completed"
                }
            ],
            "specs": {
                "pages": 64,
                "trim_size": "8.5x8.5 inches",
                "dpi": 300,
                "format": "KDP Paperback & Etsy Digital Bundle"
            }
        }
        self.wfile.write(json.dumps(payload).encode('utf-8'))
        return
