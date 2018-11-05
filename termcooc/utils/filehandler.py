#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
This script contains util functions
"""
import sys
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from os.path import realpath, isfile


def is_file(inputfile, boolean=False):
    """ Check whether the ``inputfile`` corresponds to a file """
    inputfile = realpath(inputfile)
    if not isfile(inputfile):
        if boolean:
            return False
        logger.error('Input is not a file!')
        sys.exit(0)
    return inputfile


def is_folder(inputfolder, boolean=False):
    """ Check whether the ``inputfolder`` corresponds to a folder """
    inputfolder = realpath(inputfolder)
    if not isdir(inputfolder):
        if boolean:
            return False
        logger.error('Argument %s is not a folder!' % inputfolder)
        sys.exit(0)
    return inputfolder


class MatrixMarket(object):
    """ 
    Create or load a matrix market (.mm) file.
        .mm files start by index 1
    """
    def __init__(self):
        pass

    def add(self):
        pass
