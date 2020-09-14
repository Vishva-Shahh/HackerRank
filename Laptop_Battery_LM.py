#!/bin/python

import math
import os
import random
import re
import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from matplotlib import pyplot
import pylab

data = pylab.loadtxt('trainingdata.txt', delimiter=',')
x = data[:, 0]
y = data[:, 1]

pyplot.scatter(x, y)
pyplot.title('Fred\'s Battery Life')
pyplot.xlabel('Charged time (h)')
pyplot.ylabel('Laptop usage (h)')
pyplot.grid()
pyplot.show()


def Input_Fit():
    df = pd.read_csv("trainingdata.txt", header=None)
    X_train = df[[0]]
    y_train = df[[1]]
    clf = LinearRegression()
    model = clf.fit(X_train, y_train)
    return model


def raw_input():
    n = input()
    return n


def main():
    model = Input_Fit()
    prediction = model.predict([[timeCharged]])
    return prediction[0]


if __name__ == '__main__':
    timeCharged = float(raw_input())
    print("{0:.2f}".format(min(timeCharged * 2, 8)))