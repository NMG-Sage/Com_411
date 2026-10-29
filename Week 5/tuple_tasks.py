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


# Task 6
def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run_task6():
    likelihood_min, likelihood_max = likelihood_min_max()
    print(f"Minimum likelihood of falling: {likelihood_min}%\nMaximum likelihood of falling: {likelihood_max}%")


if __name__ == "__main__":
    run_task6()
