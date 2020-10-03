#!/usr/bin/python3
# -*- coding: utf-8 -*-


def web(environ):
    title = "Página de Login"
    reboot_css = ""
    css = ""
    grid_css = ""
    script_js = ""
    itens = environ.items()
    path = environ['PATH_INFO']
    message = "Hanokh"
    img_logo = "https://static.hanokh.com.br/img/log03.png"

    if path == "/":
        file = open('web/templates/login.html', 'r')
        page = ""

        for html in file.readlines():
            page = page + html

        file.close()

        return page.format(title, reboot_css, css, grid_css, img_logo, script_js)

    elif path == "/teste":
        return "<meta charset='utf-8'>\nVocê digitou /teste"

