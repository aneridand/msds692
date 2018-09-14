import sys

import nltk
from nltk.stem.porter import *
from sklearn.feature_extraction import stop_words
import xml.etree.cElementTree as ET
from collections import Counter
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import zipfile
import os

PARTIALS = False

def gettext(xmltext):
    """
    Parse xmltext and return the text from <title> and <text> tags
    """
    xmltext = xmltext.encode('ascii', 'ignore') # ensure there are no weird char


def tokenize(text):
    """
    Tokenize text and return a non-unique list of tokenized words
    found in the text. Normalize to lowercase, strip punctuation,
    remove stop words, drop words of length < 3.
    """


def stemwords(words):
    """
    Given a list of tokens/words, return a new list with each word
    stemmed using a PorterStemmer.
    """


def tokenizer(text):
    return stemwords(tokenize(text))


def compute_tfidf(corpus):
    """
    Create and return a TfidfVectorizer object after training it on
    the list of articles pulled from the corpus dictionary. The
    corpus argument is a dictionary mapping file name to xml text.
    """


def summarize(tfidf, text, n):
    """
    Given a trained TfidfVectorizer object and some XML text, return
    up to n (word,score) pairs in a list. Discard any terms with
    scores < 0.09.
    """


def load_corpus(zipfilename):
    """
    Given a zip file containing root directory reuters-vol1-disk1-subset
    and a bunch of *.xml files, read them from the zip file into
    a dictionary of (word,xmltext) associations. Use namelist() from
    ZipFile object to get list of xml files in that zip file.
    Convert filename reuters-vol1-disk1-subset/foo.xml to foo.xml
    as the keys in the dictionary. The values in the dictionary are the
    raw XML text from the various files.
    """
