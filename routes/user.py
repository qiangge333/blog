from models.user import User
from routes import *

import os


main = Blueprint('user', __name__)

Model = User


xfrs_dict = {
    'd40a58205d884331aa7f2a7304ad6345': 0,
}


def random_string():
    import uuid
    return str(uuid.uuid4())


@main.route('/')
def index():
    return render_template('users/login_views.html')


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get('username', '')
    # 检查 u 是否存在于数据库中并且 密码用户 都验证合格
    model = Model.query.filter_by(username=username).first()
    if model is not None and model.validate_auth(form):
        print('登录成功')
        session['user_id'] = model.id
        return redirect(url_for('user.index'))
    else:
        print('登录失败')
        # 蓝图中的 url_for 需要加上蓝图的名字，这里是 user
        return redirect(url_for('user.index'))


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    m = Model(form)
    # 检查 u 是否存在于数据库中并且 密码用户 都验证合格
    status, msgs = m.validate_register()
    if status:
        print('注册成功')
        m.save()
        session['user_id'] = m.id
        return redirect(url_for('blog.index'))
    else:
        print('注册失败')
        # 蓝图中的 url_for 需要加上蓝图的名字，这里是 user
        return redirect(url_for('user.index', msgs=msgs))


@main.route('/profile')
@login_required
def profile():
    m = current_user()
    lb = len(m.blogs)
    return render_template('user/user_profile.html', user=m, lb=lb)


def file_name(filename):
    count = len(os.listdir('uploads')) + 1
    name = str(count) + '.' + filename.split('.')[-1]
    print(name)
    return name
