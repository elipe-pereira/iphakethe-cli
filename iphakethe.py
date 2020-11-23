#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from config.config import Config
from lib.dirs import Dirs
from lib.debug import Debug
from lib.package import Package


class Iphakethe(object):
    def __init__(self, command_line_argument):
        self.__config = Config()
        self.__dirs = Dirs()
        self.__debug = Debug()
        self.__command_line_argument = command_line_argument

    def pack(self):
        package = Package()
        self.__config.set_sections()
        sections = self.__config.get_sections()

        if self.__command_line_argument in sections:
            package.set_config(self.__command_line_argument)
            package.load_config()
            package.remove_temp_dir()
            package.create_temp_dir()
            package.check_dest_install_and_clone()
            package.if_testing_change_branch()
            package.write_debian_file()
            package.write_pre_inst_file()
            package.write_post_inst_file()
            package.write_pre_rm_file()
            package.write_post_rm_file()
            package.clean_project()
            package.build()
            package.send_to_repo()
            package.remove_temp_dir()
        else:
            for section in sections:
                package.set_config(section)
                package.load_config()
                package.remove_temp_dir()
                package.create_temp_dir()
                package.check_dest_install_and_clone()
                package.if_testing_change_branch()
                package.write_debian_file()
                package.write_pre_inst_file()
                package.write_post_inst_file()
                package.write_pre_rm_file()
                package.write_post_rm_file()
                package.clean_project()
                package.build()
                package.send_to_repo()
                package.remove_temp_dir()
