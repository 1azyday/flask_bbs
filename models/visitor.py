from models.user import User
import time
from utils import log

class Visitor():
    __instance = None

    def __init__(self):
        self.id = '0'
        self.username = '游客'
        self.user_image = '/static/user_image/doge.gif'
        self.signature = '游客，您好！以游客身份可以浏览、发帖或回复！'

    @staticmethod
    def singleton():
        if Visitor.__instance:
            return Visitor.__instance
        else:
            Visitor.__instance = Visitor()
            return Visitor.__instance
