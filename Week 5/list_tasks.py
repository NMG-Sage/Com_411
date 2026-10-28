# # Task 1
# def directions():
#     steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
#     return steps
#
#
# def run_task1():
#     output = directions()
#     print(output)
#
#
# if __name__ == "__main__":
#     run_task1()


# # Task 2
# def movements():
#     path = ["Move Forward", 10,  "Move Backward", 5, "Move Left", 3, "Move Right", 1]
#     return path
#
#
# def run_task2():
#     print("Moving. . .")
#     direction = movements()
#     print(f"{direction[0]} for {direction[1]} steps")
#     print(f"{direction[2]} for {direction[3]} steps")
#     print(f"{direction[4]} for {direction[5]} steps")
#     print(f"{direction[6]} for {direction[7]} steps")
#
#
# if __name__ == "__main__":
#     run_task2()


# # Task 3
# def directions():
#     directions_list = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
#     return directions_list
#
#
# def menu():
#     print("Please select a direction:")
#     called_directions = directions()
#     for direction in range(len(called_directions)):
#         print(f"{direction}: {called_directions[direction]}")
#
#
# def run_task3():
#     menu()
#
#
# if __name__ == "__main__":
#     run_task3()


# Task 4
def directions():
    steps = ["Forward", "Backward", "Left", "Right"]
    return steps


def menu_and_input():
    print("Please select a direction:")
    menu_directions = directions()
    for direction in range(len(menu_directions)):
        print(f"{direction} : {menu_directions[direction]}")
    user_choice = input("> ")
    return user_choice


def run_task4():
    route = [""]
    print("Working out escape route...")
    for i in range(5):
        route.append(menu_and_input())
    print(f"Escape route: {route}")


if __name__ == "__main__":
    run_task4()
