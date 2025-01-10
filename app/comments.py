# app/comments.py
from app.models.linkedin import db, Comment

def view_comments(transfer_id):
    return Comment.query.filter_by(transfer_id=transfer_id).all()

def add_comment(transfer_id, content):
    comment = Comment(transfer_id=transfer_id, content=content)
    db.session.add(comment)
    db.session.commit()

def update_comment(comment_id, content):
    comment = Comment.query.get(comment_id)
    comment.content = content
    db.session.commit()

def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    db.session.delete(comment)
    db.session.commit()
