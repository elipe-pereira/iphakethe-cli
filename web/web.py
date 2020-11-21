#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

class Web(object):
    def __init__(self, environ):
        self.__response_headers = [('content-type', 'text/html')]
        self.__environ = environ
        self.__path = self.__environ['PATH_INFO']

    def get_reponse_headers(self):
        return self.__response_headers


    def get_page(self):
        title = "Página de Login"
        bootstrap_reboot_css = "web/assets/bootstrap/css/bootstrap-reboot.min.css"
        bootstrap_css = "web/assets/bootstrap/css/bootstrap.min.css"
        bootstrap_grid_css = "web/assets/bootstrap/css/bootstrap-grid.min.css"
        bootstrap_script_js = "web/assets/bootstrap/js/bootstrap.min.js"
        itens = self.__environ.items()
        server = self.__environ['HTTP_HOST']
        url_reboot = "http://" + server + "/assets/css/reboot"
        url_css = "http://" + server + "/assets/css"
        message = "Hanokh"

        if self.__path == "/":
            file = open('web/templates/login.html', 'r')
            page = ""

            for html in file.readlines():
                page = page + html

            file.close()

            page = str(page)


            return page.format(title, url_reboot, url_css)

        elif self.__path == "/teste":
            return str(itens)

        elif self.__path == "/assets/css/reboot":
            file_reboot = open(bootstrap_reboot_css, 'r')
            page_reboot = ""
            self.__response_headers = [('content-type', 'text/css')]

            for line in file_reboot.readlines():
                page_reboot += line

            # return self.__path
            return str(page_reboot)

        elif self.__path == "/assets/css":
            file_css = open(bootstrap_css, 'r')
            page_css = ""
            self.__response_headers = [('content-type', 'text/css')]

            for line in file_css.readlines():
                page_css += line

            return str(page_css)

        elif self.__path == "/assets/css/bootstrap-reboot.min.css.map":
            file = open("web/assets/bootstrap/css/bootstrap-reboot.min.css.map", 'r')
            page_map = ""
            self.__response_headers = [('content-type', 'text/css')]

            for line in file.readlines():
                page_map += line

            return str(page_map)

        elif self.__path == "/assets/bootstrap.min.css.map":
            file = open("web/assets/bootstrap/css/bootstrap.min.css.map", 'r')
            page_map = ""
            self.__response_headers = [('content-type', 'text/css')]

            for line in file.readlines():
                page_map += line

            return page_map

        elif self.__path == "/start":
            file = open('web/templates/start.html')
            page = ""
            title = "Página inicial"

            for line in file.readlines():
                page += line

            return page.format(title, url_reboot, url_css)
