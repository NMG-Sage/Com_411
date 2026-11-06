# Task 5
import csv


def read(filepath):
    with open(filepath) as csvfile:
        data = csv.reader(csvfile)
        print(f"Headings:\n{next(data)}")
        print("Values:")
        for value in data:
            print(value)


def run_task5():
    read("clothing.csv")


if __name__ == "__main__":
    run_task5()
