# app/search.py
from app.models.linkedin import Transfer

def search_transfers(query, filters=None):
    transfers = Transfer.query.filter(Transfer.content.contains(query))
    if filters:
        for key, value in filters.items():
            transfers = transfers.filter(getattr(Transfer, key) == value)
    return transfers.all()
