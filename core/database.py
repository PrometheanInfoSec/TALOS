#!/usr/bin/env python
import sqlite3



class essential:
	#don't chance this just yet.  We're gonna work with a centralized database until I see a compelling need for multiple workstations.
	db_file = 'assets/talos.db'

	def __init__(self):
		try:
			conn = sqlite3.connect(self.db_file)
			conn.close()
		except:
			print "Database error\nCannot connect to db file\n%s " % (self.db_file)

	def db_create_table(self, table):
		conn = sqlite3.connect(self.db_file)
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS %s" % (table))
		conn.commit()
		conn.close()
		return

	def db_exec(self, commands):
		conn = sqlite3.connect(self.db_file)
		c = conn.cursor()
		if type(commands) == list:
			for com in commands:
				c.execute(com)
		elif type(commands) == str:
			c.execute(commands)
		else:
			print "type error"
		conn.commit()	
		conn.close()
		return
