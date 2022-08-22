from datetime import date
current_year = date.today().year

name = input("What is your name? ")

print (f"Hello, {name}!")

year_birth = input("What is your birth year? ")
print(f"You were born in {year_birth}")

name = input("What is your name? ")

print (f"Hello, {name}!")

year_birth = int(input("What is your birth year? "))

print (f"You are {current_year-year_birth} years old.")