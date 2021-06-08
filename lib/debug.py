#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import time

class Debug(object):
	def __init__(self):
		self.message = ""
		self.time = time.strftime('%Y-%m-%d %H:%M:%S') 
		self.format = self.time + ' - %(name)s - %(levelname)s - %(message)s'

	def log(self, message):
		logging.basicConfig(format=self.format, filename='/var/log/iphakethe.log', level=logging.DEBUG)
		logger = logging.getLogger('iphakethe')
		logger.info(message)
