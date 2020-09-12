from sys import exit


def gold_room():
    print("The room is full of gold.  How much do you take?")

    choice = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    #else:
     #   dead("Type a number. ")

    elif how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    elif how_much > 50:
        print("You're greedy")
        exit(0)
    else:
        dead("You're greedy")


def bear_room():
    print("There is a bear here")
    print("The bear has honey")
    print("The bear is in front of another door")
    print("How are you going to move the bear")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear slaps you")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door")
            print("You can go through it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed and chews your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("What does that mean")


def cthulhu_room():
    print("Here is Cthulhu")
    print("If it stares at you, you're done")
    print("Do you flee or eat yourself")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "eat" in choice:
        dead("Well that was tasty")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good Job")
    exit(0)


def start():
    print("You are in a dark room")
    print("There is a door to your right and left")
    print("Which one do you take")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You didn't choose")


start()
