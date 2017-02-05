from . import ModelMixin
from . import db
from . import timestamp


class Comment(db.Model, ModelMixin):
    # 类的属性就是数据库表的字段
    # 这些都是内置的 __tablename__ 是表名
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text,)
    content= db.Column(db.Text)
    created_time = db.Column(db.Text(), default=timestamp())

    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def __init__(self, form):
        self.username = form.get('username', '匿名用户')
        self.content = form.get('content', '')
        self.blog_id = int(form.get('blog_id'))
