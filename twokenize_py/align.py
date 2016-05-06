"""Aligner for texts and their segmentations.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

__all__ = ['AlignmentFailed', 'Aligner']


class AlignmentFailed(Exception): pass


class Aligner(object):
    """Align a text with its tokenization.
    """
    def align(self, text, tokens):
        """Align text with its tokeniation.

        Parameters
        ----------
        text : str
            Text.

        tokens : list of str
            Tokenization of ``text``.

        Returns
        -------
        spans : list of tuple
            List of (``onset``, ``offset``) pairs, where ``spans[i]`` gives the
            onseta and offset in characters of ``tokens[i]`` relative to the
            beginning of ``text`` (0-indexed).
        """
        spans = []
        bi = 0
        for token in tokens:
            try:
                token_len = len(token)
                token_bi = bi + text[bi:].index(token)
                token_ei = token_bi + token_len - 1
                spans.append([token_bi, token_ei])
                bi = token_ei + 1
            except ValueError:
                raise AlignmentFailed(token)

        return spans
