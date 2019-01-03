#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
This script implements third (or higher)-order co-occurrence for word similarity. 
Gamallo and Bordag explain third-order (or higher) co-occurrences as co-occurrences 
between words that do not co-occur in the corpus with the same words 
(or lexical-syntactic contexts) but between words that can be related through 
further indirect co-occurrences.
"""
import sys
sys.path.insert(0, '..')
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def third_order():
    print("File for third (or higher) order")

