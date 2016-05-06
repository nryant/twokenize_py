I. Overview
===========
twokenize_py is a backport of CMU's `Twokenize <https://github.com/brendano/ark-tweet-nlp/blob/master/src/cmu/arktweetnlp/Twokenize.java>`_ from Java to
Python that was written in 2013 to support learning of word embeddings from
messy online discussion forum data.

II. Dependencies
================
The following are required to run this software:

- Python >= 2.7.1 (https://www.python.org/)
- regex >= 2.4    (https://pypi.python.org/pypi/regex)

In most cases versions older than those indicated should also work.


III. Installation
=================
To install into your home directory::

    python setup.py install --user

To install for all users on Unix/Linux::

    sudo python setup.py install


III. Example
============
To tokenize a text create a new ``Tokenizer`` instance, then call its
``tokenize`` method::

    >>> from twokenize_py import Tokenizer
    >>> tok = Tokenizer()
    >>> text = """Think about it: "Blood Simple" was the best film of 1984; "Raising Arizona" was the best film of 1987; "Miller's Crossing" was the best movie of 1990; "Barton Fink" was the best movie of 1991; and "Fargo" was the best movie of 1996."""
    >>> tokens = tok.tokenize(text)
    >>> print(tokens)

which outputs::

    ['Think', 'about', 'it', ':', '"', 'Blood', 'Simple', '"', 'was', 'the', 'best', 'film', 'of', '1984', ';', '"', 'Raising', 'Arizona', '"', 'was', 'the', 'best', 'film', 'of', '1987', ';', '"', u"Miller's", 'Crossing', '"', 'was', 'the', 'best', 'movie', 'of', '1990', ';', '"', 'Barton', 'Fink', '"', 'was', 'the', 'best', 'movie', 'of', '1991', ';', 'and', '"', 'Fargo', '"', 'was', 'the', 'best', 'movie', 'of', '1996', '.']

The onset and offsets in characters of the tokens may be recovered using
``twokenize_py.Aligner`` as in the following::

    >>> from twokenize_py import Aligner, Tokenizer
    >>> tok = Tokenizer()
    >>> text = 'Oh Captain! My Captain!'
    >>> tokens = tok.tokenize(text)
    >>> aligner = Aligner()
    >>> spans = aligner.align(text, tokens)
    >>> for token, (onset, offset) in zip(tokens, spans):
    ...     print(token, onset, offset)

which produces::

    ('Oh', 0, 1)
    ('Captain', 3, 9)
    ('!', 10, 10)
    ('My', 12, 13)
    ('Captain', 15, 21)
    ('!', 22, 22)
