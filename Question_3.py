import random


def create_name(length):
    """
    gives a list of letters to choose from, and depending on the length, generates a "name" from the list.
    joins str0 and alphabet
    :param length:
    :return:
    """
    alphabet = random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                              's', 't', 'u', 'v', 'w' 'x', 'y', 'z'], k = length)
    str0 = ""
    if length < 1:
        return None
    return str0.join(alphabet)


def main():
    """
    tests the function above
    :return:
    """
    length = 6
    result = create_name(length)
    print(result)

    length = 10
    result = create_name(length)
    print(result)


if __name__ == '__main__':
    main()
