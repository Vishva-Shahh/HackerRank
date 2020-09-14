import numpy as np
import pandas as pd

T = int(input())

for i in range(T):
    N = int(input())
    df = pd.DataFrame(np.array([input().strip().split() for _ in range(0, N + 1)], float).T)
    print(df.corr('kendall')[0][1:].argmax())
