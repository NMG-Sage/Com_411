# Task 1
# import os
#
#
# def cwd_path():
#     path = os.getcwd()
#     print(f"The current working directory is {path}")
#     print("The directory contains the following files:")
#     print(os.listdir(path))
#
#
# def run():
#     print("Processing...")
#     cwd_path()
#
#
# if __name__ == "__main__":
#     run()


# Task 2
# def display_chars(file_path=input("Enter file path: "), num_char=int(input("Enter character numbers to display: "))):
#     with open(file_path, "r") as file:
#         data = file.read(num_char)
#         print(data)
#
#
# def display_line(file_path=input("Enter the file path: ")):
#     with open(file_path, "r") as file:
#         data = file.readline().strip()
#         print(data)
#
#
# def display_text(file_path=input("Enter the file path: ")):
#     with open(file_path, "r") as file:
#         data = file.read()
#         print(data)
#
#
# def run():
#     print("The first chosen characters are: ")
#     display_chars()
#     print("The first line is : ")
#     display_line()
#     print("The full text is: ")
#     display_text()
#
#
# if __name__ == "__main__":
#     run()


# Task 3
# def search(file_name=input("Enter the file name: ")):
#     print("Searching...")
#     with open(file_name, "r") as file:
#         for line in file:
#             print(f"Looked in {line}")
#         print("...Done!")
#
#
# def run_task3():
#     search()
#
#
# if __name__ == "__main__":
#     run_task3()


# Task 4
def search_books(filename=input("Enter the file name: ")):
    print("Searching books...")
    sections = ""
    books = "Books:\n"
    with open(filename, "r") as file:
        for each_line in file:
            if each_line.startswith("Section"):
                sections += each_line
            else:
                books += each_line
    print("Done!")
    return f"\n{sections}\n\n{books}"


def save(filename=input("Enter the file name: "), user_input_add=input("Enter text: ")):
    print("Saving...")
    with open(filename, "w") as file:
        file.write(user_input_add)
        print("Done!")


def run_task4():
    data = search_books(filename=input("Enter the file name: "))
    save("exported_books.txt", data)


if __name__ == "__main__":
    run_task4()
