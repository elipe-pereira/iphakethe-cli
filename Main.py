#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
from Iphakethe import Iphakethe


class Main(object):
    def __init__(self):
        self.realpath = os.path.realpath(sys.argv[0])
        self.iphakethe_working_dir = os.path.dirname(self.realpath)
        self.iphakethe_lib_dir = self.iphakethe_working_dir + "/lib"

    def main(self):
        os.environ['IPHAKETHE_WORKING_DIR'] = self.iphakethe_working_dir
        os.environ['IPHAKETHE_LIB_DIR'] = self.iphakethe_lib_dir
        iphakethe = Iphakethe()
        iphakethe.pack()


if __name__ == '__main__':
    run = Main()
    run.main()
