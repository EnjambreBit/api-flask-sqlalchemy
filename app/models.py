import uuid
import datetime

from app import app, db
from sqlalchemy_utils import UUIDType

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(UUIDType(binary=False), default=uuid.uuid4, primary_key=True)          # string, UUID representing the identifier for this commmand
    firstname = db.Column(db.String(128), unique=False)                                      # string, device id
    lastname = db.Column(db.String(256), unique=False)                                     # string, command text
    created_timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)          # number, UNIX UTC seconds when command was originally created in this system.

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return '<User uuid: "%r" firstname: "%s" lastname: "%s">' % (self.id, self.firstname, self.lastname)
