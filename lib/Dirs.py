#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os


class Dirs(object):
	@staticmethod
	def check_dir(directory):
		if os.path.isdir(directory):
			return True
		else:
			return False

	@staticmethod
	def check_dir_and_create(directory):
		if not Dirs.check_dir(directory):
			os.mkdir(directory, 0o0770)
			return True
		else:
			return False

	def check_dir_and_create_and_go_to(self, directory):
		self.check_dir_and_create(directory)
		os.chdir(directory)
		return True

	@staticmethod
	def set_permission(permission, folder):
		os.system("chmod -R {0} {1}".format(permission, folder))

	@staticmethod
	def create_recursive_dirs(path):
		os.makedirs(path)
