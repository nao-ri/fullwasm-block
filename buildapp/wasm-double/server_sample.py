import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler


# MINEtpyeに application/wasmをTuikaSURU
Handler.extensions_map['.wasm'] = 'application/wasm'
with socketserver.TCPServer(("", 8001), Handler) as httpd:
    print("SERVER port", 8001)
    httpd.serve_forever()