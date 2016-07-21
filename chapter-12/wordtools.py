# exercise 12.8

import sys

def test(did_pass):
    """ Print the result of the test. """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def cleanword(strng):
    sans_punct = ""
    for c in strng:
        if c not in punctuation:
            sans_punct += c
    return sans_punct

def has_dashdash(strng):
    for c in enumerate(strng):
        if (not c[0] == len(strng)-1) and c[1] == "-":
            if strng[c[0]+1] == "-":
                return True
    return False
            
def extract_words(strng):
    strng_lower = strng.lower()
    strng_nodashes = ""
    if has_dashdash(strng_lower):
        strng_nodashes = ' '.join(strng_lower.split("--"))
    else:
        strng_nodashes = strng_lower
    words = strng_nodashes.split()
    strng_clean = []
    for word in words:
        strng_clean.append(cleanword(word))

    return strng_clean

def wordcount(strng, llist):
    count = 0
    for s in llist:
        if s == strng:
            count += 1
    return count

def wordset(llist):
    word_set = []
    for word in llist:
        if word not in word_set:
            word_set.append(word)
    return sorted(word_set)

def longestword(llist):
    longest_word = ""
    for word in llist:
        if len(word) > len(longest_word):
            longest_word = word
    return len(longest_word)


test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
      ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
    ['she','tried','to','curtsey','as','she','spoke','fancy'])

test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
    ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)
