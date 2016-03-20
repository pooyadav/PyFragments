# -----------------
# User Instructions
# 
# This homework deals with anagrams. An anagram is a rearrangement 
# of the letters in a word to form one or more new words. 
#
# Your job is to write a function anagrams(), which takes as input 
# a phrase and an optional argument, shortest, which is an integer 
# that specifies the shortest acceptable word. Your function should
# return a set of all the possible combinations of anagrams. 
#
# Your function should not return every permutation of a multi word
# anagram: only the permutation where the words are in alphabetical
# order. For example, for the input string 'ANAGRAMS' the set that 
# your function returns should include 'AN ARM SAG', but should NOT 
# include 'ARM SAG AN', or 'SAG AN ARM', etc...

import math
import itertools as it

## My solution works, but terribly slow
def anagrams(phrase, shortest=2):
    """Return a set of phrases with words from WORDS that form anagram
    of phrase. Spaces can be anywhere in phrase or anagram. All words 
    have length >= shortest. Phrases in answer must have words in 
    lexicographic order (not all permutations)."""
    # your code here
    def exactCombo(wordstuple):
        if wordstuple == (): return False
        combined = reduce(lambda x, y: x+y, wordstuple)
        return len(combined) == len(phrase) and sorted(combined) == sorted(phrase) # --25s
        #return sorted(combined) == sorted(phrase) # -- 8s

    phrase = phrase.replace(' ', '')
    words = find_words(phrase)
    words = filter(lambda x : len(x) >= shortest, words)
    MaxTry = int(math.floor(len(phrase)/shortest))
    results = []
    for n in range(1,MaxTry+1):
        combx = it.combinations(words, n)
        answers = filter(exactCombo, combx)
        results.extend(answers)
    results = map(sorted, results)
    return set(map(lambda wl : ' '.join(wl), results))

# ======== PN's solution ==========

def anagrams2(phrase, shortest=2):
    return(find_anagrams(phrase.replace(' ', ''), '', shortest))

def find_anagrams(letters, previous_word, shortest):
    results = set()
    for w in find_words(letters):
        if len(w) >= shortest and w > previous_word:
            remainder = removed(letters, w)
            if remainder:
                for rest in find_anagrams(remainder, w, shortest):
                    results.add(w + ' ' + rest)
            else:
                results.add(w)
    return results
        
# ------------
# Helpful functions
# 
# You may find the following functions useful. These functions
# are identical to those we defined in lecture. 

def removed(letters, remove):
    "Return a str of letters, but with each letter in remove removed once."
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters

def find_words(letters):
    return extend_prefix('', letters, set())

def extend_prefix(pre, letters, results):
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            extend_prefix(pre+L, letters.replace(L, '', 1), results)
    return results

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    "Return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)"
    wordset = set(open(filename).read().upper().split())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset

WORDS, PREFIXES = readwordlist('words4k.txt')

# ------------
# Testing
# 
# Run the function test() to see if your function behaves as expected.

def test():
    assert 'DOCTOR WHO' in anagrams('TORCHWOOD')
    assert 'BOOK SEC TRY' in anagrams('OCTOBER SKY')
    assert 'SEE THEY' in anagrams('THE EYES')
    assert 'LIVES' in anagrams('ELVIS')
    assert anagrams('PYTHONIC') == set([
        'NTH PIC YO', 'NTH OY PIC', 'ON PIC THY', 'NO PIC THY', 'COY IN PHT',
        'ICY NO PHT', 'ICY ON PHT', 'ICY NTH OP', 'COP IN THY', 'HYP ON TIC',
        'CON PI THY', 'HYP NO TIC', 'COY NTH PI', 'CON HYP IT', 'COT HYP IN',
        'CON HYP TI'])
    return 'tests pass'

import time
def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

#print timedcall(test)
