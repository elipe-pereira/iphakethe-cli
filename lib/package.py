#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from .dirs import Dirs
from .git import Git
from .repo import Repo
from config.config import Config


class Package(object):
    def __init__(self):
        self.__temp_dir = ""
        self.__git_addr = ""
        self.__user_git = ""
        self.__git_port = ""
        self.__repo = ""
        self.__folder_package_linux_repo = ""
        self.__testing = ""
        self.__branch_dev_testing = ""
        self.__distro_repo = ""
        self.__codename_repo = ""
        self.__keep_old_packages = ""
        self.__package_section = ""
        self.__package_name = ""
        self.__priority = ""
        self.__version = ""
        self.__architecture = ""
        self.__maintainer = ""
        self.__depends = ""
        self.__description = ""
        self.__command_pre_inst = ""
        self.__command_post_inst = ""
        self.__command_pre_rm = ""
        self.__command_post_rm = ""
        self.__so_dest_install = ""
        self.__dirs_to_remove = ""
        self.__dir_inst = ""
        self.__debian_folder = ""
        self.__config = Config()
        self.__dirs = Dirs()
        self.__git = Git(self.__git_addr, self.__git_port, self.__user_git, self.__repo)
        self.__project_root_dir = ""
        self.__package_file_name = ""

    def set_config(self, section):
        self.__config.set_temp_dir("/tmp/build")
        self.__config.set_git_addr(section, 'git_addr')
        self.__config.set_git_port(section, 'git_port')
        self.__config.set_user_git(section, 'user_git')
        self.__config.set_repo(section, 'repo')
        self.__config.set_folder_package_linux_repo(section, 'folder_package_linux_repo')
        self.__config.set_testing(section, 'testing')
        self.__config.set_branch_dev_testing(section, 'branch_dev_testing')
        self.__config.set_distro_repo(section, 'distro_repo')
        self.__config.set_codename_repo(section, 'codename_repo')
        self.__config.set_keep_old_packages(section, 'keep_old_packages')
        self.__config.set_package_section(section, 'package_section')
        self.__config.set_package_name(section, 'package_name')
        self.__config.set_priority(section, 'priority')
        self.__config.set_version(section, 'version')
        self.__config.set_architecture(section, 'architecture')
        self.__config.set_maintainer(section, 'maintainer')
        self.__config.set_depends(section, 'depends')
        self.__config.set_description(section, 'description')
        self.__config.set_command_pre_inst(section, 'command_pre_inst')
        self.__config.set_command_post_inst(section, 'command_post_inst')
        self.__config.set_command_pre_rm(section, 'command_pre_rm')
        self.__config.set_command_post_rm(section, 'command_post_rm')
        self.__config.set_so_dest_install(section, 'so_dest_install')
        self.__config.set_dirs_to_remove(section, 'dirs_to_remove')

    def load_config(self):
        self.__temp_dir = self.__config.get_temp_dir()
        self.__git_addr = self.__config.get_git_addr()
        self.__user_git = self.__config.get_user_git()
        self.__git_port = self.__config.get_git_port()
        self.__repo = self.__config.get_repo()
        self.__folder_package_linux_repo = self.__config.get_folder_package_linux_repo()
        self.__testing = self.__config.get_testing()
        self.__branch_dev_testing = self.__config.get_branch_dev_testing()
        self.__distro_repo = self.__config.get_distro_repo()
        self.__codename_repo = self.__config.get_codename_repo()
        self.__keep_old_packages = self.__config.get_keep_old_packages()
        self.__package_section = self.__config.get_package_section()
        self.__package_name = self.__config.get_package_name()
        self.__priority = self.__config.get_priority()
        self.__version = self.__config.get_version()
        self.__architecture = self.__config.get_architecture()
        self.__maintainer = self.__config.get_maintainer()
        self.__depends = self.__config.get_depends()
        self.__description = self.__config.get_description()
        self.__command_pre_inst = self.__config.get_command_pre_inst().split(',')
        self.__command_post_inst = self.__config.get_command_post_inst().split(',')
        self.__command_pre_rm = self.__config.get_command_pre_rm().split(',')
        self.__command_post_rm = self.__config.get_command_post_rm().split(',')
        self.__so_dest_install = self.__config.get_so_dest_install()
        self.__dirs_to_remove = self.__config.get_dirs_to_remove().split(',')

    def remove_temp_dir(self):
        self.__dirs.remove_dir(self.__temp_dir)

    def create_temp_dir(self):
        self.__dirs.create_dir(self.__temp_dir)

    def check_dest_install_and_clone(self):
        self.__git = Git(self.__git_addr, self.__git_port, self.__user_git, self.__repo)

        if self.__so_dest_install == "/":
            self.__dirs.change_dir(self.__temp_dir)

            self.__git.clone()

            dir_repo = "{0}/{1}".format(self.__temp_dir, self.__repo)
            self.__dir_inst = "{0}/{1}".format(self.__temp_dir, self.__package_name)

            self.__dirs.rename_dir(dir_repo, self.__dir_inst)

            self.__debian_folder = "{0}/{1}".format(self.__dir_inst, "DEBIAN")

            self.__dirs.create_dir(self.__debian_folder)

        else:
            self.__dir_inst = "{0}/{1}/{2}".format(self.__temp_dir, self.__package_name, self.__so_dest_install)
            self.__debian_folder = "{0}/{1}/{2}".format(self.__temp_dir, self.__package_name, "DEBIAN")

            self.__dirs.create_dir(self.__dir_inst)
            self.__dirs.create_dir(self.__debian_folder)
            self.__dirs.change_dir(self.__dir_inst)

            self.__git.clone()

            dir_repo = "{0}/{1}".format(self.__dir_inst, self.__repo)

            self.__dirs.rename_dir(dir_repo, "{0}/{1}".format(self.__dir_inst, self.__package_name))

    def write_debian_file(self):
        file_control = open("{0}/{1}".format(self.__debian_folder, 'control'), '+w')

        write_control = "Section: " + self.__package_section + "\n"
        write_control += "Package: " + self.__package_name + "\n"
        write_control += "Priority: " + self.__priority + "\n"
        write_control += "Version: " + self.__version + "\n"
        write_control += "Architecture: " + self.__architecture + "\n"
        write_control += "Maintainer: " + self.__maintainer + "\n"
        write_control += "Depends: " + self.__depends + "\n"
        write_control += "Description: " + self.__description + "\n\n"

        file_control.write(write_control)
        file_control.close()

    def write_pre_inst_file(self):
        file_command_pre_inst = open("{0}/{1}".format(self.__debian_folder, "preinst"), "+w")
        file_command_pre_inst.write("#!/bin/bash\n")

        for command in self.__command_pre_inst:
            file_command_pre_inst.write(command + "\n")

        file_command_pre_inst.close()

        self.__dirs.set_permission('0755', self.__debian_folder + "/preinst")

    def write_post_inst_file(self):
        file_command_post_inst = open("{0}/{1}".format(self.__debian_folder, "postinst"), "+w")
        file_command_post_inst.write("#!/bin/bash\n")

        for command in self.__command_post_inst:
            file_command_post_inst.write(command + "\n")

        file_command_post_inst.close()

        self.__dirs.set_permission('0755', self.__debian_folder + "/postinst")

    def write_pre_rm_file(self):
        file_command_pre_rm = open("{0}/{1}".format(self.__debian_folder, "prerm"), "+w")
        file_command_pre_rm.write("#!/bin/bash\n")

        for command in self.__command_pre_rm:
            file_command_pre_rm.write(command + "\n")

        file_command_pre_rm.close()

        self.__dirs.set_permission('0755', self.__debian_folder + "/prerm")

    def write_post_rm_file(self):
        file_command_post_rm = open("{0}/{1}".format(self.__debian_folder, "postrm"), "+w")
        file_command_post_rm.write("#!/bin/bash\n")

        for command in self.__command_post_rm:
            file_command_post_rm.write(command + "\n")

        file_command_post_rm.close()

        self.__dirs.set_permission('0755', self.__debian_folder + "/prerm")

    def if_testing_change_branch(self):
        if self.__testing == "yes":
            dir_package = "{0}/{1}".format(self.__dir_inst, self.__package_name)

            self.__dirs.change_dir(dir_package)
            self.__git.checkout(self.__branch_dev_testing)

    def clean_project(self):
        for directory in self.__dirs_to_remove:
            directory = "{0}/{1}/{2}".format(self.__dir_inst, self.__package_name, directory)
            self.__dirs.remove_dir(directory)

    def build(self):
        self.__project_root_dir = "{0}/{1}".format(self.__temp_dir, self.__package_name)

        self.__dirs.set_permission('0755', self.__project_root_dir)
        os.system("dpkg -b {0} {1}".format(self.__project_root_dir, self.__temp_dir))

    def send_to_repo(self):
        repo = Repo()

        self.__package_file_name = "{0}/{1}_{2}_{3}.deb".format(
            self.__temp_dir,
            self.__package_name,
            self.__version,
            self.__architecture)

        repo.send_to_repo(self.__package_file_name, self.__keep_old_packages)
