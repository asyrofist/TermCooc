#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
This script implements second-order co-occurrence for word similarity. 
Lemaire and Denhiere define that two words are associated by means of 
second-order co-occurrence if they share at least one word context. 
This view is based on the Harris' distributional hypothesis which states 
that words that occur in the same contexts tend to be similar.
"""
import sys
sys.path.insert(0, '..')
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def second_order():
    print("File for second order")

