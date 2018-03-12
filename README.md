
## flask_bbs基于Flask框架的Web论坛
* Flask框架，MVC架构，使用Flask内置的Jinja引擎渲染模板。
* 数据使用MongoDB存储，实现ORM。部分临时数据（token），使用Redis存储，提高效率。
* 实现论坛基本功能（注册登录、头像签名、发帖回复、用户信息等功能）
* 发帖、回复支持Markdwon格式。
* 实现权限控制：编辑、删除仅该用户可操作；发帖回复、用户设置等功能要求用户登录。
* 用户信息查看该用户发帖、回复情况。
* 注意用户安全，用户密码加盐hash再进行存储。
* CSRF和CSS攻防。对于CSRF攻击，定义随机token藏于页面一并提交，服务器依据token判断是否是实际请求。
对于XSS攻击，后端对用户提交的内容和文件进行安全转义再存储。
* vagrant配合visualbox，保持开发环境、测试环境与部署环境的一致性，实现Shell脚本一键部署。
* Gunicorn启动应用，实现负载均衡；supervisor监视应用运行情况；Nginx反向代理，处理静态文件请求。

- ### 注册与登录

    ![image](https://github.com/blinkd/Flask_blog/blob/master/readme/register.gif)

- ### 个人图像上传

    ![image](https://github.com/blinkd/Flask_blog/blob/master/readme/upload.gif)



- ### blog 发布，板块的分类
     - 博客详情页中包括**发布时间，作者，博客的板块来源，浏览次数**
     - 博客书写支持**Markdown**格式
     - 博客主页可以根据不同**板块**进行筛选分类
     - 博客主页列表包括博客**浏览数**与**评论数**

    ![image](https://github.com/blinkd/Flask_blog/blob/master/readme/blog.gif)

- ### 个人主页设置
    - 个人签名设置
    - 重置密码
    - 更新头像

    ![image](https://github.com/blinkd/Flask_blog/blob/master/readme/profile.gif)


- ### 评论与个人主页
    - 支持Markdown格式
    - 显示楼层，发布时间，个人头像连接跳转
    - 个人主页的博客与评论列表根据**时间倒序排列**显示
    ![image](https://github.com/blinkd/Flask_blog/blob/master/readme/profile.gif)
