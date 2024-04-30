# 使用官方的 Python 3 镜像作为基础镜像
FROM python:3

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到镜像的 /app 目录中
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 运行定时任务
CMD [ "python", "main.py" ]
