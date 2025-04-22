from http.server import BaseHTTPRequestHandler, HTTPServer

class Hx(BaseHTTPRequestHandler):
    def do_POST(self):
        l = int(self.headers['Content-Length'])
        d = self.rfile.read(l)

        fn = self.headers.get('File-Name', 'x.tmp')
        with open(f'recv_{fn}', 'wb') as f:
            f.write(d)

        print(f"[#] Got: {fn}")
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    s = HTTPServer(('0.0.0.0', 8000), Hx)  # Listening on all interfaces
    print(":: Server listening on http://192.168.56.1:8000 ::")
    s.serve_forever()
