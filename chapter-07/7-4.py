# exercise 7.4

def count_word(arr):
    count = 0
    for w in arr:
        if len(w) == 5:
            count += 1
    return count


xs = ["one", "two", "three", "third", "fifth"]
print(count_word(xs))
