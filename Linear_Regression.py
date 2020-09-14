# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def read_input():
    F, N = map(int,input().split(' '))

    # For Data set rows:
    Rows = []
    [Rows.append(list(map(np.float64, input("\nEnter the numbers for N : ").strip().split()))) for _ in range(0,N)]

    df = pd.DataFrame(Rows)
    T = int(input("\nEnter the T : "))
    Rows_2 = []
    [Rows_2.append(list(map(np.float64, input("\nEnter the numbers for T : ").strip().split()))) for _ in range(0,T)]

    # Building Dataframe
    df = df.append(pd.DataFrame(Rows_2), ignore_index=True)
    df = df.fillna(0)
    X = df.iloc[:,:-1]
    y = df.iloc[:,-1:]

    X_train = df.iloc[:N, :-1]
    y_train = df.iloc[:N, -1:]

    X_test = df.iloc[N:, :-1]
    y_test = df.iloc[N:, -1:]

    return X_train, y_train, X_test, y_test


def LR(X_train, y_train, X_test):
    # Train Test Split

    # Linear Regression
    clf = LinearRegression()
    clf.fit(X_train, y_train)
    Y_test = clf.predict(X_test)
    return Y_test


def main():
    X_train, y_train, X_test, y_test = read_input()
    result = LR(X_train, y_train, X_test)
    result = [elem[0] for elem in result]
    return result


if __name__ == '__main__':
    prediction = main()
    print(prediction)





E_C = []
T = 2
for i in range(1):
    Prob_Die = [0.32,0.32,0.12,0.04,0.07,0.13]
    N_Ladders, N_Snakes = 3, 7
    Ladders = [[32,62], [42,68], [12,98]]
    Snakes = [[95,13], [97,25], [93,37],[79,27], [75,19], [49,47], [67,17]]

    # Ladder_Dict
    CP_L = [_[0] for _ in Ladders]
    GT_L = [_[1] for _ in Ladders]
    D_L = {}
    for i in range(N_Ladders):
        D_L[CP_L[i]] = GT_L[i]

    # Snake_Dict
    CP_s = [_[0] for _ in Snakes]
    GT_s = [_[1] for _ in Snakes]
    D_s = {}
    for i in range(N_Snakes):
        D_s[CP_s[i]] = GT_s[i]

    # Determining roll based on max probability
    Die = [_ for _ in range(1, 7)]
    m = Prob_Die.index(max(Prob_Die))
    Roll = Die[m]

    # Calculating expected number of moves to complete the game

    E_C = []
    total = 0

    for i in range(5000):
        win = True
        current = 0
        moves = 0

        while win:

            for k, v in D_L.items():
                if current == k:
                    current += D_L[current]

            for k, v in D_s.items():
                if current == k:
                    current -= D_s[current]

            if not (current + Roll > 100):
                current += Roll
                moves += 1

            if current == 100:
                win = False
                total += 1

            if moves == 1000:
                break

        E_C.append(moves)

print(round(sum(E_C) / total))
