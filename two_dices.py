

n_faces = 6

def throw(n_faces=6):
    max_value = input("Insert a value, i'll give you the probability of "
          "getting a number lower than that with {} dices".format(2))
    faces = [x for x in range(1, n_faces+1)]
    values = []
    for face1 in range(1, n_faces+1):
        for face2 in range(1, n_faces+1):
            values.append(face1+face2)

    good_ones = [x for x in values if x < int(max_value)]
    return round(len(good_ones)/36*100, 2)


if __name__ == "__main__":
    print(throw(n_faces), "% of probability")
