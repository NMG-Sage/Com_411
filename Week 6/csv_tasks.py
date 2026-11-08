# Task 5
# import csv
#
#
# def read(filepath):
#     with open(filepath) as csvfile:
#         data = csv.reader(csvfile)
#         print(f"Headings:\n{next(data)}")
#         print("Values:")
#         for value in data:
#             print(value)
#
#
# def run_task5():
#     read("clothing.csv")
#
#
# if __name__ == "__main__":
#     run_task5()


# Task 6
import csv


def extract(filepath):
    print("Extracting...", end=" ")
    with open(filepath, "r") as file_data:
        data = csv.reader(file_data)
        next(data)
        names = ""
        for line in data:
            names += f"{line[1]}\n"
    print("Done!")
    print(f"The extracted items are:\n{names}")


def run_task2():
    extract("clothing.csv")


if __name__ == "__main__":
    run_task2()

