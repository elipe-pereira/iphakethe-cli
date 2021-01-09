#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Template(object):
	def __init__(self):
		self._content_type = " "
		self._doctype = " "
		self._title = " "
		self._charset = " "

	def read_file(self, file):
		file = open(file, 'r')
		page = ""

		for html in file.readlines():
			page = page + html

		file.close()

		return page
