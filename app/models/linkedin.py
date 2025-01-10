# app/models/linkedin.py
from .db import db

class LinkedInAccount(db.Model):
    __tablename__ = 'linkedin_accounts'

    id = db.Column(db.Integer, primary_key=True)
    profile_url = db.Column(db.String, nullable=False)
    job_title = db.Column(db.String, nullable=False)

    transfers = db.relationship('Transfer', back_populates='account', cascade='all, delete-orphan')

class Transfer(db.Model):
    __tablename__ = 'transfers'

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('linkedin_accounts.id'), nullable=False)
    status = db.Column(db.String, nullable=False)

    account = db.relationship('LinkedInAccount', back_populates='transfers')
    comments = db.relationship('Comment', back_populates='transfer', cascade='all, delete-orphan')
    mentions = db.relationship('Mention', back_populates='transfer', cascade='all, delete-orphan')

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    transfer_id = db.Column(db.Integer, db.ForeignKey('transfers.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    transfer = db.relationship('Transfer', back_populates='comments')

class Mention(db.Model):
    __tablename__ = 'mentions'

    id = db.Column(db.Integer, primary_key=True)
    transfer_id = db.Column(db.Integer, db.ForeignKey('transfers.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    transfer = db.relationship('Transfer', back_populates='mentions')

LinkedInAccount.transfers = db.relationship('Transfer', order_by=Transfer.id, back_populates='account')
Transfer.comments = db.relationship('Comment', order_by=Comment.id, back_populates='transfer')
Transfer.mentions = db.relationship('Mention', order_by=Mention.id, back_populates='transfer')
