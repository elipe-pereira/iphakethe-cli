#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
from configparser import ConfigParser
from Iphakethe import Iphakethe
import time

class Main(object):
    realpath = os.path.realpath(sys.argv[0])
    iphakethe_working_dir = os.path.dirname(realpath)
    iphakethe_lib_dir = iphakethe_working_dir + "/lib"
    
    os.environ['IPHAKETHE_WORKING_DIR'] = iphakethe_working_dir
    os.environ['IPHAKETHE_LIB_DIR'] = iphakethe_lib_dir

    def main():	
        iphakethe = Iphakethe()

        # iphakethe.pack()


if __name__ == '__main__':
    Main.main()
	