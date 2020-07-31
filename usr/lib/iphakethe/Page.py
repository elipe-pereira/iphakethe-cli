#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Page(object):
	def __init__(self):
		self._content_type = " "
		self._doctype = " "
		self._title = " "
		self._charset = " "

	def set_content_type(self, content_type):
		self._content_type = content_type


	def get_content_type(self):
		return "Content-type: " + self._content_type + "\n\n\n"


	def set_doctype_html5(self):
		self._doctype = "<!DOCTYPE html>"

	def get_doctype_html5(self):
		return self._doctype


	def set_title(self, title):
		self._title = title

	def get_title(self):
		return self._title

	def set_meta_charset(self, charset):
		self._charset = "<meta charset=" + charset + ">"


	def get_meta_charset(self):
		return self._charset

	def h1(self, classname, idname, text):
		print ("<h1 class={0} id={1}>{2}</h1>".format(classname, idname, text))

	
	def get_bootstrap_link_css(self):
		link = "<link rel=stylesheet type='text/css' "
		link += "href='assets/bootstrap/dist/css/bootstrap.min.css'>"
		link += "\n"
		link += "<link rel='stylesheet' type='text/css' "
		link += "href='assets/bootstrap/dist/css/bootstrap-reboot.min.css'>"
		link += "\n"
		link += "<link rel='stylesheet' type='text/css' "
		link += "href='assets/elip/elip.css'>"

		return link	


	def get_bootstrap_link_js(self):
		link = "<script src="
		link += "'assets/bootstrap/dist/js/bootstrap.bundle.min.js'></script>\n"
		link += "<script src="
		link += "'assets/bootstrap/dist/js/bootstrap.min.js'></script"

		return link


	def get_jquery_link(self):
		link = "<script src="
		link += "'assets/jquery/jquery-3.5.1.min.js'></script>"

		return link

	def get_popper_link(self):
		link = "<script src="
		link += "'assets/popper/popper.min.js'></script>"

		return link


	def body_start(self, classname, idname):
		print("<body class='{0}' id='{1}'>".format(classname, idname))


	def body_end(self):
		print("</body>")


	def header_start(self, classname, idname):
		print("<header class='{0}' id='{1}'>".format(classname, idname))


	def header_end(self):
		print("</header>")


	def nav(self, classname, idname):
		print("<nav class='{0}' id={1}>".format(classname, idname))


	def nav_end(self):
		print("</nav>")


	def ol(self, classname, idname):
		print("<ol class='{0}' id='{1}'>".format(classname, idname))


	def ol_end(self):
		print("</ol>")


	def ul(self, classname, idname):
		print("<ul class='{0}' id='{1}'>".format(classname, idname))


	def ul_end(self):
		print("</ul>")


	def li(self, classname, idname, text):
		print("<li class='{0}' id='{1}'>{2}".format(classname, idname, text))


	def li_end(self):
		print("</li>")


	def div(self, classname, idname, text):
		print("<div class='{0}' id='{1}'>{2}".format(classname, idname, text))


	def div_end(self):
		print("</div>")


	def form(self, action, method):
		print("<form action='{0}' method='{1}'".format(action, method))


	def form_end(self):
		print("</form>")


	def input(self, classname, idname, type, text):
		print("<input type='{2} class='{0}' id={1}>{3}".format(classname, idname, type, text))
