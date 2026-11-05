import os


def cwd_path():
    path = os.getcwd()
    print(rf"The current working directory is {path}")
    print("The directory contains the following files:")
    print(os.listdir(path))


def run():
    print("Processing...")
    cwd_path()


if __name__ == "__main__":
    run()
