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
import csv


# Task 6
def extract(filepath):
    print("Extracting...", end=" ")
    with open(filepath) as file_data:
        csv_reader = csv.reader(file_data)
        next(csv_reader)
        names = ""
        for line in file_data:
            names += f"{line[1]}\n"
    print("Done!")
    print(f"The extracted items are:\n{names}")


def run_task2():
    extract("clothing.csv")


if __name__ == "__main__":
    run_task2()
