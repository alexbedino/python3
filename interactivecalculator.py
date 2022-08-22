print ("*"*100)
print ()

a = int(input("Input first value: "))
b = int(input("Input second value: "))

product = a*b

print (f"The result is {product}")
print ()
print ("*"*100)
print ()
age = int(input("How old are you? "))

total_age_days = age*365
total_age_hours = age*365*24
total_age_minutes = age*365*24*60

print (f"You are {total_age_days} days old, {total_age_hours} hours old, {total_age_minutes} minutes old")
print ()
print ("*"*100)
print ()
print ("---TIP CALCULATOR---")
price = float(input("What is the price? "))
tip_percentage = float(input("How much(in percentage) do you want to tip? "))
tip = (price * tip_percentage)/100
print (f"If you want to tip {tip_percentage}% you will need to give the waiter {round(tip, 2)}$")
print()
print ("*"*100)