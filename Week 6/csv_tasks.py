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


# # Task 6
# import csv
#
#
# def extract(filepath):
#     print("Extracting...", end=" ")
#     with open(filepath, "r") as file_data:
#         data = csv.reader(file_data)
#         next(data)
#         names = ""
#         for line in data:
#             names += f"{line[1]}\n"
#     print("Done!")
#     print(f"The extracted items are:\n{names}")
#
#
# def run_task2():
#     extract("clothing.csv")
#
#
# if __name__ == "__main__":
#     run_task2()


# Task 7
import csv


def export(filepath, export_items):
    print("Exporting...")
    with open(filepath, 'a') as data_file:
        for i in range(export_items):
            item_id = int(input("Enter item ID: "))
            item_name = input("Enter item name: ")
            item_color = input("Enter item color: ")
            data = f"{item_id},{item_name},{item_color}\n"
            data_file.write(data)
    print("Done!")


def run_task7():
    export("exported_items.csv", 2)


if __name__ == "__main__":
    run_task7()
