"""
Brother Alex Bedino

file_name =  tire_volume.py

Scope = calculate the volume of a tire

"""
# importing the math libary so we can use pi with all its decimals
import math

print (f"This program calculates the volume of a tire")

width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# tire volume formula
volume = math.pi * width**2 * aspect * (width*aspect + 2540*diameter) / 10000000000

# using the following function to round the tire volume to 2 decimals 
volume =  round(volume, 2)

# printing the final result
print (f"The approximate volume is {volume} liters")