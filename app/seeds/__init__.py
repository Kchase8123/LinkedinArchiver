from flask.cli import AppGroup
from app.seeds.users import seed_users, undo_users
from app.seeds.linkedin_data import seed_linkedin_data, undo_linkedin_data

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_linkedin_data()
    seed_users()
    seed_linkedin_data()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_linkedin_data()
    # Add other undo functions here
