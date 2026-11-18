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


# Task 2
import matplotlib.pyplot as plt


def small():
    x = [4, 4, 6, 6, 4]
    y = [4, 6, 6, 4, 4]
    plt.plot(x, y, "o:")


def medium():
    x = [3, 3, 7, 7, 3]
    y = [3, 7, 7, 3, 3]
    plt.plot(x, y, "s--")


def large():
    x = [2, 2, 8, 8, 2]
    y = [2, 8, 8, 2, 2]
    plt.plot(x, y, "x-.")


if __name__ == "__main__":
    small()
    medium()
    large()
    plt.show()
