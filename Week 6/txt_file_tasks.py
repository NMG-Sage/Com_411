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
def search(file_name=input("Enter the file name: ")):
    print("Searching...")
    with open(file_name, "r") as file:
        for line in file:
            print(f"Looked in {line}")
        print("...Done!")


def run_task3():
    search()


if __name__ == "__main__":
    run_task3()
