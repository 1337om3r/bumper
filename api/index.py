import json
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.bumper_engine import BumperEngine

engine = BumperEngine()

def handler(request):
    """Vercel Serverless Function Handler."""
    path = getattr(request, "path", "/")
    method = getattr(request, "method", "GET")

    if path in ["/", "/index.html"]:
        template_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "web", "templates", "index.html"
        )
        if os.path.exists(template_path):
            with open(template_path, "r", encoding="utf-8") as f:
                content = f.read()
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "text/html; charset=utf-8"},
                "body": content
            }

    if "/api/bump-now" in path and method == "POST":
        engine.trigger_manual_bump()
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"status": "ok", "message": "Manual bump triggered"})
        }

    if "/api/stream" in path or "/api/status" in path:
        payload = engine.get_status_payload()
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/event-stream",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive"
            },
            "body": f"data: {json.dumps(payload)}\n\n"
        }

    return {
        "statusCode": 404,
        "headers": {"Content-Type": "text/plain"},
        "body": "404 Not Found"
    }
