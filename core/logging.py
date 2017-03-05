import datetime

def log_notification(msg, tool=None):
	if tool == None:
		tool = "Tool Unspecified"
	fi = open("logs/notify.log","a")
	fi.write(str(datetime.datetime.now())+":"+str(tool) + ":" + str(msg)+"\n")
	fi.close()
	return

def log_tripcode(msg, tripcode, tool=None):
	if tool == None:
		tool = "Tool Unspecified"
	fi = open("logs/notify.log","a")
	fi.write(str(datetime.datetime.now())+":"+str(tool)+":"+str(msg)+"TRIPCODE:"+tripcode+"\n")
	fi.close()
	return
