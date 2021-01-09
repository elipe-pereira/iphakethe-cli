#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import cgi
from urllib.parse import parse_qs
from web.template import Template
from web.login import Login

class Web(object):
    def __init__(self, environ):
        self.__response_headers = [('content-type', 'text/html')]
        self.__environ = environ
        self.__path = self.__environ['PATH_INFO']
        self.__page_file = Template()
        self.__login = ""
        self.__authenticated = False

    def get_reponse_headers(self):
        return self.__response_headers


    def get_page(self):
        title = "Página de Login"
        bootstrap_reboot_css = "web/assets/bootstrap/css/bootstrap-reboot.min.css"
        bootstrap_css = "web/assets/bootstrap/css/bootstrap.min.css"
        bootstrap_grid_css = "web/assets/bootstrap/css/bootstrap-grid.min.css"
        bootstrap_script_js = "web/assets/bootstrap/js/bootstrap.min.js"
        hanokh_css = "web/assets/hanokh/style.css"
        itens = self.__environ.items()
        server = ""
        url_reboot = ""
        url_css = ""

        # Ambiente de produção via proxy reverso
        try:
            server = self.__environ['HTTP_X_FORWARDED_SERVER']
            url_reboot = "https://" + server + "/assets/css/reboot"
            url_css = "https://" + server + "/assets/css"
        except:
            # ambiente de desenvolvimento via gunicorn
            server = self.__environ['HTTP_HOST']
            url_reboot = "http://" + server + "/assets/css/reboot"
            url_css = "http://" + server + "/assets/css"


        if self.__path == "/":
            page = self.__page_file.read_file('web/templates/login.html')

            return page.format(title, url_reboot, url_css)

        elif self.__path == "/teste":
            return str(itens)

        elif self.__path == "/assets/css/reboot":
            self.__response_headers = [('content-type', 'text/css')]
            page = self.__page_file.read_file(bootstrap_reboot_css)

            return page

        elif self.__path == "/assets/css":
            page = self.__page_file.read_file(bootstrap_css)
            self.__response_headers = [('content-type', 'text/css')]

            return page

        elif self.__path == "/assets/css/bootstrap-reboot.min.css.map":
            page = self.__page_file.read_file("web/assets/bootstrap/css/bootstrap-reboot.min.css.map")
            self.__response_headers = [('content-type', 'text/css')]

            return page

        elif self.__path == "/assets/bootstrap.min.css.map":
            page = self.__page_file.read_file("web/assets/bootstrap/css/bootstrap.min.css.map")
            self.__response_headers = [('content-type', 'text/css')]

            return page

        elif self.__path == "/start":
            request_body = self.__environ['wsgi.input'].read()
            post_values = parse_qs(request_body)
            username = post_values[b'usuario'][0].decode('utf-8')
            password = post_values[b'senha'][0].decode('utf-8')

            self.__login = Login(username, password)
            self.__login = self.__login.check_user()

            if self.__login == 0:
                self.__path = "/start"
                self.__authenticated = True

            if not self.__authenticated:
                return "<html><body>Nao autenticado</body></html>"

            else:
                page = self.__page_file.read_file('web/templates/start.html')
                title = "Página inicial"

                return page.format(title, url_reboot, url_css)
