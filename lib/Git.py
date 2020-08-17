#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os


class Git(object):
	def __init__(self, git_addr, git_port, git_user, git_repo):
		self._git_addr = git_addr
		self._git_port = git_port
		self._git_user = git_user
		self._git_repo = git_repo


	def clone(self):
		if self._git_port == "22":
			os.system("git clone {0}:{1}/{2}.git".format(self._git_addr, self._git_user, self._git_repo))
			
		else:
			os.system("git clone ssh://{0}:{1}/{2}/{3}.git".format(self._git_addr, self._git_port, self._git_user, self._git_repo))



	def checkout(self, branch):
		os.system("git checkout {0}".format(branch))