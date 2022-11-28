from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class AuthServerHandler(BaseHTTPRequestHandler):

    """
    
    """

    # static variables
    code = None
    state = None

    def log_message(self, format, *args):
        # disables server logging
        return

    def do_GET(self):
        """
        Handles GET requests.
        In this case, the only GET request is the one that is sent to the redirect_uri
        after the user has logged in and authorized the application. It logs the code
        and state parameters.

        :return: None
        """
        parsed_path = urlparse(self.path)
        AuthServerHandler.code = parse_qs(parsed_path.query)['code'][0]
        AuthServerHandler.state = parse_qs(parsed_path.query)['state'][0]
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'You may now close this window.')
        return

    @staticmethod
    def get_code():
        """
        Returns the code parameter from the GET request.

        :return: code parameter
        :rtype: str
        """
        code = AuthServerHandler.code
        AuthServerHandler.code = None
        return code

    @staticmethod
    def get_state():
        """
        Returns the state parameter from the GET request.

        :return: state parameter
        :rtype: str
        """
        state = AuthServerHandler.state
        AuthServerHandler.state = None
        return state


def wait_for_auth_code(handler_class=AuthServerHandler):
    """
    Starts a local HTTP server and waits for a GET request to the redirect_uri.

    :param handler_class: AuthServerHandler class
    :type handler_class: BaseRequestHandler
    :return: code and state parameters
    :rtype: tuple
    """
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, handler_class)
    httpd.handle_request()
    return AuthServerHandler.get_code(), AuthServerHandler.get_state()
