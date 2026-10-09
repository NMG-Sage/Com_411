cover_type = input("What is the cover type of the book?")

if cover_type == "soft":
    bond_type = input("Is the book a perfect bound?")
    if bond_type == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")
