# 使用一个基础镜像作为起点
FROM 172.30.41.248/base_images/unbuntu_mengxiu:23.10

# 设置工作目录
WORKDIR /app

# 复制当前目录的所有文件到容器中
COPY . /app

# 安装依赖
RUN pip --default-timeout=100 install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn -r /app/requirements/requirements.txt

# 定义容器启动时执行的命令
CMD ["python", "/app/main_v3.py"]