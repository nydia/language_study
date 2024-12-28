#-*- coding:utf-8 -*-
import BaseHTTPServer
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

    # 处理一个GET请求
    def do_GET(self):
        self.do_exec_shell()

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page)

    def do_exec_shell(self):
        os.system("/home/oper/h5/deploy_sit.sh deploy")

if __name__ == '__main__':
    serverAddress = ('', 8088)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()