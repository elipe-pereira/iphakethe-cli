#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import configparser


class Config(object):
	def __init__(self):
		self.__iphakethe_working_dir = os.getenv('IPHAKETHE_WORKING_DIR')
		self.__iphakethe_lib_dir = os.getenv('IPHAKETHE_LIB_DIR')
		self.__config_file = "{0}/config/iphakethe/iphakethe.conf".format(self.__iphakethe_working_dir)
		self.__config = configparser.ConfigParser()
		self.__config.read(self.__config_file)
		self.__temp_dir = "/tmp/build"
		self.__sections = []  
		self.__git_addr = " "
		self.__git_port = 22
		self.__user_git = " "
		self.__repo = " "
		self.__folder_package_linux_repo = " "
		self.__testing = "no"
		self.__branch_dev_testing = "dev"
		self.__distro_repo = "distro"
		self.__codename_repo = "codename"
		self.__keep_old_packages = "no"
		self.__package_file_control = " "
		self.__temp_file_package_control = " "
		self.__files_to_delete_package_deb = []
		self.__package_section = " "
		self.__package = " "
		self.__priority = " "
		self.__version = " "
		self.__architecture = " "
		self.__maintainer = " "
		self.__depends = " "
		self.__description = " "
		self.__command_pre_inst = " "
		self.__command_post_inst = " "
		self.__command_pre_rm = " "
		self.__command_post_rm = " "
		self.__so_dest_install = " "

	def set_sections(self):
		self.__sections = self.__config.sections()

	def get_sections(self):
		return self.__sections

	def set_temp_dir(self, temp_dir):
		self.__temp_dir = temp_dir

	def get_temp_dir(self):
		return self.__temp_dir

	def set_git_addr(self, section, git_addr):
		self.__git_addr = self.__config.get(section, git_addr)

	def get_git_addr(self):
		return self.__git_addr

	def set_git_port(self, section, git_port):
		self.__git_port = self.__config.get(section, git_port)

	def get_git_port(self):
		return self.__git_port

	def set_user_git(self, section, user_git):
		self.__user_git = self.__config.get(section, user_git)

	def get_user_git(self):
		return self.__user_git

	def set_repo(self, section, repo):
		self.__repo = self.__config.get(section, repo)

	def get_repo(self):
		return self.__repo

	def set_folder_package_linux_repo(self, section, folder_package_linux_repo):
		self.__folder_package_linux_repo = self.__config.get(section, folder_package_linux_repo)

	def get_folder_package_linux_repo(self):
		return self.__folder_package_linux_repo

	def set_testing(self, section, testing):
		self.__testing = self.__config.get(section, testing)

	def get_testing(self):
		return self.__testing

	def set_branch_dev_testing(self, section, branch_dev_testing):
		self.__branch_dev_testing = self.__config.get(section, branch_dev_testing)

	def get_branch_dev_testing(self):
		return self.__branch_dev_testing

	def set_distro_repo(self, section, distro_repo):
		self.__distro_repo = self.__config.get(section, distro_repo)

	def get_distro_repo(self):
		return self.__distro_repo

	def set_codename_repo(self, section, codename_repo):
		self.__codename_repo = self.__config.get(section, codename_repo)

	def get_codename_repo(self):
		return self.__codename_repo

	def set_keep_old_packages(self, section, keep_old_packages):
		self.__keep_old_packages = self.__config.get(section, keep_old_packages)

	def get_keep_old_packages(self):
		return self.__keep_old_packages

	def set_files_to_delete_packge_deb(self, section, files_to_delete_package_deb):
		self.__files_to_delete_package_deb = self.__config.get(section, files_to_delete_package_deb)

	def get_files_to_delete_package_deb(self):
		return self.__files_to_delete_package_deb

	def set_package_section(self, section, package_section ):
		self.__package_section = self.__config.get(section, package_section)

	def get_package_section(self):
		return self.__package_section

	def set_package(self, section, package):
		self.__package = self.__config.get(section, package)

	def get_package(self):
		return self.__package

	def set_priority(self, section, priority):
		self.__priority = self.__config.get(section, priority)

	def get_priority(self):
		return self.__priority

	def set_version(self, section, version):
		self.__version = self.__config.get(section, version)

	def get_version(self):
		return self.__version

	def set_architecture(self, section, architecture):
		self.__architecture = self.__config.get(section, architecture)

	def get_architecture(self):
		return self.__architecture

	def set_maintainer(self, section, maintainer):
		self.__maintainer = self.__config.get(section, maintainer)

	def get_maintainer(self):
		return self.__maintainer

	def set_depends(self, section, depends):
		self.__depends = self.__config.get(section, depends)

	def get_depends(self):
		return self.__depends

	def set_description(self, section, description):
		self.__description = self.__config.get(section, description)

	def get_description(self):
		return self.__description

	def set_command_pre_inst(self, section, command_pre_inst):
		self.__command_pre_inst = self.__config.get(section, command_pre_inst)

	def get_command_pre_inst(self):
		return self.__command_pre_inst

	def set_command_post_inst(self, section, command_post_inst):
		self.__command_post_inst = self.__config.get(section, command_post_inst)

	def get_command_post_inst(self):
		return self.__command_post_inst

	def set_command_pre_rm(self, section, command_pre_rm):
		self.__command_pre_rm = self.__config.get(section, command_pre_rm)

	def get_command_pre_rm(self):
		return self.__command_pre_rm

	def set_command_post_rm(self, section, command_post_rm):
		self.__command_post_rm = self.__config.get(section, command_post_rm)

	def get_command_post_rm(self):
		return self.__command_post_rm

	def set_so_dest_install(self, section, so_dest_install):
		self.__so_dest_install = self.__config.get(section, so_dest_install)

	def get_so_dest_install(self):
		return self.__so_dest_install
