from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    abort,
)

from routes import (
    current_user,
    login_required,
)

from models.user import User
from models.topic import Topic
from models.board import Board
from utils import log
import uuid
import os

main = Blueprint('index', __name__)


@main.route("/login")
def login():
    u = current_user()
    return render_template("login.html", u=u)


@main.route("/register")
def register():
    u = current_user()
    return render_template("register.html", u=u)


@main.route("/register/confirm", methods=['POST'])
def register_confirm():
    form = request.form
    u = User.register(form)
    return redirect(url_for('index.login'))


@main.route("/login/confirm", methods=['POST'])
def login_confirm():
    form = request.form
    u = User.validate_login(form)
    if u is None:
        return redirect(url_for('topic.index'))
    else:
        # session 中写入 user_id
        session['user_id'] = u.id
        # 开启cookie 参数，有效期默认永久
        session.permanent = True
        return redirect(url_for('topic.index'))


@main.route("/logout/confirm", methods=['GET'])
def logout_confirm():
    session.pop('user_id')
    return redirect(url_for('topic.index'))


@main.route('/user/<id>')
def user_detail(id):
    target_u = User.find(id)
    if target_u is None:
        abort(404)
    else:
        target_u.time_difference()
        joined_topics = Topic.recent_joined(target_u.id)
        created_topics = Topic.recent_created(target_u.id)
        u = current_user()
        return render_template('profile.html', u=u, target_u=target_u, created_topics=created_topics, joined_topics=joined_topics)

def valid_suffix(suffix):
    valid_type = ['jpg', 'png', 'jpeg', 'gif']
    return suffix in valid_type

@main.route('/image/add', methods=["POST"])
@login_required
def add_img():
    # file 是一个上传的文件对象
    file = request.files['avatar']
    suffix = file.filename.split('.')[-1]
    if valid_suffix(suffix):
        # 上传的文件用 secure_filename 函数过滤一下名字
        # 防止这情况：../../../../../../../root/.ssh/authorized_keys
        # filename = secure_filename(file.filename)
        filename = '{}.{}'.format(str(uuid.uuid4()), suffix)
        file.save(os.path.join('static/user_image', filename))
        u = current_user()

        User.update(u.id, dict(
            user_image='/static/user_image/{}'.format(filename)
        ))
    return redirect(url_for("index.user_detail", id=u.id))


@main.route('/setting')
@login_required
def setting():
    user = current_user()
    return render_template('setting.html', u=user)


@main.route('/user/update', methods=["POST"])
def user_update():
    form = request.form
    if not 'old_pass' in form:
        u = current_user()
        User.update(u.id, form)
        return redirect(url_for("index.user_detail", id=u.id))
    else:
        u = current_user()
        u.edit_password(form)
        return redirect(url_for("index.user_detail", id=u.id))

@main.route('/board/setting')
def board_setting():
    bs = Board.all()
    if bs == None:
        bs = []
    else:
        pass

    return render_template('board/setting.html', bs=bs)

@main.route('/board/add', methods=["POST"])
def board_add():
    form = request.form
    Board.new(form)
    return redirect(url_for('index.board_setting'))

@main.route('/board/delete')
def board_delete():
    board_id = request.args.get('board_id')
    if board_id:
        Board.delete(board_id)
    else:
        pass
    return redirect(url_for('index.board_setting'))
