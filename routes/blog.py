from models.blog import Blog
from models.comment import Comment
from routes import *


main = Blueprint('blog', __name__)

Model = Blog


@main.route('/blog')
def index():
    ms = Model.query.all()
    u = current_user()
    return render_template('blogs/index.html', blogs=ms, user=u)


@main.route('/blog/<int:id>')
def detail(id):
    m = Model.query.get(id)
    cs = m.comments
    u = current_user()
    return render_template('blogs/detail.html', blog=m, comments=cs, user=u)


@main.route('/blog/new')
@login_required
def new():
    u = current_user()
    return render_template('blogs/new.html', user=u)


@main.route('/blgo/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.user_id = current_user().id
    m.save()
    return redirect(url_for('blog.detail', id=m.id))


@main.route('/answer/add', methods=['POST'])
def comment_add():
    form = request.form
    Comment.new(form)
    blog_id = int(form.get('blog_id'))
    return redirect(url_for('blog.detail', id=blog_id))
