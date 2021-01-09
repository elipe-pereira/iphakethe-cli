#!/usr/bin/python3
# -*- coding: utf-8 -*-

import configparser

class Login(object):

	def __init__(self, username, password):
		self._username = username
		self._password = password
		self._user_ok = -1

	def check_user(self):

		access_config = configparser.ConfigParser()
		access_config.read("config/iphakethe/access.conf")
		sections = access_config.sections()

		for section in sections:
			valid_user = access_config.get(section, 'username')
			valid_password = access_config.get(section, 'password')

			if valid_user == self._username and valid_password == self._password:
				self._user_ok = 0
				break

			elif self._username == " " and self._password == " ":
				self._user_ok = -1
				break

			else:
				self._user_ok = 1
				break

		return self._user_ok
