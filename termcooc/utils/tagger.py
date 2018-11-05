#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
This script parse text and tag all terms of a file
"""
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from nltk.parse.corenlp import CoreNLPParser

# {u'index': 1, u'word': u'no', u'lemma': u'no', u'pos': u'DT', 
#  u'characterOffsetEnd': 836, u'characterOffsetBegin': 834, 
#  u'originalText': u'no'}

additional_properties = {
    'tokenize.options': 'ptb3Escaping=false, unicodeQuotes=true, splitHyphenated=true, normalizeParentheses=false, normalizeOtherBrackets=false',
    'annotators': 'tokenize, ssplit, pos, lemma'
}

def tag_file(inputfile, lemma=True):
    stanford_parser = CoreNLPParser()
    with open(inputfile) as fin:
        content = []
        for line in fin:
            linepos = []
            line = line.strip()
            json_result = stanford_parser.api_call(line, properties=additional_properties)
            for sentence in json_result['sentences']:
                for dpos in sentence['tokens']:
                    if lemma:
                        word = dpos['lemma']
                    else:
                        word = dpos['word']
                    pos = dpos['pos']
                    linepos.append((word, pos))
            if linepos:
                content.append(linepos[:])
    print content
    
