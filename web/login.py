#!/usr/bin/python3
# -*- coding: utf-8 -*-


import cgi
import configparser


class Login(object):

	def __init__(self):
		self._form = cgi.FieldStorage()
		self._username = " "
		self._password = " "
		self._user_ok = -1
		self._debug = Debug()

	def check_user(self):
		if "email" in self._form or "password" in self._form:
			self._username = self._form.getvalue("email")
			self._password = self._form.getvalue("password")

		access_config = configparser.ConfigParser()
		access_config.read("/etc/iphakethe/access.conf")
		sections = access_config.sections()

		for section in sections:
			valid_user = access_config.get(section, 'email')
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


