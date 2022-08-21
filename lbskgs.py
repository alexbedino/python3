import math 

print ("." * 100)

print ("Let's start the project")
print ("Convert from kgs to lbs")
print ("lbs = kgs * 2.2046")

kgs = float(input("How many kgs do you have? "))
lbs = kgs*2.2046

print (f"Your weight is {lbs} lbs")

print ("." * 100)

print ("Calculate the circumference of a circle given the radius")
print ("Given the circumference formula c = 2*pi*r")

r = float(input("What is the radius of the circle? "))

c =  (2*math.pi*r)

c = round(c, 2) # rounding to only 2 decimals

print (f"The circumference of your circle is {c}")
print ("." * 100)

print ("." * 100)

print ("Assign a number to a variable, multiply by 3, add 6, divide by 3, subtract by the first number, the answer is 2 ")

a = int(input("Give me a number, the answer will always be two! "))

def twoformula(a):
    b = ((((a*3)+6)/3)-a)
    return int(b) #answer is always 2

print (twoformula(a))
print ("." * 100)
