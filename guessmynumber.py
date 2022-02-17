while True:
    import random # importing library

    magic_n = random.randint(1, 10) #setting the magic number to random
    guess = int(input("What is your guess? ")) #asking the user to input the guess number
    num_guess = (1)
    
    while guess != magic_n: #starting the loop, it will take in any case that the guess is different from the magic number
        
        while guess > magic_n: #first loop, will take in any case that the guess number is higher than the magic
            print ("lower")
            guess = int(input("What is your guess? ")) #asking for new input, if the new number is still higher the secondary loop starts again
            num_guess = num_guess + 1
        while guess < magic_n: #second loop, will take in any case that the guess number is lower than the magic
            print ("higher")
            guess = int(input("What is your guess? "))
            num_guess = num_guess + 1

    print (f"You got it right, the number is {guess}. You got it with {num_guess} guesses.") # printing the answer
    
    check = input("Do you want to quit or start again? enter Y to restart or another key to end: ")
    if check.upper() == "Y": #go back to the top
        continue    
    print ("Bye...")
    break #exit
