# app/seeds/linkedin_data.py
from app.models import db, LinkedInAccount, Transfer, Comment, Mention, environment, SCHEMA
from sqlalchemy.sql import text

def seed_linkedin_data():
    # Seed LinkedIn accounts
    account1 = LinkedInAccount(profile_url='https://www.linkedin.com/in/johndoe', job_title='Software Engineer')
    account2 = LinkedInAccount(profile_url='https://www.linkedin.com/in/janedoe', job_title='Data Scientist')
    account3 = LinkedInAccount(profile_url='https://www.linkedin.com/in/alicesmith', job_title='Product Manager')

    db.session.add(account1)
    db.session.add(account2)
    db.session.add(account3)
    db.session.commit()

    # Seed Transfers
    transfer1 = Transfer(account_id=account1.id, status='completed')
    transfer2 = Transfer(account_id=account2.id, status='in_progress')
    transfer3 = Transfer(account_id=account3.id, status='failed')

    db.session.add(transfer1)
    db.session.add(transfer2)
    db.session.add(transfer3)
    db.session.commit()

    # Seed Comments
    comment1 = Comment(transfer_id=transfer1.id, content='This is a comment on transfer 1.')
    comment2 = Comment(transfer_id=transfer2.id, content='This is a comment on transfer 2.')
    comment3 = Comment(transfer_id=transfer3.id, content='This is a comment on transfer 3.')

    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)
    db.session.commit()

    # Seed Mentions
    mention1 = Mention(transfer_id=transfer1.id, content='This is a mention in transfer 1.')
    mention2 = Mention(transfer_id=transfer2.id, content='This is a mention in transfer 2.')
    mention3 = Mention(transfer_id=transfer3.id, content='This is a mention in transfer 3.')

    db.session.add(mention1)
    db.session.add(mention2)
    db.session.add(mention3)
    db.session.commit()

def undo_linkedin_data():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.linkedin_accounts RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.transfers RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.mentions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM linkedin_accounts"))
        db.session.execute(text("DELETE FROM transfers"))
        db.session.execute(text("DELETE FROM comments"))
        db.session.execute(text("DELETE FROM mentions"))

    db.session.commit()
