import subprocess
import os

class bootstrap:
	
	def __init__(self, force=False):
		#self._install_requirements(force)

	def _install_requirements(self, force=False):
		if not os.path.isfile("conf/.installed_requiements") or force:
			subprocess.check_output("pip install -r REQUIREMENTS.txt", shell=True)
			subprocess.check_output("touch conf/.installed_requirements", shell=True)
