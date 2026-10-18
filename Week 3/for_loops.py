#Task 7
# #Ask user how mountains how many mountains to display and store the int.
# print("How many mountains should I display?")
# mountains_to_display = int(input())
#
# for _ in range(mountains_to_display):
#     print("          __ ")
#     print("         / \\_  ")
#     print("      _ /  ^ \\  ")
#     print("     /  ^     \\  ")
#     print("    /      ^   \\  ")




# Task 8
print( "How far are we from the target?")
number_of_steps = int(input())

for _ in range(number_of_steps):
    print(f"{number_of_steps} step(s) remaining")
    number_of_steps = number_of_steps - 1
print("Target Achieved!")