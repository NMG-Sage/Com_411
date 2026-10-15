#Classify books
#
# cover_type = input("What is the cover type of the book?")
#
# if cover_type == "soft":
#     bond_type = input("Is the book a perfect bound?")
#     if bond_type == "yes":
#         print("Soft cover, perfect bound books are very popular!")
#     else:
#         print("Soft covers with coils or stitches are great for short books")
# else:
#     print("Books with hard covers can be more expensive!")


#Find Phone
place = input("Where should I look?")
if place == "bedroom":
    bedroom = input("Where in the bedroom should I look?")
    if bedroom == "under the bed":
        print("Found some shoes but no phone!")
    else:
        print("Found some mess but no phone.")
elif place == "bathroom":
    bathroom = input("Where in the bathroom should I look?")
    if bathroom == "in the bathtub":
        print("Found a rubber duck but no phone!")
    else:
        print("Found bathroom stuff but no phone.")
elif place == "living room":
    living_room = input("Where in the living room should I look?")
    if living_room == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")
else:
    print("I do not know where that is but I will keep looking.")

