def divide1(int1, int2):
    """
    divides two integers
    :param int1:
    :param int2:
    :return:
    """
    result = (int1 // int2)
    return result


def remainder1(int3, int4):
    """
    finds the remainder of two divided integers
    :param int3:
    :param int4:
    :return:
    """
    result1 = (int3 % int4)
    return result1


def base_conversion(dest_base, base10):
    """
    converts the base 10 to the destination base
    :param dest_base:
    :param base10:
    :return:
    """
    first1 = divide1(base10, dest_base)
    remainder2 = remainder1(base10, dest_base)
    second1 = divide1(first1, dest_base)
    remainder3 = remainder1(first1, dest_base)
    third1 = divide1(second1, dest_base)
    remainder4 = remainder1(second1, dest_base)
    fourth1 = divide1(third1, dest_base)
    remainder5 = remainder1(third1, dest_base)
    fifth1 = divide1(fourth1, dest_base)
    remainder6 = remainder1(fourth1, dest_base)
    answer = (str(remainder5) + str(remainder4) + str(remainder3) + str(remainder2))
    if dest_base > 9:
        return -1
    if remainder6 > 0:
        return -1
    elif fifth1 > 0:
        return -1
    else:
        return answer


def main():
    """
    tests the function above
    :return:
    """
    base_10 = 10
    dest_base = 2
    result = base_conversion(dest_base, base_10)
    print(result)

    base_10 = 16
    dest_base = 2
    result = base_conversion(dest_base, base_10)
    print(result)

    base_10 = 10
    dest_base = 11
    result = base_conversion(dest_base, base_10)
    print(result)


if __name__ == "__main__":
    main()