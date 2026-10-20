print("Welcome to the hogwarts Sorting Hat")

trait = input("What best describes you? (bravery, intelligence, loyalty, ambition): ").lower

if trait ==  "brave":
    print("You belong in Gryffindor!")

elif trait == "intelligent":
    print("You belong in Ravenclaw!")

elif trait == "loyal":
    print("You belong in Hufflepuff!")

elif trait == "ambitious":
    print("You belong in Slytherin!")

elif trait == "hungry":
    print("You belong in the kitchen!")

else:
    print("The Sorting hat is confused.")

brave = input("Are you brave? (yes or no): ").lower()
intelligent = input("Are you intelligent? (yes or no): ").lower()

if brave == "yes" and intelligent == "yes":
    print("You belong in Gryffindor or Ravenclaw!")

tired = False
trait = input("What best describes you? (bravery, intelligence, loyalty, ambition): ").lower()
if (trait ==  "brave" or trait == "daring") and not tired:
    print("You belong in Gryffindor!")

bravery = int(input("On a scale of 1-10, how brave are you? "))
loyalty = int(input("On a scale of 1-10, how loyal are you? "))

if bravery > 7 and loyalty >= 5:
    print("You belong in Gryffindor or Hufflepuff!")