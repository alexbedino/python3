'''
Brother Alex Bedino

File_name = assignment12.py

Goal = read data from a csv file and display results

'''
max_age = 0
min_age = 130
max_country = ()
min_country = ()
print (f"Reading database data...")
with open("life-expectancy.csv") as life_data:
    for line in life_data:
        new_line = line.split(",")
        country = new_line[0]   # country 
        country_abb = new_line[1]   # country abbreviation
        year = float(new_line[2])   # year
        age = float(new_line[3])    # age
        if age > max_age:
            max_age = age
            max_country = country
        elif age < min_age:
            min_age = age
            min_country = country
        else:
            continue

print (f"Result:")
print (f"The max recorded age in the whole database is for {max_country} and it is {max_age}")
print (f"The min recorded age in the whole database is for {min_country} and it is {min_age}")
