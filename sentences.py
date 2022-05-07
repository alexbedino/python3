import random


def main():

    together(1,1,1,"past")
    together(1,1,1,"present")
    together(1,1,1,"future")
    together(2,2,2,"past")
    together(2,2,2,"present")
    together(2,2,2,"future")


def get_determiner(quantity):
# Create a list of strings and assign
# the list to a variable named determiners.
    if quantity == 1:
        words = ["A", "One", "The"]
    else:
        words = ["Two", "Some", "Many", "The"]
# Call the random.choice function which will choose
# one string from the words list. Store the chosen
# string in a variable named determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
# Create a list of strings and assign
# the list to a variable named nouns.
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "childs","dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
# Create a list of strings and assign
# the list to a variable named verbs.
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    
    verb = random.choice(verbs)
    return verb

def together(det_qty, noun_qty, verb_qty, tns):
    # this function puts together the three elements and allows to re-iterate them adding proper arguments

    determiner = get_determiner(det_qty)
    noun = get_noun(noun_qty)
    verb = get_verb(verb_qty, tns)

    print (f"{determiner} {noun} {verb}")

main()