# #Task 3
# #Define a function
# def listen():
#     print("Enter the word that represents the sound")
#     #Store user input in a variable
#     sound = input("")
#     #print (sound)
#     print(f"That was a loud {sound}!")
# #Call the function
# listen()


# # Task 4
# def identity():
#     word = input("What do you see?")
#     if word == "a large boulder":
#         print("It's time to run!")
#     else:
#         print("We will be fine.")
# identity()


# # Task 5
# #Define the function and add a parameter or more if needed
# def escape_by(plan):
#     if plan == "jumping over":
#         print("We cannot escape that way! The boulder is too big!")
#     elif plan == "running around":
#         print("We cannot escape that way! The boulder is moving too fast!")
#     elif plan == "cross bridge ahead":
#         print("That might just work! Let's go!")
#     else:
#         print("We cannot escape that way! The boulder is in the way!")
# #Call the function and place the parameter in the brackets, which also asks for the user input
# escape_by(plan = input("Enter a plan: "))


# # Task 6
# def cross_bridge(steps_crossed):
#     for step in range (steps_crossed):
#         print("Crossed step.")
#
#     if steps_crossed > 5:
#         print("The bridge is collapsing!")
#     else:
#         print("We must keep going!")
#
# cross_bridge(steps_crossed = int(input("Enter the number of steps: ")))


# # Task 7
def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


climb_ladder(5, 2)
climb_ladder(2, 5)
