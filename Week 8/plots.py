# # Task 1
# from matplotlib import pyplot as plt
#
#
# def display_line(x, y):
#     plt.scatter(x, y)
#     plt.show()
#
#
# def run_task1():
#     x_values = [1, 2, 3, 4, 5]
#     y_values = [1, 4, 9, 16, 25]
#     display_line(x_values, y_values)
#
#
# if __name__ == '__main__':
#     run_task1()


# # Task 2
# import matplotlib.pyplot as plt
#
#
# def small():
#     x = [4, 4, 6, 6, 4]
#     y = [4, 6, 6, 4, 4]
#     plt.plot(x, y, "o:")
#
#
# def medium():
#     x = [3, 3, 7, 7, 3]
#     y = [3, 7, 7, 3, 3]
#     plt.plot(x, y, "s--")
#
#
# def large():
#     x = [2, 2, 8, 8, 2]
#     y = [2, 8, 8, 2, 2]
#     plt.plot(x, y, "x-.")
#
#
# if __name__ == "__main__":
#     small()
#     medium()
#     large()
#     plt.show()


# # Task 3
# import matplotlib.pyplot as plt
#
#
# def coordinate():
#     x = int(input("Enter the x coordinate: "))
#     y = int(input("Enter the y coordinate: "))
#     return x, y
#
#
# def path():
#     print("Retrieving path...")
#     x_values = []
#     y_values = []
#     for i in range(4):
#         data = coordinate()
#         x_values.append(data[0])
#         y_values.append(data[1])
#     return x_values, y_values
#
#
# def run_task3():
#     values = path()
#     plt.plot(values[0], values[1], "or--")
#     plt.show()
#
#
# if __name__ == "__main__":
#     run_task3()


# Task 4
import matplotlib.pyplot as plt
import random as rnd

def data():
    paths = {}
    line_style = input("What line style would you like to use?")
    color = input("What color would you like for the line?")
    marker_style = input("What marker style would you like for the line?")
    paths['line_style'] = line_style
    paths['color'] = color
    paths['marker_style'] = marker_style
    return paths


def generate():
    line_amount = int(input("How many lines would you like to display?"))
    for i in range(line_amount):
        values = data()
        x_values = rnd.sample(range(1, 10), 5)
        y_values = rnd.sample(range(1, 10), 5)
        line_format = f"{values['line_style']}{values['color']}{values['marker_style']}"
        plt.plot(x_values, y_values, line_format)
    plt.show()


def run_task4():
    print("Running...")
    generate()
    print("Done!")


if __name__ == "__main__":
     run_task4()
