#!/usr/bin/python3
# coding: utf-8
import os
import sys


config_dir = os.path.realpath(sys.argv[0])
config_dir = os.path.dirname(config_dir)
config_dir += "/config"
sys.path.insert(0, config_dir)

