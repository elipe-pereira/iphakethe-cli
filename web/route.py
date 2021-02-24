#!/usr/bin/python3
# coding: utf-8

class Route(object):
    def __init__(self, path, file , content_type):
        self.__route = path
        self.__file = file
        self.__content_tipe = content_type
