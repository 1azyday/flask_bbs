from flask import Flask
from routes.index import main as index_routes
from routes.topic import main as topic_routes
from routes.reply import main as reply_routes
import config

def configured_app():
    app = Flask(__name__)
    # 设置 secret_key 来使用 flask 自带的 session
    # 字符串随意设置，但需要保密
    app.secret_key = config.secret_key

    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    # 注册蓝图
    # 用 url_prefix 可以用来给蓝图中的每个路由加一个前缀
    app.register_blueprint(index_routes)
    app.register_blueprint(topic_routes, url_prefix='/topic')
    app.register_blueprint(reply_routes, url_prefix='/reply')
    return app



# 运行代码
if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    # 自动 reload jinja
    app = configured_app()
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )

    app.run(**config)
