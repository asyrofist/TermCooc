#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
This script run first-order co-occurrence for word similarity. 
"""

import sys
sys.path.insert(0, '..')
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import argparse

from utils import fileconfig as fc
from utils import filehandler as fh
from utils import tagger

import order_fst as order

def main(inputfile):
    inputfile = fh.is_file(inputfile)

    # extract content from settings.conf
    settings = fc.Configuration()
    server = settings.get('SERVER')


    tagger.tag_content(inputfile)

    #order.first_order()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', metavar='input_text', help='File containing text to generate synonyms')
    #parser.add_argument('featuresfile', metavar='file_feats', help='File containing paths and features')
    #parser.add_argument('-o', '--output', help='File to save the output. In empty case, the output is the features file', default=None)
    args = parser.parse_args()
    main(args.input)
