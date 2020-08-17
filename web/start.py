#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
sys.path.insert(0, "/usr/lib/iphakethe")
from Login import Login
from Page import Page

html = Page()
login = Login()

html.set_content_type("text/html")
content_type = html.get_content_type()

print(content_type)

def start_page():
	html.set_meta_charset("utf-8")

	page = html.get_doctype_html5()
	page += "<html lang='pt-br'>"
	page += "<head>"
	page += "	" + html.get_meta_charset()
	page += "	<title>IPHAKETHE| START</title>"
	page += "	" + html.get_bootstrap_link_css()
	page += "</head>"
	page += "<body>"
	page += "	<div class='row'>"
	page += "		<div class='col'"
	page += "			<section>"
	page += "				<header>"
	page += "					<nav class='navbar navbar-dark bg-dark text-white'>"
	page += "						<h3>"
	page += "							IPHAKETHE"
	page += "						</h3>"
	page += "						<nav>"
	page += "							<ul class='list-unstyled'>"
	page += "								<li>Tela inicial</li>"
	page += "							</ul>"
	page +=	"						</nav>"
	page += "					</nav>"
	page += "				</header>"
	page += "			</section>"
	page += "		</div>"
	page += " 	</div>"
	page += "	<section>"
	page += "		<nav>"
	page += "			<ul>"
	page += "				<li>Configuracoes</li>"
	page += "				<ul>"
	page += "					<li>Criar Usuario</li>"
	page += "					<li>Deletar usuario</li>"
	page += "					<li>Listar Usuarios</li>"
	page += "				</ul>"
	page += "			</ul>"
	page += "			<ul>"
	page += "				<li>Repositorios</li>"
	page += "				<ul>"
	page += "					<li>Criar Novo Repositorio</li>"
	page += "					<li>Listar repositorio</li>"
	page += "					<li>Apagar repositorio</li>"
	page += "				</ul>"
	page += "			</ul>"
	page += "		</nav>"
	page += "	</section>"
	page += "	<section>"
	page += "	</section>"
	page += "<footer>"
	page += "	" + html.get_jquery_link()
	page += "	" + html.get_bootstrap_link_js()
	page += "	" + html.get_popper_link()
	page += "</footer>"
	page += "</body>"
	page += "</html>"

	print(page)


valid_user = login.check_user()

if valid_user == 0:
	start_page()

elif valid_user == -1:
	print("<script>window.location.assign('index.py')</script>")

else:
	print("<h3>")
	print ("Login icorreto")
	print ("</h3>")
	print("<script>window.location.assign('http://iphakethe.elipereira.com.br/index.py?login_failed=1')</script>")

