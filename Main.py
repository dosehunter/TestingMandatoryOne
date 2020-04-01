from http.server import HTTPServer, BaseHTTPRequestHandler




class ServePage(BaseHTTPRequestHandler):

    def split_request(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)

        catagories = post_body.decode("utf-8").split("&")
        phones = catagories[0][catagories[0].index("=") + 1:].split("%2C")
        phoneLines = catagories[1][catagories[1].index("=") + 1:]
        interConnections = catagories[2][catagories[2].index("=") + 1:]

        print(phones)
        print(phoneLines)
        print(interConnections)

    def do_POST(self):
        if self.path == "/checkout":
            self.split_request()

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