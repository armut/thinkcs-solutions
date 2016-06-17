# exercise 5.2

def num_to_day(num_of_the_day):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday"]
    return days[num_of_the_day]


start_day = input("Please enter the starting day: ")
stay_amount = input("How many days will you stay?: ")
return_day = int((start_day + stay_amount)) % 7

print("You will return on ", num_to_day(return_day))
