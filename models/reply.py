import time
from models import Model
from models.user import User


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
        u = User.find(self.user_id)
        return u
