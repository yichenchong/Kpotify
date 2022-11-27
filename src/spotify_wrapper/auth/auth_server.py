from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class AuthServerHandler(BaseHTTPRequestHandler):
    code = None
    state = None

    def log_message(self, format, *args):
        return

    def do_GET(self):
        parsed_path = urlparse(self.path)
        print(parse_qs(parsed_path.query))
        AuthServerHandler.code = parse_qs(parsed_path.query)['code'][0]
        AuthServerHandler.state = parse_qs(parsed_path.query)['state'][0]
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'You may now close this window.')
        return

    @staticmethod
    def get_code():
        code = AuthServerHandler.code
        AuthServerHandler.code = None
        return code

    @staticmethod
    def get_state():
        state = AuthServerHandler.state
        AuthServerHandler.state = None
        return state


def wait_for_auth_code(server_class=HTTPServer, handler_class=AuthServerHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.handle_request()
    return AuthServerHandler.get_code(), AuthServerHandler.get_state()
