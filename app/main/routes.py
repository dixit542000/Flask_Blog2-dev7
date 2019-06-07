from flask import render_template, request, Blueprint
from app.models import Post
from app.posts.forms import AddCommentForm
from app import db

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    str = "select * from Comment order by path + 0 asc"
    comments = (db.session.execute(str).fetchall())
    return render_template('home.html', posts=posts, comments=comments, form=AddCommentForm())

@main.route('/about')
def about():
    return render_template('about.html',title='About')

