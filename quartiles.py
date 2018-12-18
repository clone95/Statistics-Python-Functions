X = [3, 7, 8, 5, 12, 14, 21, 13, 18]


def quartiles(values):

    lenght = len(values)
    percent_1 = lenght/100
    first_q = percent_1 * 25
    second_q = percent_1 * 50
    third_q = percent_1 * 75

    return [values[int(first_q)], values[int(second_q)], values[int(third_q)]]


if __name__ == "__main__":
    print(quartiles(X))
