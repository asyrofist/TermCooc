#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
This script implements first-order co-occurrence for word similarity. 
First-order co-occurrence, also called direct co-occurrence, occurs 
when two terms appear in identical contexts. It is based on the 
J.R. Firth saying "You shall know a word by the company it keeps.".
"""
import sys
sys.path.insert(0, '..')
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def first_order():
    print("File for first order")

