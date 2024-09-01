##############################################
# This file is part of the project credentials-git.
# This Source Code Form is subject to the license in the file LICENSE
#
# (c) Philipp Lies <phil@lies.io>
##############################################
from http.server import BaseHTTPRequestHandler, HTTPServer
import os


# Super basic webserver that reads the contents of credentials.key and displays it
# Technically just here so we don't have an empty repo, but still a valid solution
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if os.path.exists("credentials.key"):
            with open("credentials.key", "r") as f:
                self.wfile.write(
                    f"<html><body><h1>{f.read()}</h1></body></html>".encode()
                )
        else:
            self.wfile.write(
                b"<html><body><h1>credentials.key does not exist</h1></body></html>"
            )


def run() -> None:
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, MyServer)
    print("Starting server...")
    httpd.serve_forever()


run()
