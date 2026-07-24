#!/usr/bin/env python3
import webbrowser
import threading
import time
from server import start_server, PORT

def open_browser():
    time.sleep(1.2)
    url = f"http://localhost:{PORT}"
    print(f"🚀 Opening Bumper Web GUI in browser: {url}")
    webbrowser.open(url)

if __name__ == "__main__":
    threading.Thread(target=open_browser, daemon=True).start()
    start_server(PORT)
