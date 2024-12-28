#!/usr/bin/env bash

pip --default-timeout=100 install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn -r /app/requirements/requirements.txt

python main_v2.py