import time
from models import Model
from models.user import User
from models.visitor import Visitor

class Reply(Model):
    @classmethod
    def valid_names(cls):
        names = super().valid_names()
        names = names + [
            ('title', str, ''),
            ('content', str, ''),
            ('user_id', str, ''),
            ('topic_id', str, ''),
        ]
        return names


    def user(self):
        if self.user_id == '0':
            u = Visitor.singleton()
        else:
            u = User.find(self.user_id)
        return u
