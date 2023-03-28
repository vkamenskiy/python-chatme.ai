import os
from http.server import BaseHTTPRequestHandler
import requests


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(
            self.headers["Content-Length"]
        )
        post_data = self.rfile.read(content_length).decode("utf-8")
        requests.post(
            f"https://api.telegram.org/bot{os.environ.get('BOT_TOKEN')}/sendMessage",
            {"text": post_data, "chat_id": int(os.environ.get('CHAT_ID'))},
        )

        self.send_response(200, message=None)
        self.end_headers()
