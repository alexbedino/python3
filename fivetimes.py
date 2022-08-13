print("My name is")

for i in range (5):
    print('Jimmy Five times ('+str(i)+')')


total = 0
for num in range(101):
    total = total + num
print (total)

print("My name is")
i = 0
while i < 5:
    print("Jimmy Five times ("+str(i)+")")
    i = i + 1

for i in range(12, 26):
    print(i)

for i in range(0,10,2): # The step is the amount that the variable is increased by after each iteration.
    print(i)

for i in range (5,-1,-1): #you can even use a negative number for the step argument to make the for loop count down instead of up
    print(i)