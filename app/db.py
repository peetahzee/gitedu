from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import constants

def get_db():
	# an Engine, which the Session will use for connection
	# resources
	engine = create_engine(constants.DB_URL)

	# create a configured "Session" class
	session = sessionmaker(bind=engine)

	# create a Session
	return session()
