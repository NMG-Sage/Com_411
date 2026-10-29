# Task 5
def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run_task5():
    likelihood_run_task5_local = likelihood()
    print(f"Minimum likelihood of falling: {likelihood_run_task5_local}%")


if __name__ == "__main__":
    run_task5()
