X = [10, 20, 30, 40, 50, 30, 40]
W = [3, 5, 6, 2, 4, 6, 7]


def weighted_mean(values, weights):

    total = 0
    for n, el in enumerate(values):
        total += values[n]*weights[n]

    return total/len(values)


if __name__ == "__main__":
    print(weighted_mean(X, W))
