# -*- coding: utf-8 -*-
import datetime

import os
from fabric.api import *
from fabric.context_managers import *
from config.default import FullConfig
from fabric.colors import green, blue


def write_log(msg):
    with open(FullConfig.UPLOAD_LOG, "a") as log_file:
        log_file.write('%s: %s\n' % (datetime.datetime.now().isoformat(), msg))

@task
def put_task(src_file_path, des_file_path):
    path, file = os.path.split(des_file_path)
    run("mkdir -p %s" % path)
    with cd(path):
        with settings(warn_only=True):
            write_log("%s upload Start" % file)
            try:
                result = put(src_file_path, des_file_path)
            except Exception as e:
                write_log("%s upload Fail\n ------error_msg=%s" % (file, str(e)))
                return False
        if result.failed:
            write_log("%s upload Fail" % file)
            return False
        else:
            write_log("%s upload OK" % file)
            return True

# 校对文件
@task
def check_task(src_file_path, des_file_path):
    with settings(warn_only=True):
        try:
            lmd5 = local("md5sum %s" % src_file_path, capture=True).split(' ')[0]
            rmd5 = run("md5sum %s" % des_file_path).split(' ')[0]
        except Exception as e:
            write_log("%s md5 Fail\n ------error_msg=%s" % (os.path.split(src_file_path)[1], str(e)))
            return False
    if lmd5 == rmd5:
        write_log("%s md5 OK" % os.path.split(src_file_path)[1])
    else:
        write_log("%s md5 Fail" % os.path.split(src_file_path)[1])

    # 3个功能一起实现


@task
def go(src_file_path, des_file_path):
    env.hosts = [
        'jzb@124.250.24.241:10086',
    ]
    env.password = "jzb1122"

    # tar_task()
    if put_task(src_file_path, des_file_path):
        check_task(src_file_path, des_file_path)


env.hosts = ["122.112.13.36:1715"]
env.user = "haoyuan"
env.password = "sObrZ!fIFdoIa2sfeI"


@task
def deploy():

    base_dir = "/home/haoyuan/"
    code_path = "code/utools"
    deploy_path = "deploy"

    with cd(base_dir):
        print(blue("pull code ..."))
        with cd(code_path):
            run("git pull")
            run("git checkout-index -a -f --prefix=%s/%s/" % (base_dir, deploy_path))

        with cd(deploy_path):
            try:
                run("/home/haoyuan/.virtualenvs/utools/bin/supervisorctl reload")
            except:
                run("/home/haoyuan/.virtualenvs/utools/bin/supervisord -c supervisor.conf")
        print(green("deploy ok."))
