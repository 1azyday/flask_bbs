from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import (
    current_user,
    login_required,
    csrf_token_required,
    new_csrf_token,
)

from models.topic import Topic
from models.board import Board
main = Blueprint('topic', __name__)


@main.route("/")
def index():
    board_id = request.args.get('board_id')
    if board_id:
        ms = Topic.find_all(board_id =board_id)
    else:
        ms = Topic.all()

    u = current_user()
    bs = Board.all()
    return render_template("topic/index.html", ms=ms, u=u, bs=bs)


@main.route('/<id>')
def detail(id):
    t = Topic.get(id)
    u = current_user()
    token  = new_csrf_token()
    return render_template("topic/detail.html", topic=t, u=u, token=token)

@main.route("/add", methods=["POST"])
@csrf_token_required
@login_required
def add():
    form = request.form
    u = current_user()
    t = Topic.new(form, user_id=u.id)
    return redirect(url_for('.detail', id=t.id))


@main.route("/new")
@login_required
def new():
    login_required(add)
    bs = Board.all()
    token = new_csrf_token()
    return render_template("topic/new.html", bs=bs, token=token)

@main.route("/delete")
@csrf_token_required
@login_required
def delete():
    topic_id = request.args.get('topic_id')
    Topic.delete(topic_id)
    return redirect(url_for('topic.index'))