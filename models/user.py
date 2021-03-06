from models import Model
import time
from utils import log

class User(Model):
    @classmethod
    def valid_names(cls):
        names = super().valid_names()
        names = names + [
            ('username', str, ''),
            ('password', str, ''),
            ('user_image', str, '/static/user_image/doge.gif'),
            ('signature', str, '这家伙很懒，什么也没有留下。'),
        ]
        return names

    def salted_password(self, password, salt='$!@><?>HUI&DWQa`'):
        import hashlib
        def sha256(ascii_str):
            return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()
        hash1 = sha256(password)
        hash2 = sha256(hash1 + salt)
        return hash2

    def hashed_password(self, pwd):
        import hashlib
        # 用 ascii 编码转换成 bytes 对象
        p = pwd.encode('ascii')
        s = hashlib.sha256(p)
        # 返回摘要字符串
        return s.hexdigest()

    @classmethod
    def register(cls, form):
        name = form.get('username', '')
        pwd = form.get('password', '')
        if len(name) > 2 and User.find_by(username=name) is None:
            u = User.new(form)
            u.password = u.salted_password(pwd)
            u.set_cteate_time()
            u.save()
            return u
        else:
            return None

    @classmethod
    def validate_login(cls, form):
        u = User.new(form)
        user = User.find_by(username=u.username)
        if user is not None and user.password == u.salted_password(u.password):
            return user
        else:
            return None

    @classmethod
    def set_cteate_time(self):
        self.ct = int(time.time())
        self.ut = self.ct

    def time_difference(self):
        self.td = int(time.time()) - self.ct
        return self

    def edit_password(self, form):
        if  self.password == self.salted_password(form['old_pass']):
            self.password = self.salted_password(form['new_pass'])
            self.save()
            return self
        else:
            return None