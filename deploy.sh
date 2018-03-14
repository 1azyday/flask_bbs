sudo su

# 手动
# git clone
# cd dir
# 拉代码
#git pull

# 装依赖
#sudo apt-get install git python3 python3-pip supervisor nginx
#sudo pip3 install -U pip setuptools wheel
#pip3 install jinja2 flask gunicorn pymongo

# 删掉 nginx default 设置
sudo rm -f /etc/nginx/sites-enabled/default
sudo rm -f /etc/nginx/sites-available/default

source_root='/var/flask_bbs'

# 建立一个软连接
sudo ln -s -f ${source_root}/flask_bbs.conf /etc/supervisor/conf.d/flask_bbs.conf
# 不要再 sites-available 里面放任何东西
sudo ln -s -f ${source_root}/flask_bbs.nginx /etc/nginx/sites-enabled/flask_bbs.nginx

# 重启服务器
sudo service supervisor restart
sudo service nginx restart
sudo service mongodb start
sudo service supervisor start
sudo redis-server &

# service supervisor status
# ls /var/log/supervisor/

sudo echo 'deploy success'
