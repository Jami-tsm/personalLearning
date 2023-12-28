"""
Name:
Date:
Description:
"""


def fizzBuzz():
    """
    This function prints a string that contains fizz or buzz depending
    on whether the number is divisible by three or five or divisible by both
    :param
    :return: None
    """
    for i in range(100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def main():
    fizzBuzz()


if __name__ == "__main__":
    main()
