# # Task 5
# def likelihood():
#     likelihoods = (50, 38, 27, 99, 4)
#     return min(likelihoods)
#
#
# def run_task5():
#     likelihood_run_task5_local = likelihood()
#     print(f"Minimum likelihood of falling: {likelihood_run_task5_local}%")
#
#
# if __name__ == "__main__":
#     run_task5()


# # Task 6
# def likelihood_min_max():
#     likelihoods = (50, 38, 27, 99, 4)
#     return min(likelihoods), max(likelihoods)
#
#
# def run_task6():
#     likelihood_min, likelihood_max = likelihood_min_max()
#     print(f"Minimum likelihood of falling: {likelihood_min}%\nMaximum likelihood of falling: {likelihood_max}%")
#
#
# if __name__ == "__main__":
#     run_task6()


# Task 7
def steps():
    all_steps = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return all_steps


def run_task7():
    all_steps = steps()
    good_steps = []
    bad_steps = []
    for step in all_steps:
        if step[1] >= 50:
            bad_steps.append(step)
        else:
            good_steps.append(step)
    print(f"Good steps: {good_steps}\nBad steps: {bad_steps}")


if __name__ == "__main__":
    run_task7()
