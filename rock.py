import random

def play():
    user = input("What's your choice? \n 'r' for rock, 'p' for paper, 's' scissors? ")
    computer = random.choice(['r', 'p', 's'])
    print (f"computer choice is {computer}")

    if user == computer:
        return "It's a tie"
    # r > s, s > p, p > r

    if is_win(user, computer):
        return "You won!"

    # we get to this line if the previous are false anyway 
    return "You lost"


def is_win(player, opponent):
    #return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 's'):
        return True

print (play())
