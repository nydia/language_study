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

# 需要加载的包

## 七牛云
pip3 install qiniu

## 日志库
Loguru是一个Python日志记录库，以其易用性和灵活性而闻名
pip install loguru

#  启动
根目录下运行
```shell
python manage.py runserver
```
默认端口8000，访问页面
1. 首页  http://127.0.0.1:8000/  (设置的默认首页是 http://127.0.0.1:8000/ocrs)
2. 文件上传页面 http://127.0.0.1:8000/files/file_upload_page
3. 文件上传  http://127.0.0.1:8000/files/file_upload
4. 文件登录页面 http://127.0.0.1:8000/files/user_login_page
5. 文件登录 http://127.0.0.1:8000/files/user_login
6. ocr页面 http://127.0.0.1:8000/ocrs/ocr
7. orc识别接口 http://127.0.0.1:8000/ocrs/doocr

# base64转图片
https://www.lddgo.net/convert/base64-to-image