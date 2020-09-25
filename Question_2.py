import random


def roll_die(number_of_rolls, number_of_sides):
    """
    calculates the minimum and maximum possible numbers one could role with the parameters, and chooses a random
    number from that range
    :param number_of_rolls:
    :param number_of_sides:
    :return:
    """
    max_number = (number_of_rolls * number_of_sides)
    total = random.randrange(number_of_rolls, max_number)
    return total


def main():
    """
    tests the function above
    :return:
    """
    number_of_rolls = 2
    number_of_sides = 6
    result = roll_die(number_of_rolls, number_of_sides)
    print(result)

    number_of_rolls = 5
    number_of_sides = 12
    result = roll_die(number_of_rolls, number_of_sides)
    print(result)


if __name__ == "__main__":
    main()