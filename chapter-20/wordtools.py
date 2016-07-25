punctuation = "!\"#$%&'()*+,./:;<=>?@[\\]^_`{|}~"

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

