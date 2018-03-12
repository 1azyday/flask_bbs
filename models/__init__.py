
import time
import models

from bson import ObjectId
from pymongo import MongoClient
from utils import log

# Model 是一个 ORM（object relation mapper）
# 不需要关心存储数据的细节，直接使用即可
class Model():
    db = MongoClient()['web21']

    @classmethod
    def valid_names(cls):
        names = [
            # (字段名, 类型, 默认值)
            ('deleted', bool, False),
            ('ct', int, 0),
            ('ut', int, 0),
        ]
        return names

    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
        return '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))

    @classmethod
    def new(cls, form, **kwargs):
        """
        new 是给外部生成实例的函数
        """
        # 创建一个空对象
        m = cls()
        for name in cls.valid_names():
            k, t, v = name
            if k in form:
                setattr(m, k, t(form[k]))
            else:
                # 设置默认值
                setattr(m, k, v)

        # 处理额外的参数 kwargs
        for k, v in kwargs.items():
            if hasattr(m, k):
                setattr(m, k, v)
            else:
                raise KeyError

        # 写入默认数据
        timestamp = int(time.time())
        m.ct = timestamp
        m.ut = timestamp

        m.save()
        return m

    def save(self):
        name = self.__class__.__name__
        # print('save', self.__dict__)
        _id = self.db[name].save(self.__dict__)
        self.id = str(_id)

    @classmethod
    def update(cls, id, form):
        name = cls.__name__
        query = {
            '_id': ObjectId(id),
        }
        values = {
            '$set': form,
        }
        print('mongo update', query, values)
        cls.db[name].update_one(query, values)

    @classmethod
    def _new_with_bson(cls, bson):
        """
        给内部 all 这种函数使用的函数
        从 mongo 数据中恢复一个 model
        """
        m = cls()
        # print('bson', bson)
        for key in bson:
            setattr(m, key, bson[key])
        m.id = str(bson['_id'])
        return m

    @classmethod
    def all(cls, **kwargs):
        kwargs['deleted'] = False
        if 'id' in kwargs:
            kwargs['_id'] = ObjectId(kwargs['id'])
            kwargs.pop('id')
        name = cls.__name__
        docuemtns = cls.db[name].find(kwargs)
        # print('_find', kwargs, ds)
        l = [cls._new_with_bson(d) for d in docuemtns]
        return l

    @classmethod
    def one(cls, **kwargs):
        documents = cls.all(**kwargs)
        if len(documents) > 0:
            return documents[0]
        else:
            return None

    def json(self):
        d = self.__dict__
        d['id'] = d.pop('_id')
        return d

    @classmethod
    def find_all(cls, **kwargs):
        ms = []
        log('kwargs, ', kwargs, type(kwargs))
        k, v = '', ''
        for key, value in kwargs.items():
            k, v = key, value
        all = cls.all()
        for m in all:
            if v == m.__dict__[k]:
                ms.append(m)
        return ms

    @classmethod
    def find_by(cls, **kwargs):
        log('kwargs, ', kwargs, type(kwargs))
        k, v = '', ''
        for key, value in kwargs.items():
            k, v = key, value
        all = cls.all()
        for m in all:
            # 也可以用 getattr(m, k) 取值
            if v == m.__dict__[k]:
                return m
        return None

    @classmethod
    def find(cls, id):
        return cls.find_by(id=id)

    @classmethod
    def get(cls, id):
        return cls.find_by(id=id)

    @classmethod
    def delete(cls, id):
        form = {'deleted': True}
        a = cls.update(id, form)
        return cls.find_by(id=id)




