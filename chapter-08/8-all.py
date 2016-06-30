import sys

def test(did_pass):
    """Print the result of the test"""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


# exercise 8.2
def ex8_2():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter is "O" or letter is "Q":
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)


# exercise 8.3
def count_letters(strng, ch):
    count = 0
    for char in strng:
        if char == ch:
            count += 1
    return count


# exercise 8.4
def find(strng, ch, start=0):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1


def count_letterz(strng, ch):
    count = 0
    s_point = find(strng, ch, 0)
    while s_point != -1:
        s_point = find(strng, ch, s_point + 1)
        count += 1
    return count


# exercise 8.5
def remove_punctuation(s):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    sans_punct = ""
    for letter in s:
        if letter not in punctuation:
            sans_punct += letter
    return sans_punct


def ex8_5():
    instants = """  INSTANTS

    If I could live again my life,
    In the next - I'll try,
    - to make more mistakes,
    I won't try to be so perfect,
    I'll be more relaxed,
    I'll be more full - than I am now,
    In fact, I'll take fewer things seriously,
    I'll be less hygenic,
    I'll take more risks,
    I'll take more trips,
    I'll watch more sunsets,
    I'll climb more mountains,
    I'll swim more rivers,
    I'll go to more places - I've never been,
    I'll eat more ice creams and less (lime) beans,
    I'll have more real problems - and less imaginary
                                            ones,
    I was one of those people who live
                    prudent and prolific lives -
                            each minute of his life,
    Offcourse that I had moments of joy  - but,
     if I could go back I'll try to have only good moments,

    If you don't know - thats what life is made of,
    Don't lose the now! 

    I was one of those who never goes anywhere
                    without a thermometer,
    without a hot-water bottle,
     and without an umberella and without a parachute,

    If I could live again - I will travel light,
    If I could live again - I'll try to work bare feet
                    at the beginning of spring till 
                      the end of autumn,
    I'll ride more carts,
    I'll watch more sunrises and play with more children,
    If I have the life to live - but now I am 85,
            - and I know that I am dying ...

 

            Jorge Luis BORGES """
            
    list_of_words = remove_punctuation(instants).split()
    count_e = 0
    count = 0
    for word in list_of_words:
        if "e" in word:
            count_e += 1
        else:
            count += 1
    percentage = (100 * count_e) / (count + count_e)
    print("Your text contains {0} words, of which {1} ({2:.1f}%) contain an \"e\".".format(count + count_e, count_e, percentage))
    


# exercise 8.6
layout = "{0:>3}"
def get_multiplies(n, high):
    table = ""
    for i in range(1, high+1):
        table += layout.format(n*i) + " "
    return table


def print_mult_table(high):
    lin = "  :"
    for i in range(1, high+1):
        if i == 1:
            print("{0:>8}{1}".format(" ", get_multiplies(1, high)))
            for l in range(len(get_multiplies(1, high)) + 4):
                lin += "-"
            print("{0:<}".format(lin))
        print("{0:>2}{1:<6}{2}".format(str(i), ":", get_multiplies(i, high)))



# exercise 8.7
def reverse(strng):
    res = ""
    for i in range(1, len(strng)+1):
        res += strng[-i]
    return res


test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")



# exercise 8.8
def mirror(strng):
    return strng + reverse(strng)


test(mirror("good") == "gooddoog")
test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")



# exercise 8.9
def remove_letter(ch, strng):
    final_string = ""
    for c in strng:
        if c is not ch:
            final_string += c
    return final_string


test(remove_letter("a", "apple") == "pple")
test(remove_letter("a", "banana") == "bnn")
test(remove_letter("z", "banana") == "banana")
test(remove_letter("i", "Mississippi") == "Msssspp")
test(remove_letter("b", "") == "")
test(remove_letter("b", "c") == "c")



# exercise 8.10
def is_palindrome(strng):
    half = strng[0:len(strng)//2]
    if len(strng) % 2 == 0:
        if strng == half + reverse(half):
            return True
        else:
            return False
    else:
        if strng[len(half)+1:] == reverse(half):
            return True
        else:
            return False


test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome(""))



# exercise 8.11
def count(subs, strng):
    tally = 0
    for i in range(len(strng)-len(subs)+1):
        if strng[i:i+len(subs)] == subs:
            tally += 1
    return tally


test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 4)



# exercise 8.12
def remove(subs, strng):
    for i in range(len(strng)-len(subs)+1):
        if strng[i:i+len(subs)] == subs:
            return strng[:i] + strng[i+len(subs):]


test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") != "bicycle")



# exercise 8.13
def remove_all(subs, strng):
    result = ""
    while subs in strng:
        strng = remove(subs, strng)
    return strng


test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")
