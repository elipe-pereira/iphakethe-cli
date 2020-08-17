#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi
import cgitb
sys.path.insert(0, "/usr/lib/iphakethe")
import functions
from Page import Page
from Login import Login
from Debug import Debug

html = Page()
login = Login()
debug = Debug()

html.set_content_type("text/html")
html.set_doctype_html5()
html.set_title("IPHAKETHE | Tela de Login")
html.set_meta_charset("utf-8")

print (html.get_content_type())

page = html.get_doctype_html5()
page += "<html lang='pt-br'>"
page += "<head>"
page += "	" + html.get_meta_charset()
page += "	<title>"
page += "		" + html.get_title()
page += "	</title>"
page += "	" + html.get_bootstrap_link_css()
page += "</head>"
page += "<body class='containter containter-sm containter-md containter-lg'>"
page += "<section>"
page += "	<div class='row'>"
page += "		<div class='col'>"
page += "		<header>"
page += "			<nav class='navbar navbar-dark bg-dark text-white'>"
page += "				<h3>"
page += "					IPHAKETHE"
page += "				</h3>"
page += "				<nav>"
page += "					<ul class='list-unstyled'>"
page += "						<li>TELA DE LOGIN</li>"
page += "					</ul>"
page += "				</nav>"
page += "			</nav>"
page += "		</header>"
page += "		</div>"
page += "	</div>"
page += "</section>"
page += "<section>"
page += "<div class='row m-0'>"
page += "	<div class='col-3'>"
page += "	</div>"
page += "	<div class='col-6 mt-5'>"

form = cgi.FieldStorage()
login_failed = form.getvalue('login_failed')

valid_user = " "

if login_failed == "1":
	valid_user = 1

else:
	valid_user = login.check_user()

if valid_user == -1:
	page += "<div class='h3'>"
	page += "	Login"
	page += "</div>"
	
else:
	if valid_user == 1:
		page += "<div class='alert alert-danger'>"
		page += "	Login failed"
		page += "</div>"

page += "		<form action='start.py' method='POST'>"
page += "			<div class='form-group'>"
page += "				<label for='email'>"
page += "					E-mail"
page += "				</label>"
page += "				<input class='form-control' type='email' id='email' name='email'>"
page += "			</div>"
page += "			<div class='form-group'>"
page += "				<label for='password'>"
page += "					Password"
page += "				</label>"
page += "				<input class='form-control' type='password' id='password' name='password'>"
page += "			</div>"
page += "			<input class='btn btn-primary' type='submit' value='Enviar'>"
page += "		</form>"
page += "	</div>"
page += "	<div class='col-3'>"
page += "	</div>"
page += "</div>"
page += "</section>"
page += "<section>"
page += "	<div class='row'>"
page += "		<div class='col'>"
page += "			<footer class='fixed-bottom text-white bg-dark p-5'>"
page += " 				Desenvolvido por Eli F. Pereira"
page += "			</footer>"
page += "		</div>"
page += "	</div>"
page += "  " + html.get_jquery_link()
page += "  " + html.get_bootstrap_link_js()
page += "  " + html.get_popper_link()
page += "</section>"
page += "</body>"
page += "</html>"

print(page)
