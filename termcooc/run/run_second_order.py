#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
This script run second-order co-occurrence for word similarity. 
"""

import sys
sys.path.insert(0, '..')
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import argparse

import order_snd as order

def main():
    order.second_order()


if __name__ == "__main__":
    #parser = argparse.ArgumentParser()
    #parser.add_argument('groundtruth', metavar='file_ground', help='File containing paths and true labels')
    #parser.add_argument('featuresfile', metavar='file_feats', help='File containing paths and features')
    #parser.add_argument('-o', '--output', help='File to save the output. In empty case, the output is the features file', default=None)
    #args = parser.parse_args()
    #main(args.groundtruth, args.featuresfile, args.output)
    main()
