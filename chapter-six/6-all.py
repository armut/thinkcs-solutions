import sys

def test(did_pass):
    """ Print the result of the test. """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

# exercise 6.1
def turn_clockwise(point):
    if point == "W":
        return "N"
    elif point == "N":
        return "E"
    elif point == "E":
        return "S"
    elif point == "S":
        return "W"

# exercise 6.2
def day_name(num_of_the_day):
    if num_of_the_day == 0:
        return "Sunday"
    elif num_of_the_day == 1:
        return "Monday"
    elif num_of_the_day == 2:
        return "Tuesday"
    elif num_of_the_day == 3:
        return "Wednesday"
    elif num_of_the_day == 4:
        return "Thursday"
    elif num_of_the_day == 5:
        return "Friday"
    elif num_of_the_day == 6:
        return "Saturday"

# exercise 6.3
def day_num(name_of_the_day):
    if name_of_the_day == "Sunday":
        return 0
    elif name_of_the_day == "Monday":
        return 1
    elif name_of_the_day == "Tuesday":
        return 2
    elif name_of_the_day == "Wednesday":
        return 3
    elif name_of_the_day == "Thursday":
        return 4
    elif name_of_the_day == "Friday":
        return 5
    elif name_of_the_day == "Saturday":
        return 6

# exercise 6.4 - 6.5
def day_add(name_of_the_day, offset):
    num_of_the_day = day_num(name_of_the_day)
    result = (num_of_the_day + offset) % 7
    return day_name(result)

# exercise 6.6
def days_in_month(name_of_the_month):
    if name_of_the_month == "January":
        return 31
    elif name_of_the_month == "February":
        return 28
    elif name_of_the_month == "March":
        return 31
    elif name_of_the_month == "April":
        return 30
    elif name_of_the_month == "May":
        return 31
    elif name_of_the_month == "June":
        return 30
    elif name_of_the_month == "July":
        return 31
    elif name_of_the_month == "August":
        return 31
    elif name_of_the_month == "September":
        return 30
    elif name_of_the_month == "October":
        return 31
    elif name_of_the_month == "November":
        return 30
    elif name_of_the_month == "December":
        return 31

# exercise 6.7 - 6.8
def to_secs(h, m, s):
    return int((h*60*60) + (m*60) + s)

# exercise 6.9
def hours_in(sec):
    return int(sec/3600)


def minutes_in(sec):
    remaining_sec = sec - (hours_in(sec) * 3600)
    return int(remaining_sec / 60)


def seconds_in(sec):
    remaining_sec = (sec - (hours_in(sec) * 3600)) - (minutes_in(sec) * 60)
    return remaining_sec

# exercise 6.11
def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    elif a < b:
        return -1

# exercise 6.12
def hypotenuse(side1, side2):
    hypot = ((side1 * side1) + (side2 * side2)) ** 0.5
    return hypot

# exercise 6.13
def slope(x1, y1, x2, y2):
    d1 = y1 - y2
    d2 = x1 - x2
    return d1 / d2


def intercept(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    return y1 - m*x1

# exercise 6.14
def is_even(n):
    if n % 2 == 0:
        return True
    return False

# exercise 6.15
def is_odd(n):
    if is_even(n) == False:
        return True
    else:
        return False

# exercise 6.16
def is_factor(f, n):
    if n % f == 0:
        return True
    else:
        return False

# exercise 6.17
def is_multiple(n, f):
    if is_factor(f, n):
        return True
    else:
        return False

# exercise 6.18
def f2c(t):
   result = (t - 32) / 1.8
   return round(result)

# exercise 6.19
def c2f(t):
    result = 1.8 * t + 32
    return round(result)

def test_suite():
    print("exercise 6.1")
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    print()

    print("exercise 6.2")
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    print()
    
    print("exercise 6.3")
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    print()
    
    print("exercise 6.4")
    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    print()

    print("exercise 6.5")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    print()

    print("exercise 6.6")
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    print()

    print("exercise 6.7")
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    print()

    print("exercise 6.8")
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433,0,0) == 8758)
    print()

    print("exercise 6.9")
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)
    print()

    print("exercise 6.10")
    test(3 % 4 == 0)
    test(3 % 4 == 3)
    test(3 / 4 == 0)
    test(3 // 4 == 0)
    test(3+4  *  2 == 14)
    test(4-2+2 == 0)
    test(len("hello, world!") == 13)
    print()

    print("exercise 6.11")
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    print()

    print("exercise 6.12")
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    print()

    print("exercise 6.13")
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)

    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)
    print()

    print("exercise 6.14")
    test(is_even(2) == True)
    test(is_even(3) == False)
    print()

    print("exercise 6.15")
    test(is_odd(2) == False)
    test(is_odd(3) == True)
    print()

    print("exercise 6.16")
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))
    print()

    print("exercise 6.17")
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))
    print()

    print("exercise 6.18")
    test(f2c(212) == 100)     # Boiling point of water
    test(f2c(32) == 0)        # Freezing point of water
    test(f2c(-40) == -40)     # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)
    print()

    print("exercise 6.19")
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)


test_suite()
