#Task 1
# #Declare a variable and store user input
# removed_apples = input("Please enter apples to be removed:")
# #Set up while loop to read the user input as int and print the output message*{user variable}
# for removed_apples in range(int(removed_apples)):
#     print("Apples are removed")


#Task 2
print("How many obstacles must I avoid?")
obstacles = int(input(""))
obstacles_avoided = 0
while obstacles_avoided < obstacles:
    print("Avoiding...", end="")
    obstacles_avoided += 1
    print(f"...Done! {obstacles_avoided} avoided!")
print("All obstacles have been avoided!")