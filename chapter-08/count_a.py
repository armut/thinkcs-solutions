def count_a(text):
    count = 0
    for c in text:
        if c == "a":
            count += 1
    return count


print(count_a("banana"))
