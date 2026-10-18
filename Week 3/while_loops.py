#Task 1
# #Declare a variable and store user input
# removed_apples = input("Please enter apples to be removed:")
# #Set up while loop to read the user input as int and print the output message*{user variable}
# for removed_apples in range(int(removed_apples)):
#     print("Apples are removed")




# #Task 2
# #Ask user to enter obstacles to be avoided  and store value
# print("How many obstacles must I avoid?")
# obstacles = int(input(""))
# #create variable to store iteration sequence number
# obstacles_avoided = 0
# ##check if the iteration number is still smaller than the user input
# while obstacles_avoided < obstacles:
#     #end parameter used to prevent going to next line
#     print("Avoiding...", end="")
#     #Add 1 to the iteration variable
#     obstacles_avoided += 1
#     print(f"...Done! {obstacles_avoided} avoided!")
# print("All obstacles have been avoided!")




# #Task 3
# print("How many bars should be charged?: ")
# bars_input = int(input())
# bars_charged = 0
# bars_charged_display = ("")
# while bars_charged < bars_input:
#     print("Charging:", end=" ")
#     bars_charged += 1
#     bars_charged_display += ("█")
#     print(f"{bars_charged_display}", end=" ")
#     print(f"{bars_charged}%")




# #Task 4
# print("Please enter phrase")
# phrase = input("")
# for letter in phrase:
#     print("Hi", end=" ")




# #Task 5
# print("Calculating the sum of the first 100 numbers...", end="")
# print(f"...Done! The answer is {sum(range(101))}")




#Task 6
# Ask user for number
print("How many numbers should I sum up?")
number_to_sum = int(input())

# Declare a control variable
summed = 0

# Display blank line

print()

# Sum numbers

total = 0

while summed < number_to_sum:
    print(f"Please enter number {summed+1} of {number_to_sum}:")
    number = int(input())
    total = total + number
    summed = summed + 1

# Display result
print(f"The answer is {total}.")
