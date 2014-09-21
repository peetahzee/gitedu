from sqlalchemy import Column, Integer, String, DateTime, Sequence, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime

import constants

base = declarative_base()

class User(base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    email = Column(String)
    username = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return "<User(id='%s', email='%s')>" % (self.id, self.email)


class Org(base):
    __tablename__ = 'orgs'
    id = Column(Integer, Sequence('org_id_seq'), primary_key=True)
    name = Column(String)
    owner = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return "<Org(id='%s', name='%s')>" % (self.id, self.name)

def create_all():
    tables = [User, Org]

    for table in tables:
        print "Creating metadata for " + table.__name__
        engine = create_engine(constants.DB_URL)
        table.metadata.create_all(engine)
