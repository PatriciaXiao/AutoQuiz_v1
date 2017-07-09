from sqlite3 import dbapi2 as sqlite3
import os

def hello_db():
	print "hello database!"

class sqlite3DB(object):
	def __init__(self, db_name):
		self.name = db_name
		self.path = os.path.join(app.root_path, db_name)