#-*- coding:utf-8 -*-
from flask import Flask
from src.module_route.module_ansible import ansible_opt

app = Flask(__name__)
# 注册蓝图，并指定其对应的前缀（url_prefix）
app.register_blueprint(ansible_opt, url_prefix="/ansible_opt")

@app.route("/")
def hello():
    return "Hello, World!"

######################  >>>>> ansible  start <<<<<  #############
# module_ansible.py 使用ansible运维服务器操作
######################  >>>>> ansible  end <<<<<  ###############

# start server    
if __name__ == '__main__':    
    app.run(host='0.0.0.0',port=8089, debug=True)