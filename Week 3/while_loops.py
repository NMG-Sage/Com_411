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




#Task 3
print("How many bars should be charged?: ")
bars_input = int(input())
bars_charged = 0#
bars_charged_display = ("")
while bars_charged < bars_input:
    print("Charging:", end=" ")
    bars_charged += 1
    bars_charged_display += ("█")
    print(f"{bars_charged_display}", end=" ")
    print(f"{bars_charged}%")
