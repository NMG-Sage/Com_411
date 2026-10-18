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




# # Task 8
# print( "How far are we from the target?")
# number_of_steps = int(input())
#
# for _ in range(number_of_steps):
#     print(f"{number_of_steps} step(s) remaining")
#     number_of_steps = number_of_steps - 1
# print("Target Achieved!")




# #Task 9
# print("What level of brightness is required?")
# brightness_desired = int(input())
#
# for brightness in range(2, brightness_desired + 1, 2):
#     print(f"Brightness level: {'*'* brightness}")
#     print(brightness)




# # Task 10
# # Ask user for word
# print("What word do you see?")
# word = input()
#
# print("\nDisplaying index positions...\n")
#
# for count in range(0, len(word), 1):
#     print(f"index {count}:", word[count])




# Task 11
print("What phrase do you want to see in reverse?")
reverse_phrase = input("")

for letter in reverse_phrase:
    print(letter[reverse_phrase], end="")