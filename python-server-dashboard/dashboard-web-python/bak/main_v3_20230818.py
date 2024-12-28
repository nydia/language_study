import json
from http.server import SimpleHTTPRequestHandler
import socketserver
import socket
import jenkins
from jinja2 import Environment,BaseLoader,PackageLoader,FileSystemLoader
from pathlib import Path


class MyRequestHandler(SimpleHTTPRequestHandler):

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

    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(self.Page)))
            self.end_headers()
            self.wfile.write(self.Page.encode("utf-8"))
        elif self.path == "/index":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(self.Page)))
            self.end_headers()

            jenkins_api = JenkinsApi()
            jenkins_api.login()
            jenkins_api.job_list()

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_POST(self):
        if self.path == "/login":
            req = {'code': "0", 'msg': 'OK'}
        elif self.path == "/get_ipaddr":
            req = {'code': "0", 'msg': 'OK', 'ipaddr': socket.gethostbyname(socket.gethostname())}
        elif self.path == "/job_list":
            jenkins_api = JenkinsApi()
            jenkins_api.login()
            jenkins_api.job_list()
            #jenkins_api.job_info('mengxiu-demo-pipeline')
            #jenkins_api.job_info('mengxiu-1')
            #jenkins_api.job_build_env_vars('mengxiu-demo-pipeline',1)
            req = {'code': "0", 'msg': 'OK', 'ipaddr': socket.gethostbyname(socket.gethostname())}
        else:
            req = {'code': "4103", 'msg': 'path error'}

        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()
        rspstr = json.dumps(req)
        self.wfile.write(rspstr.encode("utf-8"))

class JenkinsApi:
    jen = object()
    def __init__(self) -> None:
        pass
    def login(self):
        self.jen = jenkins.Jenkins(url="http://172.30.41.249:8080/", username="admin", password="admin")
        #print(self.jen.get_whoami())
    def job_list(self):
        self.mx_job_list = self.jen.get_jobs()
        print(self.mx_job_list)

        # 创建模板引擎
        #env = Environment(loader=BaseLoader)
        # 添加全局变量
        #env.globals['posts'] = self.mx_job_list
        # 获取一个模板文件
        #with open("templates/index.html") as f:
        #    template_str = f.read()
        #template = env.get_template('templates/index.html')
        # 渲染
        #template.render({"posts":self.mx_job_list})

        script_location = Path(__file__).absolute().parent
        with open(script_location / 'templates/index.html') as f:
            template_str = f.read()
        template = Environment(loader=FileSystemLoader("templates/")).from_string(template_str)
        html_str = template.render({"posts":self.mx_job_list})
        

    def job_info(self,job_name):
        self.mx_job_info = self.jen.get_job_info(name=job_name)
        print(self.mx_job_info)
    def job_build_env_vars(self,job_name,build_n):
        self.mx_job_build_env_vars = self.jen.get_build_env_vars(name=job_name,number=build_n)
        print(self.mx_job_build_env_vars)


if __name__ == '__main__':
    server_host = '127.0.0.1'
    server_port = 8088
    httpd = socketserver.TCPServer((server_host, server_port), MyRequestHandler)
    print('exe_server started on ' + str(server_host) + ' server_port:' + str(server_port))
    httpd.serve_forever()
