# app/transfers.py
from app.models.linkedin import db, Transfer

def view_transfers():
    return Transfer.query.all()

def initiate_transfer(account_id):
    transfer = Transfer(account_id=account_id, status='initiated')
    db.session.add(transfer)
    db.session.commit()

def update_transfer_status(transfer_id, status):
    transfer = Transfer.query.get(transfer_id)
    transfer.status = status
    db.session.commit()

def delete_transfer(transfer_id):
    transfer = Transfer.query.get(transfer_id)
    db.session.delete(transfer)
    db.session.commit()
