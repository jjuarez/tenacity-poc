#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from typing import Final, Tuple
from http.server import BaseHTTPRequestHandler, HTTPServer


DEFAULT_HOST_KEY: Final = "HOST"
DEFAULT_PORT_KEY: Final = "PORT"
DEFAULT_HOST_VALUE: Final = "0.0.0.0"
DEFAULT_PORT_VALUE: Final = "8080"


class TenacityServer(BaseHTTPRequestHandler):
    """A basic HTTP server to make the tests of the tenacity rety library"""
    def do_GET(self):
        """A basic HTTP GET"""
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes('{"message":"hello"}', encoding="utf-8"))


class ConfigurationError(Exception):
    """A custom error"""


def setup() -> Tuple[str, int]:
    """Gets the configuration from the environment"""
    host: str = os.environ.get(DEFAULT_HOST_KEY, DEFAULT_HOST_VALUE)
    str_port: str = os.environ.get(DEFAULT_PORT_KEY, DEFAULT_PORT_VALUE)
    try:
        port: int = int(str_port)
    except ValueError:
        raise ConfigurationError(f"The server port must be an integer (0-65535), we got: {str_port}")
    return (host, port)

def main():
    """The main script entrypoint"""

    try:
        config: Tuple[str, int] = setup()
        server: HTTPServer = HTTPServer(config, TenacityServer)
        print(f"Server started http://{config[0]}:{config[1]}/")
        server.serve_forever()
    except ConfigurationError as cexc:
        print(f"We have a configuration error: {cexc}")
    except KeyboardInterrupt:
        print("Server stopped!")


if __name__ == "__main__":
    main()
