from flask import render_template, request, Blueprint
from app.models import Post,Comment
from app.posts.forms import AddCommentForm

main = Blueprint('main', __name__)



@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    comments = Comment.query.order_by(Post.date_posted.desc())
    return render_template('home.html', posts=posts, comments=comments, form=AddCommentForm())

@main.route('/about')
def about():
    return render_template('about.html',title='About')
