#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os


class Dirs(object):
	@staticmethod
	def check_dir(folder):
		if os.path.isdir(folder):
			return True
		else:
			return False

	@staticmethod
	def check_dir_and_create(folder):
		if not Dirs.check_dir(folder):
			os.mkdir(folder, 0o0770)
			return True
		else:
			return False

	def check_dir_and_create_and_go_to(self, folder):
		self.check_dir_and_create(folder)
		os.chdir(folder)
		return True

	@staticmethod
	def set_permission(permission, folder):
		os.system("chmod -R {0} {1}".format(permission, folder))

	@staticmethod
	def create_recursive_dirs(path):
		os.makedirs(path)

	def remove_dir(self, folder):
		if self.check_dir(folder):
			os.system("rm -rf {0}".format(folder))

	def create_dir(self, folder):
		if not self.check_dir(folder):
			os.makedirs(folder)
			return True
		else:
			return False

	def change_dir(self, folder):
		if self.check_dir(folder):
			os.chdir(folder)

	def rename_dir(self, folder_source, folder_dest):
		if not self.check_dir(folder_dest):
			os.rename(folder_source, folder_dest)
		else:
			print("Não é necessário renomear")
			print("Diretório já possui este nome")
