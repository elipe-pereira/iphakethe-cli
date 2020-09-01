#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os


class Dirs(object):
	def __init__(self):
		self._value = " "

	def check_dir(self, directory):
		if os.path.isdir(directory):
			return True
		else:
			return False

	def check_dir_and_create(self, directory):
		if not self.check_dir(directory):
			os.mkdir(directory, 0o0770)
			return True
		else:
			return False

	def check_dir_and_create_and_go_to(self, directory):
		self.check_dir_and_create(directory)
		os.chdir(directory)
		return True

	def set_permission(self, permission, folder):
		os.system("chmod -R {0} {1}".format(permission, folder))

	def create_recursive_dirs(self, path):
		os.makedirs(path)
