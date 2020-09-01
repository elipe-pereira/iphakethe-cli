#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from config.Config import Config
from lib.Dirs import Dirs
from lib.Git import Git
from lib.Debug import Debug


class Iphakethe(object):
    def __init__(self):
        self.__config = Config()
        self.__dirs = Dirs()
        self.__debug = Debug()

    def pack(self):
        config = Config()
        config.set_sections()
        sections = config.get_sections()

        for section in sections:
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
            self.__config.set_package(section, 'package')
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

            temp_dir = self.__config.get_temp_dir()
            git_addr = self.__config.get_git_addr()
            user_git = self.__config.get_user_git()
            git_port = self.__config.get_git_port()
            repo = self.__config.get_repo()
            folder_package_linux_repo = self.__config.get_folder_package_linux_repo()
            testing = self.__config.get_testing()
            branch_dev_testing = self.__config.get_branch_dev_testing()
            distro_repo = self.__config.get_distro_repo()
            codename_repo = self.__config.get_codename_repo()
            keep_old_packages = self.__config.get_keep_old_packages()
            package_section = self.__config.get_package_section()
            package = self.__config.get_package()
            priority = self.__config.get_priority()
            version = self.__config.get_version()
            architecture = self.__config.get_architecture()
            maintainer = self.__config.get_maintainer()
            depends = self.__config.get_depends()
            description = self.__config.get_description()
            command_pre_inst = self.__config.get_command_pre_inst().split(',')
            command_post_inst = self.__config.get_command_post_inst().split(',')
            command_pre_rm = self.__config.get_command_pre_rm().split(',')
            command_post_rm = self.__config.get_command_post_rm().split(',')
            so_dest_install = self.__config.get_so_dest_install()
            dirs_to_remove = self.__config.get_dirs_to_remove().split(',')

            if self.__dirs.check_dir(temp_dir):
                os.system("rm -rf {0}".format(temp_dir))

            self.__dirs.check_dir_and_create_and_go_to(temp_dir)

            dir_inst = "{0}/{1}/{2}".format(temp_dir, package, so_dest_install)
            debian_folder = "{0}/{1}/{2}".format(temp_dir, package, "DEBIAN")
            os.makedirs(dir_inst)
            os.mkdir(debian_folder)

            file_control = open("{0}/{1}".format(debian_folder, 'control'), '+w')

            write_control = "Section: " + package_section + "\n"
            write_control += "Package: " + package + "\n"
            write_control += "Priority: " + priority + "\n"
            write_control += "Version: " + version + "\n"
            write_control += "Architecture: " + architecture + "\n"
            write_control += "Maintainer: " + maintainer + "\n"
            write_control += "Depends: " + depends + "\n"
            write_control += "Description: " + description + "\n\n"

            file_control.write(write_control)
            file_control.close()

            file_command_pre_inst = open("{0}/{1}".format(debian_folder, "preinst"), "+w")
            file_command_pre_inst.write("#!/bin/bash\n")

            for command in command_pre_inst:
                file_command_pre_inst.write(command + "\n")

            file_command_pre_inst.close()

            os.chmod("{0}/{1}".format(debian_folder, "preinst"), 0o755)

            file_command_post_inst = open("{0}/{1}".format(debian_folder, "postinst"), "+w")
            file_command_post_inst.write("#!/bin/bash\n")

            for command in command_post_inst:
                file_command_post_inst.write(command + "\n")

            file_command_post_inst.close()

            os.chmod("{0}/{1}".format(debian_folder, 'postinst'), 0o755)

            file_command_pre_rm = open("{0}/{1}".format(debian_folder, "prerm"), "+w")
            file_command_pre_rm.write("#!/bin/bash\n")

            for command in command_pre_rm:
                file_command_pre_rm.write(command + "\n")

            file_command_pre_rm.close()

            os.chmod("{0}/{1}".format(debian_folder, "prerm"), 0o755)

            file_command_post_rm = open("{0}/{1}".format(debian_folder, "postrm"), "+w")
            file_command_post_rm.write("#!/bin/bash\n")

            for command in command_post_rm:
                file_command_post_rm.write(command + "\n")

            file_command_post_rm.close()

            os.chdir("{0}/{1}/{2}".format(temp_dir, package, so_dest_install))

            git = Git(git_addr, git_port, user_git, repo)
            git.clone()

            os.rename(
                "{0}/{1}/{2}/{3}".format(temp_dir, package, so_dest_install, repo),
                "{0}/{1}/{2}/{1}".format(temp_dir, package, so_dest_install))

            if testing == "yes":
                os.chdir("{0}/{1}/{2}/{3}".format(temp_dir, package, so_dest_install, package))
                git.checkout(branch_dev_testing)

            for directory in dirs_to_remove:
                os.system("rm -rf {0}/{1}/{2}/{1}/{3}".format(temp_dir, package, so_dest_install, directory))

            folder = "{0}/{1}".format(temp_dir, package)

            self.__dirs.set_permission('0755', folder)

            os.system("dpkg -b {0} {1}".format(folder, temp_dir))

            if keep_old_packages == "yes":
                os.system("reprepro --keepunreferencedfiles -b {0}/{1} includedeb {2} {3}/{4}_{5}_{6}.deb".format(
                        folder_package_linux_repo,
                        distro_repo,
                        codename_repo,
                        temp_dir,
                        package,
                        version,
                        architecture))

            else:
                os.system("reprepro -b {0}/{1} includedeb {2} {3}/{4}_{5}_{6}.deb".format(
                    folder_package_linux_repo,
                    distro_repo,
                    codename_repo,
                    temp_dir,
                    package,
                    version,
                    architecture))

            os.system("rm -rf {0}".format(temp_dir))

