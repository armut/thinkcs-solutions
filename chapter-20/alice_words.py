# exercise 20.3

import urllib.request
import wordtools

def retrieve_page(url):
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.read())
    my_socket.close()
    return dta


alice_book = retrieve_page("http://www.gutenberg.org/cache/epub/11/pg11.txt")
alice_book = alice_book[801:158020]
rn_removed = ' '.join(alice_book.split("\\r\\n"))
words = wordtools.extract_words(rn_removed)
word_occurences = {}
for word in words:
    if not word == "":
        word_occurences[word] = word_occurences.get(word, 0) + 1

print("Word\t\t\tCount")
print("==============================")
for (u, v) in sorted(word_occurences.items()):
    print("{0:25}{1}".format(u, v))

print("The word 'alice' occurs {0} times in the book.".format(word_occurences["alice"]))


# exercise 20.4

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("The longest word is {0} and it has {1} letters.".format(longest_word, len(longest_word)))
