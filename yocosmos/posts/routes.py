from flask import Blueprint, render_template, url_for, flash, redirect, request
from yocosmos import db, limiter
from yocosmos.posts.forms import PostForm
from yocosmos.models import Post
from flask_limiter.util import get_remote_address
import os
import random

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=['POST'])
@limiter.limit("500/day")
@limiter.limit("50/hour")
@limiter.limit("5/minute")
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        address = get_remote_address()

        # get the directory of the current script
        script_dir = os.path.dirname(os.path.realpath(__file__))

        # create the absolute path of the avatar images directory
        avatars_dir = os.path.join(script_dir, '../static/avatars')

        # get list of avatar images
        avatar_images = os.listdir(avatars_dir)

        # randomly select an avatar
        selected_avatar = random.choice(avatar_images)

        post = Post(content=form.content.data, user_ip=address, avatar_image=selected_avatar)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been submitted!', 'success')
        return redirect(url_for('main.home'))
    return new_post_get()



@posts.route("/post/new", methods=['GET'])
def new_post_get():
    form = PostForm()
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post, likes=len(post.likers))
