First_number = int(input("Please enter 1st number: "))
Second_number = int(input("Please enter 2nd number: "))
Third_number = int(input("Please enter 3rd number: "))

even_counter = 0
odd_counter = 0

if First_number % 2 == 0:
    even_counter += 1
else:
    odd_counter += 1

if Second_number % 2 == 0:
    even_counter += 1
else:
    odd_counter += 1

if Third_number % 2 == 0:
    even_counter += 1
else:
    odd_counter += 1

print(f"There are {odd_counter} odd and {even_counter} even")

#if First_number % 2 == 0 and Second_number % 2 == 0 and Third_number % 2 == 0:
#    print("There are 3 even numbers and 0 odd numbers.")
#elif First_number % 2 != 0 and Second_number % 2 != 0 and Third_number % 2 != 0:
#    print("There are 0 even numbers and 3 odd numbers.")

#elif First_number % 2 != 0 and Second_number % 2 == 0 and Third_number % 2 == 0:
#    print("There are 2 even numbers and 1 odd numbers.")
#elif First_number % 2 == 0 and Second_number % 2 != 0  and Third_number % 2 == 0:
#    print("There are 2 even numbers and 1 odd numbers.")
#elif First_number % 2 == 0 and Second_number % 2 == 0 and Third_number % 2 != 0:
#    print("There are 2 even numbers and 1 odd numbers.")

#elif First_number % 2 != 0 and Second_number % 2 != 0 and Third_number % 2 == 0:
#    print("There are 1 even numbers and 3 odd numbers.")
#elif First_number % 2 == 0 and Second_number % 2 != 0  and Third_number % 2 != 0:
#   print("There are 1 even numbers and 2 odd numbers.")
#elif First_number % 2 != 0 and Second_number % 2 == 0 and Third_number % 2 != 0:
#    print("There are 1 even numbers and 2 odd numbers.")