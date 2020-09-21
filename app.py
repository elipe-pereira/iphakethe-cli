#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from web.index import web


def app(environ, start_response):
	data = web()
	status = '200 OK'
	# response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(data)))]
	response_headers = [('Content-Type', 'text/html')]
	start_response(status, response_headers)
	# return iter([data])
	return [bytes(data, 'utf-8')]
