# exercise 20.1

def letter_count(strng):
    char_counts = {}
    for char in strng.lower():
        if char != " ":
            char_counts[char] = char_counts.get(char, 0) + 1
    
    letter_items = list(char_counts.items())
    letter_items.sort()

    for (u, v) in letter_items:
        print(u + "  " + str(v))


letter_count("ThiS is String with Upper and lower case Letters")

