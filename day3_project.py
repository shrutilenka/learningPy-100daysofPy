print("Welcome to Treasure Island.Your mission is to find the treasure")
lr = input("Your options are left or right: ")
if lr == "left":
    sw = input("swim or wait: ")
    if sw == "wait":
        door = input("which door? red, blue or yellow: ")
        if door == "red":
            print("burned by fire")
        elif door == "blue":
            print("eaten by beasts")
        elif door == "yellow":
            print("you win")
        else:
            print("game over")
    if sw == "swim":
        print("Attacked by trout.Game Over.")
    else:
        print("game over")
else:
    print("fall into a hole.Game Over.")
