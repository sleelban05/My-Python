x = 10
y = 20
if x < y and x == 20:
    print("TRUE")
else:
    print("FALSE")

pi = 3.142
radius = 12
area = pi * radius
if area < 1000:
    print("this is a big circle")
else:
    print("This is a big circle")

principle = 2000
rate = 5
time = 3
interest = (principle * rate * time) / 100
if interest < 500:
    print("The loan is affordable")
elif interest < 1500:
    print("The loan is expensive")
else:
    print("The loan is a scam")


weight = 49
height = 2.0
BMI = weight / height * height
if BMI < 18:
    print("Underweight")
elif BMI >= 18.1 - 24:
    print("Normal weight")
elif BMI >= 24.1 - 29:
    print("Overweight")
elif BMI >= 29.1:
    print("Obese")


# GRADING SYSTEM
mark = 62
if mark < 40:
    print("D")
elif mark < 50:
    print("C")
elif mark < 60:
    print("B")
else:
    print("A")

# Grading system
maths = 50
physics = 63
kiswahili = 72
chemistry = 67
computerstudies = 84
history = 84
english = 71
marks = (maths + physics + kiswahili + chemistry + computerstudies + history + english) / 7
name = ("Leelban")
if marks < 40:
    print("Hello",name,"Your marks are",marks,"E")
elif marks < 50:
    print("Hello",name,"Your marks are",marks,"D")
elif marks < 60:
    print("Hello",name,"Your marks are",marks,"C")
elif marks < 70:
    print("Hello",name,"Your marks are",marks,"B")
else:
    print("Hello",name,"Your marks are",marks,"A")


a = 10
b = 20
if a > b:
    if b > 20:
        print("TRUE")
    else:
        print("FALSE")
else:
    if a < b:
        print("SECOND TRUE")
    else:
        print("SECOND FALSE")


# Given three variables "ageOne, ageTwo, age three"
# containing integer values, write efficient
# python statements to satisfy the following conditions
# 1. If ageOne is greater than ageTwo, proceed to check
# the following conditions on ageThree variable
#   i. if ageThree is greater than 18, display a
#   welcome message. Else, display a goodbye message
# 2. If ageOne is less than ageTwo, proceed to check
# the following conditions on ageThree variable
#   i. if ageThree is greater than 15, display a
#   welcome message. Else, display a goodbye message.

ageThree = 19
ageTwo = 16
ageOne = 23

if ageOne > ageTwo:
    if ageThree > 18:
        print("WELCOME")
    else:
        print("GOODBYE")
else:
    if ageOne < ageTwo:
        if ageThree < 15:
            print("WELCOME")
        else:
            print("GOODBYE")