#!/usr/bin/python3
# -*- coding: utf-8 -*-

from web.web import Web


def app(environ, start_response):
	web = Web(environ)

	data = web.get_page()

	status = '200 OK'

	response_headers = web.get_reponse_headers()
	start_response(status, response_headers)
	return [bytes(data, 'utf-8')]
