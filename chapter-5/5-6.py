# exercise 5.6

def mark_to_grade(mark):
    """Converts 6exam mark to grade for that."""
    if mark >= 75:
        return "First"
    elif mark >= 70 and mark < 75:
        return "Upper Second"
    elif mark >= 60 and mark < 70:
        return "Second"
    elif mark >= 50 and mark < 60:
        return "Third"
    elif mark >= 45 and mark < 50:
        return "F1 Supp"
    elif mark >= 40 and mark < 45:
        return "F2"
    elif mark < 40:
        return "F3"


test_data = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
             49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in test_data:
    print(mark_to_grade(i))
    
