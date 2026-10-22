# #Task 3
# #Define a function
# def listen():
#     print("Enter the word that represents the sound")
#     #Store user input in sound
#     sound = input("")
#     #print (sound)
#     print(f"That was a loud {sound}!")
# #Call the function
# listen()




# #Task 4
# def identity():
#     word = input("What do you see?")
#     if word == "a large boulder":
#         print("It's time to run!")
#     else:
#         print("We will be fine.")
# identity()




# Task 5
def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")
escape_by(plan = input("Enter a plan: "))