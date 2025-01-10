# app/mentions.py
from app.models.linkedin import db, Mention

def view_mentions(transfer_id):
    return Mention.query.filter_by(transfer_id=transfer_id).all()

def add_mention(transfer_id, content):
    mention = Mention(transfer_id=transfer_id, content=content)
    db.session.add(mention)
    db.session.commit()

def delete_mention(mention_id):
    mention = Mention.query.get(mention_id)
    db.session.delete(mention)
    db.session.commit()
