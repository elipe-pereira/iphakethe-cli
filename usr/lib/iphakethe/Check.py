#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

class Check(object):
	def __init__(self):
		self._value = " "

	
	def check_dir(self, dir):
		if os.path.isdir(dir):
			return True
		else:
			return False


	def check_dir_and_create(self, dir):
		if not self.check_dir(dir):
			os.mkdir(dir, 0o0770)
			return True
		else:
			return False


	def check_dir_and_create_and_go_to(self, dir):
		self.check_dir_and_create(dir)
		os.chdir(dir)
		return True


	def set_permission(self, permission, folder):
		os.system("chmod -R {0} {1}".format(permission, folder))
