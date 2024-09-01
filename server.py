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
    page_template = "<html><body><h1>{text}</h1></body></html>"

    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if os.path.exists("credentials.key"):
            with open("credentials.key", "r") as f:
                self.wfile.write(
                    self.page_template.format(text=f.read()).encode("utf-8")
                )
        else:
            self.wfile.write(
                self.page_template.format(text="No credentials found").encode("utf-8")
            )


def run() -> None:
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, MyServer)
    print("Starting server...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
