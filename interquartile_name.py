X = [3, 7, 8, 5, 12, 14, 21, 13, 18]


def interquartile_range(values):

    lenght = len(values)
    percent_1 = lenght/100
    first_q = percent_1 * 25
    third_q = percent_1 * 75
    interquartile_range_value = len(values[int(first_q):int(third_q)])

    return interquartile_range_value


if __name__ == "__main__":
    print(interquartile_range(X))
