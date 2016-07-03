import datetime

def log_notification(msg):
	fi = open("logs/notify.log","a")
	fi.write(str(datetime.datetime.now())+":"+str(msg)+"\n")
	fi.close()
	return

def log_tripcode(msg, tripcode):
	fi = open("logs/notify.log","a")
	fi.write(str(datetime.datetime.now())+":"+str(msg)+"TRIPCODE:"+tripcode+"\n")
	fi.close()
	return
