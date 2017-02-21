#!/usr/bin/env python

from subprocess import check_output

def main():
	fi = open("./REQUIREMENTS.txt", "r")
	data = fi.read()
	fi.close()

	tt= []

	output = check_output("pip freeze 2>/dev/null", shell=True).split("\n")
	for line in output:
		if len(line) != 0:
			tt.append(line.split("==")[0].lower())



	printed = False
	for line in data.split("\n"):
		if len(line) != 0 and line not in tt:
			if not printed:
				printed = True
				print "Attempting to install dependencies via pip"
			print "Installing %s" % line	
			check_output(["/usr/bin/pip","install","%s" % line,"2>/dev/null"])

	if printed:
		print "\n\n"
