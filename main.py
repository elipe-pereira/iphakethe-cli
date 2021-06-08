#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
from iphakethe import Iphakethe
from lib.debug import Debug


class Main(object):
    def __init__(self):
        self.realpath = os.path.realpath(sys.argv[0])
        self.iphakethe_working_dir = os.path.dirname(self.realpath)
        self.iphakethe_lib_dir = self.iphakethe_working_dir + "/lib"
        self.debug = Debug()

    def main(self):
        command_line_argument = ""

        try:
            if sys.argv[1]:
                command_line_argument = sys.argv[1]
        except:
            self.debug.log("Execução sem parâmetros de linha de comando")

        os.environ['IPHAKETHE_WORKING_DIR'] = self.iphakethe_working_dir
        os.environ['IPHAKETHE_LIB_DIR'] = self.iphakethe_lib_dir
        
        iphakethe = Iphakethe(command_line_argument)
        iphakethe.pack()


if __name__ == '__main__':
    run = Main()
    run.main()
