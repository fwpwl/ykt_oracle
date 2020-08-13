# 从仓库拉取 带有 python 3.7 的 Linux 环境
FROM python:3.7

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 添加 Debian 清华镜像源
RUN echo \
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free\
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free\
    > /etc/apt/sources.list


# 添加这两行
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev -y

# 创建 code 文件夹并将其设置为工作目录
RUN mkdir /code
WORKDIR /code
# 更新 pip
RUN pip install pip -U -i https://mirrors.aliyun.com/pypi/simple/
# 将 requirements.txt 复制到容器的 code 目录
ADD requirements.txt /code/
# 安装库
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
# 将当前目录复制到容器的 code 目录

ADD . /code/

WORKDIR /code
#RUN  ls ./ && python manage.py collectstatic --no-input -v 2
RUN sh ./config/python/deploy_ubuntu.sh


COPY config/python/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]