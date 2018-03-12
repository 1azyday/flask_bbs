#!/usr/bin/env bash
echo 'start setup.sh'
# clone 代码到 

source_root='/var/flask_bbs'


# 换成中科大的源
# sudo ln -f -s ${source_root}/misc/sources.list /etc/apt/sources.list
# sudo mkdir -p /var/.pip
# sudo ln -f -s ${source_root}/misc/pip.conf /var/.pip/pip.conf

# 装依赖
# sudo apt-get update
sudo apt-get install -y git python3 python3-pip
# 尝试修复问题依赖
# sudo apt-get -f install 
sudo apt-get install -y nginx mongodb supervisor redis-server


sudo pip3 install -U pip setuptools wheel
sudo pip3 install jinja2 flask gunicorn pymongo gevent redis

echo 'succsss'
echo 'ip'
hostname -I