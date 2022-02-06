decision = input("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?")

if decision.lower() == ("match"):
    match = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated \nYou see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ")
    if match.lower() == ("run"):
        print ("The bear is considerably faster and takes you down with its paws devouring you")
    else:
        print ("The forest is scary but the bear's sight is not the best. You are able to hide successfully, waiting until dawn might actually save your life")

else:
    flashlight = input("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. \nDo you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")
    if flashlight.lower() == ("follow"):
        print ("the path leads to a beutiful garden where you pick flowers, you are safe")
    else:
        print ("Behind the bushes a bear lurks and when it sees you he immediately jumps killing you on the spot")
