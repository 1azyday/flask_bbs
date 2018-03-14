from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *

from models.reply import Reply
from models.visitor import Visitor

main = Blueprint('reply', __name__)


@main.route("/add", methods=["POST"])
@csrf_token_required
def add():
    form = request.form
    u = current_user()
    if u is None:
        u = Visitor.singleton()
    t = Reply.new(form, user_id=u.id)
    return redirect(url_for('topic.detail', id=t.topic_id))

