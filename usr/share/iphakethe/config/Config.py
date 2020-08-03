#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import configparser

class Config(object):
	def __init__(self):
		self._iphakethe_root_os = os.getenv('IPHAKETHE_ROOT_OS')
		self._iphakethe_working_dir = os.getenv('IPHAKETHE_WORKING_DIR')
		self._iphakethe_lib_dir = os.getenv('IPHAKETHE_LIB_DIR')
		self._config_file = "{0}/config/iphakethe/iphakethe.conf".format(self._iphakethe_working_dir)
		self._config = configparser.ConfigParser()
		self._config.read(self._config_file)
		self._temp_dir = "/tmp/build"
		self._sections = []  
		self._git_addr = " "
		self._git_port = 22
		self._user_git = " "
		self._repo = " "
		self._folder_package_linux_repo = " "
		self._testing = "no"
		self._branch_dev_testing = "dev"
		self._distro_repo = "distro"
		self._codename_repo = "codename"
		self._keep_old_packages = "no"
		self._package_file_control = " "
		self._temp_file_package_control = " "
		self._files_to_delete_package_deb = []
		self._package = " "
		self._version = " "
		self._architecture = " "


	def set_sections(self):
		self._sections = self._config.sections()


	def get_sections(self):
		return self._sections


	def set_temp_dir(self, temp_dir):
		self._temp_dir = temp_dir


	def get_temp_dir(self):
		return self._temp_dir


	def set_git_addr(self, section, git_addr):
		self._git_addr = self._config.get(section, git_addr)


	def get_git_addr(self):
		return self._git_addr


	def set_git_port(self, section, git_port):
		self._git_port = self._config.get(section, git_port)


	def get_git_port(self):
		return self._git_port


	def set_user_git(self, section, user_git):
		self._user_git = self._config.get(section, user_git)


	def get_user_git(self):
		return self._user_git


	def set_repo(self, section, repo):
		self._repo = self._config.get(section, repo)


	def get_repo(self):
		return self._repo


	def set_folder_package_linux_repo(self, section, folder_package_linux_repo):
		self._folder_package_linux_repo = self._config.get(section, folder_package_linux_repo)


	def get_folder_package_linux_repo(self):
		return self._folder_package_linux_repo


	def set_testing(self, section, testing):
		self._testing = self._config.get(section, testing)


	def get_testing(self):
		return self._testing


	def set_branch_dev_testing(self, section, branch_dev_testing):
		self._branch_dev_testing = self._config.get(section, branch_dev_testing)


	def get_branch_dev_testing(self):
		return self._branch_dev_testing

	def set_distro_repo(self, section, distro_repo):
		self._distro_repo = self._config.get(section, distro_repo)


	def get_distro_repo(self):
		return self._distro_repo


	def set_codename_repo(self, section, codename_repo):
		self._codename_repo = self._config.get(section, codename_repo)


	def get_codename_repo(self):
		return self._codename_repo


	def set_keep_old_packages(self, section, keep_old_packages):
		self._keep_old_packages = self._config.get(section, keep_old_packages)


	def get_keep_old_packages(self):
		return self._keep_old_packages


	def set_package_file_control(self, section, package_file_control):
		self._package_file_control = self._config.get(section, package_file_control)


	def get_package_file_control(self):
		return self._package_file_control

	def set_temp_file_package_control(self, section, temp_file_package_control):
		self._temp_file_package_control = self._config.get(section, temp_file_package_control)


	def get_temp_file_package_control(self):
		return self._temp_file_package_control
			
	def set_files_to_delete_packge_deb(self, section, files_to_delete_package_deb):
		self._files_to_delete_package_deb = self._config.get(section, files_to_delete_package_deb)


	def get_files_to_delete_package_deb(self):
		return self._files_to_delete_package_deb


	def set_package(self, section, package):
		self._package = self._config.get(section, package)


	def get_package(self):
		return self._package


	def set_version(self, section, version):
		self._version = self._config.get(section, version)

	def get_version(self):
		return self._version


	def set_architecture(self, section, architecture):
		self._architecture = self._config.get(section, architecture)


	def get_architecture(self):
		return self._architecture	
