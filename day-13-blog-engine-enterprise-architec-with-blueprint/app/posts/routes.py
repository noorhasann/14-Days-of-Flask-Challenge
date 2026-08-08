# app/posts/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.models import BlogPost
from app.posts.forms import PostForm

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data, 
            content=form.content.data, 
            user_id=current_user.id
        )
        db.session.add(new_post)
        db.session.commit()

        flash('Post created successfully!', 'success')
        return redirect(url_for('posts.feed'))

    return render_template('post/create_post.html', form=form)


@posts_bp.route('/feed')
def feed():
    posts = BlogPost.query.all()
    return render_template('post/feed.html', posts=posts)


@posts_bp.route('/delete_post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)

    if post.author != current_user:
        flash('Aap kisi aur ki post delete nahi kar sakte!', 'danger')
        return redirect(url_for('posts.feed'))

    db.session.delete(post)
    db.session.commit()

    flash('Post successfully delete ho gayi!', 'success')
    return redirect(url_for('posts.feed'))


# ==========================================
# RESTful API Endpoints
# ==========================================

@posts_bp.route('/api/v1/posts', methods=['GET'])
def get_all_posts_api():
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    posts_data = [post.to_dict() for post in posts]
    
    return jsonify({
        'status': 'success',
        'count': len(posts_data),
        'data': posts_data
    }), 200


@posts_bp.route('/api/v1/posts/<int:post_id>', methods=['GET'])
def get_single_post_api(post_id):
    post = BlogPost.query.get(post_id)
    
    if not post:
        return jsonify({
            'status': 'error',
            'message': f'Post with ID {post_id} not found'
        }), 404

    return jsonify({
        'status': 'success',
        'data': post.to_dict()
    }), 200