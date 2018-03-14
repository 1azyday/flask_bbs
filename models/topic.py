import time
from models import Model
from models.user import User
from models.reply import Reply
from models.board import Board
from models.visitor import Visitor

class Topic(Model):
    @classmethod
    def valid_names(cls):
        names = super().valid_names()
        names = names + [
            ['views', int, 0],
            ['title', str, ''],
            ['content', str, ''],
            ['user_id', str, ''],
            ['board_id', str, ''],
        ]
        return names

    @classmethod
    def get(cls, id):
        m = cls.find_by(id=id)
        m.views += 1
        m.save()
        return m

    def user(self):
        if self.user_id == '0':
            u = Visitor.singleton()
        else:
            u = User.find(self.user_id)
        return u

    def replies(self):
        rs = Reply.find_all(topic_id=self.id)
        return rs

    def reply_count(self):
        count = len(self.replies())
        return count

    @classmethod
    def recent_created(self, user_id):
        ts = Topic.find_all(user_id=user_id)
        for t in ts:
            t.reply_count = t.reply_count()
            t.td = int(time.time()) - t.ut
        ts = sorted(ts, key=lambda t:t.td)
        return ts

    @classmethod
    def recent_joined(self, user_id):
        rs = Reply.find_all(user_id=user_id)
        ts = []
        t_ids = []

        for r in rs:
            t = Topic.find(r.topic_id)
            if t:
                if t.id not in t_ids:
                    ts.append(t)
                    t_ids.append(t.id)
            else:
                pass

        for t in ts:
            t.reply_count = t.reply_count()
            t.td = int(time.time()) - t.ut
            
        ts = sorted(ts, key=lambda t: t.td)
        return ts

    def set_reply_count(self):
        self.reply_count = self.reply_count()
        return self

    def passed_time(self):
        return int(time.time() - self.ct)

    def board_name(self):
        b = Board.find(self.board_id)
        return b.name