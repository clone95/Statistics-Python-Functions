import statistics as st
import math as mh
X = [3, 7, 8, 5, 12, 14, 21, 13, 18]


def standard_deviation(values):

    mean = st.mean(values)
    variance = sum([(x - mean)**2 for x in values])/(len(values)-1)
    std = mh.sqrt(variance)

    return std


if __name__ == "__main__":
    print(standard_deviation(X))
