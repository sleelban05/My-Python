# INBUILD FUNCTIONS
greeting = "     Hello world    "
print(greeting)
capital_greeting = greeting.upper()
print(capital_greeting)

lower_greeting = greeting.lower()
print(lower_greeting)

striped_greeting = greeting.strip()
print(striped_greeting)


number = -4
print(number)


absolute_number = abs(number)
print(absolute_number)


number_squared = pow(number, 2)
print(number_squared)

# CUSTOM / USER DEFINED FUNCTIONS
def motto():
    print("Hey, this is our motto")
motto()


def add_numbers():
    x = 20
    y = 30
    z = x + y
    print(z)

add_numbers()

def addition(x,y):
    z = x + y
    print("Hey, your answer is", z)

addition(20,40)
addition(450,900)

def  interest(p,r,t):
    interest = p * t * r / 100
    print(interest)
interest(1000,30,5)

# Create a function to calculate
# the BMI    of any person. use scale
# 0----- 18 ----underweight
# 18.1----29----normal weight
# 29.1----34----overweight
#  34.1 and above----obese

def BMI(w,h):
    BMI = w /pow(h,2)
    if BMI <= 18:
        print("Underweight")
    elif BMI <= 29:
        print("Normal weight")
    elif BMI <= 34:
        print("Overweight")
    else:
        print("Obese")

BMI(60,1.6)