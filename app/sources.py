# app/sources.py
from app.models.linkedin import db, LinkedInAccount

def add_linkedin_account(profile_url, job_title):
    account = LinkedInAccount(profile_url=profile_url, job_title=job_title)
    db.session.add(account)
    db.session.commit()

def update_linkedin_account(account_id, profile_url=None, job_title=None):
    account = LinkedInAccount.query.get(account_id)
    if profile_url:
        account.profile_url = profile_url
    if job_title:
        account.job_title = job_title
    db.session.commit()

def remove_linkedin_account(account_id):
    account = LinkedInAccount.query.get(account_id)
    db.session.delete(account)
    db.session.commit()

def view_linkedin_accounts():
    return LinkedInAccount.query.all()
