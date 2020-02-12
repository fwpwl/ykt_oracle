# 从仓库拉取 带有 python 3.7 的 Linux 环境
FROM python:3.7

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1
ENV DEPLOY_DIR /ykt_proxy

# 用aliyun的源替换原有的源
COPY ["sources.list","/etc/apt/sources.list"]

RUN apt-get update \
    && mkdir -p ~/.pip \
    && echo "[global]" >  ~/.pip/pip.conf \
    && echo "timeout = 6000" >> ~/.pip/pip.conf \
    && echo "index-url = http://mirrors.aliyun.com/pypi/simple/\ntrusted-host = mirrors.aliyun.com" >> ~/.pip/pip.conf \
    && echo "[install]" >> ~/.pip/pip.conf \
    && echo "use-mirrors = true" >> ~/.pip/pip.conf \
    && echo "mirrors = http://mirrors.aliyun.com/pypi/simple/" >> ~/.pip/pip.conf \
    && echo "trusted-host = mirrors.aliyun.com" >>  ~/.pip/pip.conf


# 创建 code 文件夹并将其设置为工作目录
RUN mkdir /code
WORKDIR /code
# 更新 pip
RUN pip install pip -U
# 将 requirements.txt 复制到容器的 code 目录
ADD requirements.txt /code/
# 安装库
RUN pip install -r requirements.txt

RUN wget http://sx.ykt.io/oracle-instantclient18.3-sqlplus-18.3.0.0.0-1.x86_64.rpm \
    && wget http://sx.ykt.io/oracle-instantclient18.3-basic-18.3.0.0.0-1.x86_64.rpm \
    && rpm -ivh oracle-instantclient18.3-basic-18.3.0.0.0-1.x86_64.rpm \
    && rpm -ivh oracle-instantclient18.3-sqlplus-18.3.0.0.0-1.x86_64.rpm
    && sh -c "echo /usr/lib/oracle/18.3/client64/lib > /etc/ld.so.conf.d/oracle-instantclient.conf";sudo ldconfig \
    && echo 'export NLS_LANG="AMERICAN_AMERICA.UTF8"'>>/etc/profile \
    && source /etc/profile

# 将当前目录复制到容器的 code 目录
ADD . /code/