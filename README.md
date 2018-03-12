
## flask_bbs基于Flask框架的Web论坛
* Flask框架，MVC架构，使用Flask内置的Jinja引擎渲染模板。
* 数据使用MongoDB存储，实现ORM。部分临时数据（token），使用Redis存储，提高效率。
* 实现论坛基本功能（注册登录、头像签名、发帖回复、用户信息等功能）
* 发帖、回复支持Markdwon格式，可帖子板块进行筛选分类。
* 实现权限控制：编辑、删除仅该用户可操作；发帖回复、用户设置等功能要求用户登录。
* 用户信息查看该用户发帖、回复情况。
* 注意用户安全，用户密码加盐hash再进行存储。
* CSRF和CSS攻防。对于CSRF攻击，定义随机token藏于页面一并提交，服务器依据token判断是否是实际请求。
对于XSS攻击，后端对用户提交的内容和文件进行安全转义再存储。
* vagrant配合visualbox，保持开发环境、测试环境与部署环境的一致性，实现Shell脚本一键部署。
* Gunicorn启动应用，实现负载均衡；supervisor监视应用运行情况；Nginx反向代理，处理静态文件请求。


## 用户功能演示

### 注册登录

![image](https://github.com/1azyday/flask_bbs/blob/master/README/user/%E7%99%BB%E5%BD%95%E6%B3%A8%E5%86%8C.gif)

### 退出登录

![image](https://github.com/1azyday/flask_bbs/blob/master/README/user/%E9%80%80%E5%87%BA.gif)

### 用户头像

![image](https://github.com/1azyday/flask_bbs/blob/master/README/user/%E5%A4%B4%E5%83%8F.gif)

### 用户签名

![image](https://github.com/1azyday/flask_bbs/blob/master/README/user/%E7%AD%BE%E5%90%8D.gif)

### 修改密码

![image](https://github.com/1azyday/flask_bbs/blob/master/README/user/%E4%BF%AE%E6%94%B9%E5%AF%86%E7%A0%81.gif)

## 论坛功能演示

### 发帖

![image](https://github.com/1azyday/flask_bbs/blob/master/README/topic/%E5%8F%91%E8%B4%B4.gif)

### 回复

![image](https://github.com/1azyday/flask_bbs/blob/master/README/topic/%E5%9B%9E%E5%A4%8D.gif)

### 删帖

![image](https://github.com/1azyday/flask_bbs/blob/master/README/topic/%E5%88%A0%E5%B8%96.gif)

### 版面选择

![image](https://github.com/1azyday/flask_bbs/blob/master/README/topic/%E7%89%88%E9%9D%A2.gif)

### 发帖、回复情况

![image](https://github.com/1azyday/flask_bbs/blob/master/README/topic/%E7%94%A8%E6%88%B7%E5%8F%91%E8%B4%B4.gif)
