from http.server import HTTPServer, BaseHTTPRequestHandler

class ServePage(BaseHTTPRequestHandler):

    def do_POST(self):

        if self.path == "/checkout":
            print("CHECKOUT!")
        try:
            content_len = int(self.headers.get('Content-Length'))
            post_body = self.rfile.read(content_len)
            print(post_body)
        except:
            print("Noes..")

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


httpd = HTTPServer(('localhost', 8080), ServePage)
httpd.serve_forever()