from . import ModelMixin
from . import db
from . import timestamp


class Blog(db.Model, ModelMixin):
    # 类的属性就是数据库表的字段
    # 这些都是内置的 __tablename__ 是表名
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    content= db.Column(db.Text())
    created_time = db.Column(db.Text(), default=timestamp())

    comments =db.relationship('Comment', backref='blog')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
