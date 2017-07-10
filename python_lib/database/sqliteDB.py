from sqlite3 import dbapi2 as sqlite3
import os

def hello_db():
	print "hello database!"

class sqlite3DB(object):
	def __init__(self, db_path, db_name):
		self.name = db_name
		self.path = os.path.join(db_path, db_name)
	def is_valid_user(self, username, password):
		if username == 'patricia' and password == 'xiao':
			error = False
			user_info = {
				"name": username,
			}
		else:
			error = True
			user_info = {}
		return error, user_info