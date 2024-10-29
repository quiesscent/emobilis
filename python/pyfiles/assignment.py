# grade  calculator
from statistics import mean

kiswahili = int(input("Enter kiswahili grade: "))
math = int(input("Enter math grade: "))
physics = int(input("Enter physics grade: "))

def compute(kiswahili, math, physics):

    if kiswahili < 0 or math < 0 or physics < 0:
        return f"Error in input"

    average = mean([ kiswahili, math, physics])
    # average = (kiswahili + math + physics ) / 3

    if average > 100:
        return f"Average invalid"

    else: 
        if average >= 0 and average <= 39:
            marks = "D"
        if average >= 40 and average <= 59:
            marks = "C"
        if average >= 60 and average <= 79:
            marks = "B"
        if average >= 80 and average <= 100:
            marks = "A"
        
        return f"Avg: {average:.2f} , Grade: { marks }"

print(compute(kiswahili, math, physics))