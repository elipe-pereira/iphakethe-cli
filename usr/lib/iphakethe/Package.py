#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
import os


class Package(object):
    config = configparser.ConfigParser()
    config.read('/etc/iphakethe/iphakethe.conf')
    temp_dir = "/tmp/build"

    def verify_if_temp_dir_exists(self):
        if os.path.exists(self.temp_dir):
            os.chdir(self.temp_dir)
        else:
            os.mkdir(self.temp_dir)
            os.chdir(self.temp_dir)

        return True

    def get_git_addr(self, repo):
        git_addr = self.config.get(repo, 'git_addr')

        return git_addr


