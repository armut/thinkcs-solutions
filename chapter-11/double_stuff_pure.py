def double_stuff_pure(a_list):
    """ Return a new list which contains
        doubles of the elements in a_list.
    """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)

    return new_list


things = [2, 5, 9]
xs = double_stuff_pure(things)
print(things)
print(xs)
