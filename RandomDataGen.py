import numpy as np
import math

DataSet = open("randomDataSet.csv", 'w')
DataSet.write("Type, Score, NormScore\n")


def generate_rand_data():
    score = round((2 * np.random.random_sample() - 1), 7)
    typ = 0
    if score > 0:
        typ = 1
    elif score < 0:
        typ = -1
    norm = round(math.exp(score), 7)
    op = str(typ) + "," + str(score) + "," + str(norm) + "\n"
    DataSet.write(op)

for i in range(0, 10000, 1):
    generate_rand_data()

DataSet.close()
