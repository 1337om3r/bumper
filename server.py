import http.server
import socketserver
import json
import os
import sys

from core.bumper_engine import BumperEngine

PORT = 8085
engine = BumperEngine()

class BumperHTTPHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path in ['/', '/index.html']:
            template_path = os.path.join(os.path.dirname(__file__), "web", "templates", "index.html")
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
        content_length = int(self.headers.get('Content-Length', 0))
        body_data = self.rfile.read(content_length) if content_length > 0 else b'{}'
        
        try:
            body_json = json.loads(body_data.decode('utf-8'))
        except Exception:
            body_json = {}

        if self.path == '/api/bump-now':
            engine.trigger_manual_bump()
            res = json.dumps({"status": "ok", "message": "Manual bump executed"}).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(res)))
            self.end_headers()
            self.wfile.write(res)
            return

        if self.path == '/api/add-token':
            name = body_json.get("name", "User-Token")
            token = body_json.get("token", "")
            channel_id = body_json.get("channel_id", "")
            engine.add_token(name, token, channel_id)
            res = json.dumps({"status": "ok", "message": "Token added"}).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(res)))
            self.end_headers()
            self.wfile.write(res)
            return

        if self.path == '/api/delete-token':
            idx = body_json.get("index", 0)
            engine.remove_token(idx)
            res = json.dumps({"status": "ok", "message": "Token deleted"}).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(res)))
            self.end_headers()
            self.wfile.write(res)
            return
        
        self.send_error(404, "Not Found")

def start_server(port=PORT):
    with socketserver.TCPServer(("", port), BumperHTTPHandler) as httpd:
        print(f"⚡ Bumper Web GUI server running at http://localhost:{port}")
        httpd.serve_forever()

if __name__ == '__main__':
    start_server()
