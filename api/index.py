from http.server import BaseHTTPRequestHandler
import json
import os
import sys

# Add parent directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.bumper_engine import BumperEngine

engine = BumperEngine()

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path in ['/', '/index.html']:
            template_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                "web", "templates", "index.html"
            )
            content = b"<!DOCTYPE html><html><body><h1>BUMPER Web GUI</h1></body></html>"
            if os.path.exists(template_path):
                with open(template_path, 'r', encoding='utf-8') as f:
                    content = f.read().encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return

        if self.path in ['/api/stream', '/api/status']:
            payload = engine.get_status_payload()
            response_body = f"data: {json.dumps(payload)}\n\n".encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Connection', 'keep-alive')
            self.end_headers()
            self.wfile.write(response_body)
            return

        self.send_error(404, "File Not Found")

    def do_POST(self):
        if self.path == '/api/bump-now':
            engine.trigger_manual_bump()
            res = json.dumps({"status": "ok", "message": "Manual bump executed"}).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(res)))
            self.end_headers()
            self.wfile.write(res)
            return
        
        self.send_error(404, "Not Found")
