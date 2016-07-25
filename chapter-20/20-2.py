# exercise 20.2

"""Python 3.5.2 (default, Jul  5 2016, 12:43:10) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> d = {"apples": 15, "bananas": 35, "grapes": 12}
>>> d["bananas"]
35
>>> d["oranges"] = 20
>>> len(d)
4
>>> "grapes" in d
True
>>> d["pears"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'pears'
>>> d.get("pears", 0)
0
>>> fruits = list(d.keys())
>>> fruits.sort()
>>> print(fruits)
['apples', 'bananas', 'grapes', 'oranges']
>>> del d["apples"]
>>> "apples" in d
False
>>> exit()"""

import sys

def test(did_pass):
    """ Print the result of the test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)



def add_fruit(inventory, fruit, quantity=0):
    if not len(inventory) == 0:
        tmp = inventory[fruit]
        inventory[fruit] = quantity + tmp
    else:
        inventory[fruit] = quantity

 

new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
test("strawberries" in new_inventory)
test(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
test(new_inventory["strawberries"] == 35)
