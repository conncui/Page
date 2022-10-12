# -*- coding: UTF-8 -*-

import time
import urllib
from http.server import BaseHTTPRequestHandler, HTTPServer

# Python server
class ServerHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        print ("_set_headers")
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.send_header("test", "This is test!")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        buf = '''<!DOCTYPE HTML>
        <html>
            <head><title>Index page</title></head>
            <body>Hello, world 11!</body>
        </html>'''.encode("utf-8")
        self.wfile.write(buf)

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        # 获取post提交的数据
        datas = self.rfile.read(int(self.headers['Content-Length']))
        datas = urllib.unquote(datas)
        print(self.headers)
        print(datas)

        buf = '''<!DOCTYPE HTML>
        <html>
            <head><title>Post page</title></head>
            <body>Post Data:%s  <br />Path:%s</body>
        </html>''' % (datas, self.path)
        self.wfile.write(buf)


def run_server(handler_class=ServerHandler, port=3100):
    try:
        server_address = ('localhost', port)
        httpd = HTTPServer(server_address, handler_class)
        print('Starting httpd...')
        httpd.serve_forever()
    except Exception as e:
        print ("Error----------------------------------")
        print ("Exception:", e)


if __name__ == '__main__':
    run_server()
