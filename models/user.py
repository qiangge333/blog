import hashlib
import os

from . import ModelMixin
from . import db
from . import timestamp


class User(db.Model, ModelMixin):
    # 类的属性就是数据库表的字段
    # 这些都是内置的 __tablename__ 是表名
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text())
    password = db.Column(db.Text())
    created_time = db.Column(db.Text(), default=timestamp())

    blogs = db.relationship('Blog', backref='user')

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')

    def valid_username(self):
        return User.query.filter_by(username=self.username).first() == None

    # 验证注册用户的合法性
    def validate_register(self):
        valid_username = self.valid_username()
        valid_username_len = len(self.username) >= 2
        valid_password_len = len(self.password) >= 2
        msgs = []
        if not valid_username:
            message = '用户名已经存在'
            msgs.append(message)
        if not valid_username_len:
            message = '用户名长度必须大于等于 2'
            msgs.append(message)
        if not valid_password_len:
            message = '密码长度必须大于等于 2'
            msgs.append(message)
        status = valid_username and valid_username_len and valid_password_len
        return status, msgs

    def validate_login(self, form):
        username = form.get('username', '')
        password = form.get('password', '')
        username_equals = self.username == username
        password_equals = self.password == password
        return username_equals and password_equals
