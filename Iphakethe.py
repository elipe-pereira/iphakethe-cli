#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import configparser
from config.Config import Config
from lib.Check import Check
from lib.Git import Git
from lib.Debug import Debug
import lib.functions


class Iphakethe(object):
	def __init__(self):
		self._temp_dir = ""
		self._git_addr = ""
		self._git_port = ""
		self._user_git = ""
		self._repo = ""
		self._folder_package_linux_repo = ""
		self._testing = ""
		self._branch_dev_testing = ""
		self._distro_repo = ""
		self._codename_repo = ""
		self._keep_old_packages = ""
		self.config = Config()
		self.check = Check()
		self.debug = Debug()

	def pack(self):
		config = Config()
		check = Check()
		debug = Debug()

		config.set_sections()

		sections = config.get_sections()

		for section in sections:
			self.config.set_temp_dir("/tmp/build")
			self.config.set_git_addr(section, 'git_addr')
			self.config.set_git_port(section, 'git_port')
			self.config.set_user_git(section, 'user_git')
			self.config.set_repo(section, 'repo')
			self.config.set_folder_package_linux_repo(section, 'folder_package_linux_repo')
			self.config.set_testing(section , 'testing')
			self.config.set_branch_dev_testing(section, 'branch_dev_testing')
			self.config.set_distro_repo(section, 'distro_repo')
			self.config.set_codename_repo(section, 'codename_repo')
			self.config.set_keep_old_packages(section, 'keep_old_packages')
			
			self._temp_dir = self.config.get_temp_dir()
			self._git_addr = self.config.get_git_addr()
			self._user_git = self.config.get_user_git()
			self._git_port = self.config.get_git_port()
			self._repo = self.config.get_repo()
			self._folder_package_linux_repo = self.config.get_folder_package_linux_repo()
			self._testing = self.config.get_testing()
			self._branch_dev_testing = self.config.get_branch_dev_testing()
			self._distro_repo = self.config.get_distro_repo()
			self._codename_repo = self.config.get_codename_repo()
			self._keep_old_packages = self.config.get_keep_old_packages()

			self.check.check_dir_and_create_and_go_to(self._temp_dir)

			git = Git(self._git_addr, self._git_port, self._user_git, self._repo)
			git.clone()

			if self._testing == "yes":
				os.chdir("{0}/{1}".format(temp_dir, repo))
				git.checkout(branch_dev_testing)

			folder = "{0}/{1}".format(self._temp_dir, self._repo)

			self.check.set_permission('0755', folder)

			package_file_control = open("{0}/{1}/DEBIAN/control".format(self._temp_dir, self._repo))
			temp_file_package_control = open("{0}/FILE_TEMP_PACKAGE".format(self._temp_dir), "w+")

			temp_file_package_control.write("[PACKAGE]\n")
	        
			for line in package_file_control:
				temp_file_package_control.write(line)

			temp_file_package_control.close()
			package_file_control.close()

			files_to_delete_package_deb = [".git", "readme.md", "README.md",
	       	                               "Jenkinsfile", ".gitignore"]

			for file in files_to_delete_package_deb:
				os.system("rm -rf /tmp/build/{0}/{1}".format(self._repo, file))

			os.system("dpkg -b {0}/{1} {0}".format(self._temp_dir, self._repo))

			package = configparser.ConfigParser()
			package.read("{0}/FILE_TEMP_PACKAGE".format(self._temp_dir))

			version = package.get('PACKAGE', 'Version')
			architecture = package.get('PACKAGE', 'Architecture')

			if self._keep_old_packages == "yes":
				os.system("reprepro --keepunreferencedfiles -b {0}/{1} includedeb {2} {3}/{4}_{5}_{6}.deb 2> /dev/null"
	                      .format(self._folder_package_linux_repo, self._distro_repo, self._codename_repo, self._temp_dir,
	                              self._repo, version, architecture))
			else:
				os.system("reprepro -b {0}/{1} includedeb {2} {3}/{4}_{5}_{6}.deb 2> /dev/null"
	                      .format(self._folder_package_linux_repo, self._distro_repo, self._codename_repo, self._temp_dir,
	                              self._repo, version, architecture))

			os.system('rm -rf /tmp/build')
