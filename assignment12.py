'''
Brother Alex Bedino

File_name = assignment12.py

Goal = read data from a csv file and display results

'''
max_age = 0
min_age = 130
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
        else:
            continue
        if age < min_age:
            min_age = age
        else:
            continue

print (f"Result:")
print (f"The max recorded age in the whole database is {max_age}")
print (f"The min recorded age in the whole database is {min_age}")