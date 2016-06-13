#exercise 5.1

def num_to_day(num_of_the_day):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday"]
    return days[num_of_the_day]


day_number =  input("Please insert the number of the day: ")
print(num_to_day(int(day_number)))
