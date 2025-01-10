# app/api/linkedin_routes.py
import os
import requests
from flask import Blueprint, request, redirect, url_for, session, jsonify
from app.models import db, LinkedInAccount, Transfer, Comment, Mention
from app.sources import add_linkedin_account, update_linkedin_account, remove_linkedin_account, view_linkedin_accounts
from app.transfers import view_transfers, initiate_transfer, update_transfer_status, delete_transfer
from app.comments import view_comments, add_comment, update_comment, delete_comment
from app.mentions import view_mentions, add_mention, delete_mention

linkedin_bp = Blueprint('linkedin', __name__)

LINKEDIN_AUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
LINKEDIN_TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
LINKEDIN_API_URL = "https://api.linkedin.com/v2/me"

@linkedin_bp.route('/login')
def linkedin_login():
    params = {
        'response_type': 'code',
        'client_id': os.environ.get('LINKEDIN_CLIENT_ID'),
        'redirect_uri': os.environ.get('LINKEDIN_REDIRECT_URI'),
        'scope': 'r_liteprofile r_emailaddress w_member_social'
    }
    url = f"{LINKEDIN_AUTH_URL}?{requests.compat.urlencode(params)}"
    return redirect(url)

@linkedin_bp.route('/callback')
def linkedin_callback():
    code = request.args.get('code')
    if not code:
        return 'Error: No code provided', 400

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': os.environ.get('LINKEDIN_REDIRECT_URI'),
        'client_id': os.environ.get('LINKEDIN_CLIENT_ID'),
        'client_secret': os.environ.get('LINKEDIN_CLIENT_SECRET')
    }
    response = requests.post(LINKEDIN_TOKEN_URL, data=data)
    response_data = response.json()
    access_token = response_data.get('access_token')

    if not access_token:
        return 'Error: No access token provided', 400

    session['linkedin_access_token'] = access_token
    return redirect(url_for('linkedin.profile'))

@linkedin_bp.route('/profile')
def profile():
    access_token = session.get('linkedin_access_token')
    if not access_token:
        return redirect(url_for('linkedin.linkedin_login'))

    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(LINKEDIN_API_URL, headers=headers)
    profile_data = response.json()
    return jsonify(profile_data)

@linkedin_bp.route('/accounts', methods=['GET', 'POST'])
def manage_accounts():
    if request.method == 'POST':
        data = request.json
        add_linkedin_account(data['profile_url'], data['job_title'])
        return jsonify({'message': 'Account added'}), 201
    else:
        accounts = view_linkedin_accounts()
        return jsonify([account.__dict__ for account in accounts])

@linkedin_bp.route('/accounts/<int:account_id>', methods=['PUT', 'DELETE'])
def modify_account(account_id):
    if request.method == 'PUT':
        data = request.json
        update_linkedin_account(account_id, data.get('profile_url'), data.get('job_title'))
        return jsonify({'message': 'Account updated'}), 200
    elif request.method == 'DELETE':
        remove_linkedin_account(account_id)
        return jsonify({'message': 'Account removed'}), 200

@linkedin_bp.route('/transfers', methods=['GET', 'POST'])
def manage_transfers():
    if request.method == 'POST':
        data = request.json
        initiate_transfer(data['account_id'])
        return jsonify({'message': 'Transfer initiated'}), 201
    else:
        transfers = view_transfers()
        return jsonify([transfer.__dict__ for transfer in transfers])

@linkedin_bp.route('/transfers/<int:transfer_id>', methods=['PUT', 'DELETE'])
def modify_transfer(transfer_id):
    if request.method == 'PUT':
        data = request.json
        update_transfer_status(transfer_id, data['status'])
        return jsonify({'message': 'Transfer status updated'}), 200
    elif request.method == 'DELETE':
        delete_transfer(transfer_id)
        return jsonify({'message': 'Transfer deleted'}), 200

@linkedin_bp.route('/transfers/<int:transfer_id>/comments', methods=['GET', 'POST'])
def manage_comments(transfer_id):
    if request.method == 'POST':
        data = request.json
        add_comment(transfer_id, data['content'])
        return jsonify({'message': 'Comment added'}), 201
    else:
        comments = view_comments(transfer_id)
        return jsonify([comment.__dict__ for comment in comments])

@linkedin_bp.route('/comments/<int:comment_id>', methods=['PUT', 'DELETE'])
def modify_comment(comment_id):
    if request.method == 'PUT':
        data = request.json
        update_comment(comment_id, data['content'])
        return jsonify({'message': 'Comment updated'}), 200
    elif request.method == 'DELETE':
        delete_comment(comment_id)
        return jsonify({'message': 'Comment deleted'}), 200

@linkedin_bp.route('/transfers/<int:transfer_id>/mentions', methods=['GET', 'POST'])
def manage_mentions(transfer_id):
    if request.method == 'POST':
        data = request.json
        add_mention(transfer_id, data['content'])
        return jsonify({'message': 'Mention added'}), 201
    else:
        mentions = view_mentions(transfer_id)
        return jsonify([mention.__dict__ for mention in mentions])

@linkedin_bp.route('/mentions/<int:mention_id>', methods=['DELETE'])
def delete_mention_route(mention_id):
    delete_mention(mention_id)
    return jsonify({'message': 'Mention deleted'}), 200
