#-*- coding:utf-8 -*-
import BaseHTTPServer
import json
import os

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''处理请求并返回页面'''

    # 页面模板
    Page = '''\
        <html>
        <body>
        <p>deploy success!</p>
        </body>
        </html>
    '''


    def _send_cors_headers(self):
        """ Sets headers required for CORS """
        self.send_header('Content-type', 'application/json')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "*")
        self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type")

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()
 
    # 处理一个GET请求
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page)

    def do_POST(self):
        if self.path == "/login":
            req = {'code': "0", 'msg': 'OK'}
        else:
            req = {'code': "403", 'msg': 'path error'}

        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()
        rspstr = json.dumps(req)
        self.wfile.write(rspstr.encode("utf-8"))


if __name__ == '__main__':
    serverAddress = ('', 8088)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()