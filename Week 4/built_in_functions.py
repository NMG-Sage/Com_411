print("Program Started!")
print("Please enter a standard character:")
user_input_char = input("")

if len(user_input_char) == 1:
    print(f"The ASCII code for {user_input_char} is {ord(user_input_char)}")
else:
    print("A single character was expected.")
print("Program Ended!")