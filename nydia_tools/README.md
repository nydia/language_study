#  介绍
一款Python语言工具包


# 目录
## nydia_tools 
主应用程序
- urls.py 所有子应用url都需要汇集到这里
- settings.py 公用设置，静态资源路径设置
## ocrs
子应用 - ocr识别工具
- migrations： 为迁移文件夹，和数据库交互用到的；
- admin：是用来管理页面的；
- apps：是设置应用程序的名称等信息；
- models：模型，和后台数据库相关，我们在这里创建对象，数据库就可以自动的生成表；
- tests：测试文件；
- views：视图相关
## files
子应用 - 文件模块
## 常用的工作包



# 需要加载的包

## 七牛云
pip3 install qiniu

## 日志库
Loguru是一个Python日志记录库，以其易用性和灵活性而闻名
pip install loguru

## ChatGPT
pip install openai


#  启动
根目录下运行
```shell

python manage.py runserver

# docker内部启动
nohup /opt/soft/Python3.11.4/bin/python3.11 /opt/soft/nydia_tools/manage.py runserver 0.0.0.0:8000 &

```

默认端口8000，访问页面
1. 首页  http://127.0.0.1:8000/  (设置的默认首页是 http://127.0.0.1:8000/ocrs)
2. 文件上传页面 http://127.0.0.1:8000/files/file_upload_page
3. 文件上传  http://127.0.0.1:8000/files/file_upload
4. 文件登录页面 http://127.0.0.1:8000/files/user_login_page
5. 文件登录 http://127.0.0.1:8000/files/user_login
6. ocr页面 http://127.0.0.1:8000/ocrs/ocr
7. orc识别接口 http://127.0.0.1:8000/ocrs/doocr
8. 工具首页 http://127.0.0.1:8000/tools/tools_index.html


外部地址:
1. 首页  http://101.43.47.38:8000/  (设置的默认首页是 http://127.0.0.1:8000/ocrs)
2. 文件上传页面 http://101.43.47.38:8000/files/file_upload_page
3. 文件上传  http://101.43.47.38:8000/files/file_upload
4. 文件登录页面 http://101.43.47.38:8000/files/user_login_page
5. 文件登录 http://101.43.47.38:8000/files/user_login
6. ocr页面 http://101.43.47.38:8000/ocrs/ocr
7. orc识别接口 http://101.43.47.38:8000/ocrs/doocr

域名地址：
1. 文件上传页面
http://www.91ocr.asia/tools/files/file_upload_page  （经过ng代理了）


# django在linux部署
python组件导入导出（这里是全量导入导出，最好利用虚拟环境缩小包的范围）
导出：  pip freeze > requirements.txt
导入： pip install -r requirements.txt

# 验证工具
## base64转图片
https://www.lddgo.net/convert/base64-to-image

# 版本计划
1. 七牛云文件上传。（v1.0.0：files模块已经实现） 
2. 在tools模块集成vue，使用块状形式集成通用的工具栏模块。（v1.0.0：files模块已经实现）
3. 做一个家庭监控：温度，适度等，接入mqtt。
4. 接入gpt，做一个智能作业解析工具。
5. 文件下载解析工具。（v1.0.0:  tools模块已经实现,目前没有页面）


# Openai ChatGPT


# 单元测试
cd到项目的根目录下面：

1. 测试tools模块
python manage.py test tools.tests.ToolsTest