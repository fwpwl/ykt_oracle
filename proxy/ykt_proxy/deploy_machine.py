# -*- encoding:utf-8 -*-
"""
中间机一键部署脚本
"""
import sys

STEP_NUM = 1
MAIN_STEP_NUM = 1


########################################################################################
# 部署脚本
########################################################################################
def DeployUbuntu():
    """
    """
    print_cyan_notify_msg("注意:本脚本为Ubuntu(全系列支持)安装基础环境,脚本兼容Python3.x和Python2.x")

    ################################################################################
    # 修改阿里源
    ################################################################################
    if query_yes_no('是否需要替换阿里源(加快网速,建议替换)?'):
        print_cyan_notify_msg("替换阿里源")
        modify_ubuntu_repository()

    ################################################################################
    # 开始安装zsh等常用软件
    ################################################################################
    print_cyan_notify_msg("开始安装Zsh/Git等常用软件")
    if not is_some_software_installed('zsh --version'):
        exec_cmd_list_and_print(["apt-get -y install zsh"])

    if not is_some_software_installed('git --version'):
        exec_cmd_list_and_print(["apt-get -y install git"])

    if not is_path_exist('/root/.oh-my-zsh'):
        cmd_list = [
            "wget -P /root https://qn-sx.yuketang.cn/install_zsh.sh",
            "chmod +x /root/install_zsh.sh",
            "echo Y | sh /root/install_zsh.sh",
        ]
        exec_cmd_list_and_print(cmd_list)
    print_small_notify_msg('oh_my_zsh已经安装,命令行执行:zsh 即可使用!')

    ################################################################################
    # 安装 Docker
    ################################################################################
    print_cyan_notify_msg("安装Docker")
    if not is_some_software_installed('docker -v'):
        cmd_list = [
            # 官方的源很慢，使用阿里的:
            "sudo apt-get -y remove docker docker-engine docker-ce docker.io",
            "sudo apt-get update",

            # 2. apt-get 可以使用https库
            "sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common",

            # 3. 添加docker的使用的公钥
            "curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -",

            # 4. 添加docker的远程库
            'add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"',
            "apt-get update",

            # 5. 安装docker-ce
            "sudo apt-get -y  install docker-ce",

            # 6. 启动docker
            "systemctl status docker",

            # 修改镜像源地址
            "sudo mkdir -p /etc/docker",
            """echo '{"registry-mirrors": ["https://d04x00es.mirror.aliyuncs.com"]}' > /etc/docker/daemon.json""",
            "sudo systemctl daemon-reload",
            "sudo systemctl restart docker",
            ""
        ]
        exec_cmd_list_and_print(cmd_list)

    ################################################################################
    # 安装 Docker Compose
    ################################################################################
    print_cyan_notify_msg("安装 Docker Compose")
    if not is_some_software_installed('docker-compose --version'):
        cmd_list = [
            "sudo curl -L http://qn-sx.yuketang.cn/docker-compose-Linux-x86_64 -o /usr/local/bin/docker-compose",
            "sudo chmod +x /usr/local/bin/docker-compose",
            "docker-compose --version"
        ]
        exec_cmd_list_and_print(cmd_list)

    ################################################################################
    # 创建工作目录
    ################################################################################
    print_cyan_notify_msg("创建工作目录")
    if not is_path_exist('/root/ykt'):
        cmd_list = [
            "mkdir /root/ykt",
        ]
        exec_cmd_list_and_print(cmd_list)

    final_notify_msg()


def DeployCentOS():
    """
    """
    print_cyan_notify_msg("注意:本脚本为CentOS(仅支持7.x)安装基础环境,脚本兼容Python3.x和Python2.x")

    ################################################################################
    # 修改阿里源
    ################################################################################
    if not is_some_software_installed('wget --version'):
        exec_cmd_list_and_print(["yum -y install wget"])

    if query_yes_no('是否需要替换阿里源(加快网速,建议替换)?'):
        print_cyan_notify_msg("替换阿里源")
        modify_centos_repository()

    ################################################################################
    # 开始安装zsh等常用软件
    ################################################################################
    print_cyan_notify_msg("开始安装Zsh/Git等常用软件")
    if not is_some_software_installed('zsh --version'):
        exec_cmd_list_and_print(["yum -y install zsh"])

    if not is_some_software_installed('git --version'):
        exec_cmd_list_and_print(["yum -y install git"])

    if not is_path_exist('/root/.oh-my-zsh'):
        cmd_list = [
            "wget -P /root https://qn-sx.yuketang.cn/install_zsh.sh",
            "chmod +x /root/install_zsh.sh",
            "echo Y | sh /root/install_zsh.sh",
        ]
        exec_cmd_list_and_print(cmd_list)
    print_small_notify_msg('oh_my_zsh已经安装,命令行执行:zsh 即可使用!')

    ################################################################################
    # 安装 Docker
    ################################################################################
    print_cyan_notify_msg("安装Docker")
    if not is_some_software_installed('docker -v'):
        cmd_list = [
            "yum -y install docker",
            "systemctl start docker.service",
            "systemctl enable docker.service",
            "sudo mkdir -p /etc/docker",

            """echo '{"registry-mirrors": ["https://d04x00es.mirror.aliyuncs.com"]}' > /etc/docker/daemon.json""",
            "sudo systemctl daemon-reload",
            "sudo systemctl restart docker",
            ""
        ]
        exec_cmd_list_and_print(cmd_list)

    ################################################################################
    # 安装 Docker Compose
    ################################################################################
    print_cyan_notify_msg("安装 Docker Compose")
    if not is_some_software_installed('docker-compose --version'):
        cmd_list = [
            "sudo curl -L http://qn-sx.yuketang.cn/docker-compose-Linux-x86_64 -o /usr/local/bin/docker-compose",
            "sudo chmod +x /usr/local/bin/docker-compose",
            "docker-compose --version"
        ]
        exec_cmd_list_and_print(cmd_list)

    ################################################################################
    # 创建工作目录
    ################################################################################
    print_cyan_notify_msg("创建工作目录")
    if not is_path_exist('/root/ykt'):
        cmd_list = [
            "mkdir /root/ykt",
        ]
        exec_cmd_list_and_print(cmd_list)

    final_notify_msg()


########################################################################################
# 工具函数定义
########################################################################################

def final_notify_msg():
    """
    """
    msg = """
        环境部署完毕,请执行以下命令开始部署代码:

        一.项目中需要修改的地方:
            首先切到相应的分支:
            git checkout feature/oracle_type 或者
            git checkout feature/mysql_type 或者
            git checkout feature/sqlserver_type

            然后,编写相应的代码之后,根据学校开的端口号,进行如下操作:
            找到docker-compose.yml 文件中找到这一行,如:
            django:
                ...
                ports:
                  - 8080:8080
                ...

            假如学校开放的是8000端口,则在ykt_proxy项目中全局替换所有8080为8000
            然后执行:git commit -a -m "MOD:修改端口" & git push origin xxx(分支名称) 提交代码

        二.中间机需要执行:
            # 克隆代码;
            1.git clone https://github.com/xiaoyaocp/proxy.git /root/ykt

            # 工作目录;
            2.cd /root/ykt/proxy/ykt_proxy/

            # 切到相应的分支
            3.git checkout feature/oracle_type 或者
            git checkout feature/mysql_type 或者
            git checkout feature/sqlserver_type


            # 打镜像
            1.docker-compose build

            # 启动
            2.docker-compose up -d

            检查服务是否启动:
            3.curl localhost:端口号/test_server
            如:
            curl localhost:8000/test_server
        """
    print_color_notify_msg(msg, CustomColors.YELLOW)


def modify_ubuntu_repository():
    """
    """
    code_name = get_ubuntu_codename()

    file_content = """deb http://mirrors.aliyun.com/ubuntu/ {codename} main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ {codename} main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ {codename}-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ {codename}-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ {codename}-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ {codename}-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ {codename}-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ {codename}-proposed main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ {codename}-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ {codename}-backports main restricted universe multiverse""".format(
        codename=code_name)

    cmd_list = [
        "cp -ra /etc/apt/sources.list /etc/apt/sources.list.bak",
        """echo '{}' > /etc/apt/sources.list""".format(file_content),
        "sudo apt-get update",
    ]
    exec_cmd_list_and_print(cmd_list)


def modify_centos_repository():
    """
    """
    cmd_list = [
        "mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup",
        "wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo",
        "wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo",
        "yum clean all",
        "yum makecache",
    ]
    exec_cmd_list_and_print(cmd_list)


def exec_cmd_list_and_print(cmd_list):
    """
    """
    global STEP_NUM
    for cmd in cmd_list:
        print_color_str('*' * 100, CustomColors.YELLOW)
        print('{}.执行命令:{}'.format(STEP_NUM, cmd))
        code = runcommand(cmd)
        if code == 0:
            print_success_str('{}.执行结果:成功'.format(STEP_NUM))
        else:
            print_error_str('{}.执行结果:失败'.format(STEP_NUM))
        STEP_NUM += 1


def is_some_software_installed(cmd):
    """
    """
    code = runcommand(cmd)

    is_installed = False
    if code == 0:
        is_installed = True
    print(u'校验命令是否已经安装, 检查命令:{}, 是否已经安装:'.format(cmd))
    if is_installed:
        print_success_str('{}'.format(is_installed))
    else:
        print_error_str('{}'.format(is_installed))

    return is_installed


def is_path_exist(path):
    """
    """
    import os
    return os.path.exists(path)


def runcommand(cmd, get_output=False):
    """
    """
    import subprocess
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            universal_newlines=True)
    std_out, std_err = proc.communicate()
    if std_out:
        print(std_out)
    if std_err:
        print(std_err)
    # return proc.returncode, std_out, std_err
    if get_output:
        return std_out
    return proc.returncode


def get_ubuntu_codename():
    """
    """
    some_str = runcommand('lsb_release -c', get_output=True)
    return some_str.split(":")[1].strip()


class CustomColors:
    RED = "\033[1;31;40m"
    BLUE = "\033[1;34;40m"
    YELLOW = "\033[1;33;40m"
    GREEN = "\033[1;32;40m"
    NEW_BLUE = "\033[0;37;44m"
    CYAN = "\033[1;36;40m"
    PURPLE = "\033[1;35;40m"
    # 自定义颜色
    REAL_PURPLE = "\033[1;34;40m"
    CHECK_COLOR = '\33[95m'
    CYAN_MIX = '\033[1;32;44m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_color_str(some_str, color):
    """
    打印彩色字符串
    """
    if not color:
        print(some_str)
    else:
        print(color + some_str + CustomColors.ENDC)


def print_error_str(some_str):
    """
    """
    print(CustomColors.RED + some_str + CustomColors.ENDC)


def print_success_str(some_str):
    """
    """
    print(CustomColors.GREEN + some_str + CustomColors.ENDC)


def print_color_notify_msg(custom_str, color=None):
    """

    """
    print_color_str('-' * 100, color=color)
    print_color_str(custom_str, color=color)
    print_color_str('-' * 100, color=color)


def print_small_notify_msg(custom_str, color=CustomColors.CYAN):
    """

    """
    print_color_str('-' * 100, color=color)
    print_color_str(custom_str, color=color)


def print_cyan_notify_msg(custom_str):
    """

    """
    global MAIN_STEP_NUM
    print_color_notify_msg('{}.{}'.format(MAIN_STEP_NUM, custom_str), CustomColors.NEW_BLUE)
    MAIN_STEP_NUM += 1


def query_yes_no(question, default="yes"):
    """
    一个简单的脚本里面交互的函数
    用法:query_yes_no("确定吗?") 如果按yes 则函数返回值为True
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        if check_python_version() == 'new':
            choice = input().lower()
        else:
            choice = raw_input().lower()

        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


class Platform(object):
    """
    """
    Ubuntu = 'ubuntu'
    CentOS = 'centos'


def query_input(question):
    """
    一个简单的脚本里面交互的函数
    用法:query_yes_no("确定吗?") 如果按yes 则函数返回值为True
    """
    valid = {"1": Platform.Ubuntu,
             "2": Platform.CentOS,}
    prompt = " [1/2] "

    while True:
        sys.stdout.write(question + prompt)
        if check_python_version() == 'new':
            choice = input().lower()
        else:
            choice = raw_input().lower()

        if choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("请输入提示中的选项!\n")


def check_python_version():
    """
    """
    import platform
    python_version = platform.python_version()
    if int(str(python_version)[0]) == 3:
        return 'new'
    else:
        return 'old'


if __name__ == '__main__':
    platform = query_input('请选择当前版本,1:Ubuntu, 2:CentOS7.x(请确保版本大于7)')
    if platform == Platform.Ubuntu:
        DeployUbuntu()
    elif platform == Platform.CentOS:
        DeployCentOS()
    else:
        print_error_str('不支持该平台')
