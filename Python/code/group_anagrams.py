# -*- coding: utf-8 -*-
"""
    Anagrams are words formed by rearranging letters of another word, For example, car and arc, cat and act, etc.

    Credits to resources by Aman Kharwal.
    Url: https://thecleverprogrammer.com/2022/05/26/group-anagrams-using-python/

Author:
    Joshua Gan - 04.07.2023
"""


def group_anagrams(alist):
    """
    A function that groups anagrams from a given list of words.
    """
    from collections import defaultdict

    # Creates a dictionary-like object with a default value for the key that does not exist
    dfdict = defaultdict(list)
    for word in alist:
        # print(word)
        # Sort characters and concatenate them
        sword = " ".join(sorted(word))
        # print(sword)
        dfdict[sword].append(word)
    return dfdict.items()


a = ["tea", "eat", "bat", "ate", "arc", "car"]
group_anagrams(a)
