from flask import (
	session,
	redirect,
    url_for,
    request,
    abort,
)

from models.user import User
from functools import wraps
import uuid
import redis

def current_user():
    uid = session.get('user_id', '')
    u = User.find_by(id=uid)
    return u

# csrf_tokens = dict()
# 改redis存储token，开启redis自动转码
r = redis.StrictRedis(charset='utf-8', decode_responses=True)

# 装饰器：权限控制
def login_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if current_user():
            return func()
        else:
            print('zxc')
            return redirect(url_for('index.login'))

    return wrap

# 装饰器：防止csrf的token判断
def csrf_token_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        token = request.args.get('token')
        u = current_user()
        """
        # dict版
        if token in csrf_tokens:

            uid = csrf_tokens.pop(token)
            if uid == u.id:
                return func(*args, **kwargs)
        """
        # redis版
        if r.exists(token) and r.get(token) == u.id:
            r.delete(token)
            return func(*args, **kwargs)
        elif u == None:
            return func(*args, **kwargs)
        else:
            return abort(401)
    return wrap

# 初始化一个token
def new_csrf_token():
    u = current_user()
    if u:
        token = str(uuid.uuid4())
        # dict版
        # csrf_tokens[token] = u.id

        # redis版
        r.set(token, u.id)
        return token
    else:
        return None