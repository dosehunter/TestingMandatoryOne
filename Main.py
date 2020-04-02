#!/usr/bin/env python
from http.server import HTTPServer, BaseHTTPRequestHandler
from Splitter_Class import Splitter

class ServePage(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path == "/checkout":
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)

            split = Splitter()
            split.split_request(post_body)

        try:
            file = open(self.path[1:] + ".html").read()
            self.send_response(200)
        except:
            file = "File not found!"
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(file, 'utf-8'))

    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        try:
            file = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file = "File not found!"
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(file, 'utf-8'))


httpd = HTTPServer(('localhost', 5000), ServePage)
httpd.serve_forever()