import random

def roll(massDist):
    randRoll = random.random() # in [0,1)
    sum = 0
    result = 1
    for mass in massDist:
        sum += mass
        if randRoll < sum:
            return result
        result+=1


T = int(input())    # Number of tests

# Probability of die & other inputs:
for i in range(0, T):
    Prob_Die = [float(a) for a in input().split(",")]
    N_Ladders, N_Snakes = map(int, input().split(","))
    Ladders = [[int(s) for s in line.split(",")] for line in input().split(" ")]
    Snakes = [[int(s) for s in line.split(",")] for line in input().split(" ")]

    # Ladder_Dict
    CP_L = [_[0] for _ in Ladders]
    GT_L = [_[1] for _ in Ladders]

    # Snake_Dict
    CP_s = [_[0] for _ in Snakes]
    GT_s = [_[1] for _ in Snakes]

    # Determining roll based on max probability
    Roll = roll(Prob_Die)

    # Calculating expected number of moves to complete the game

    E_C = []
    total = 0

    for i in range(5000):
        win = True
        current = 1
        moves = 0

        while win:
            Roll = roll(Prob_Die)

            if not (current + Roll > 100):
                current += Roll
            moves += 1

            if current in CP_L:
                current = GT_L[CP_L.index(current)]

            if current in CP_s:
                current = GT_s[CP_s.index(current)]

            if current == 100:
                win = False
                total += 1

            if moves == 1000:
                break
        E_C.append(moves)
    print(round(sum(E_C) / total))
