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

