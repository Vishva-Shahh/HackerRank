# Enter your code here. Read input from STDIN. Print output to STDOUT
import pandas as pd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("trainingdata.txt")

data['Target'] = data['5485'].astype(str).str[0]

data['target'] = data['Target'].astype(int)

data.rename(columns={"5485": "text",}, inplace=True)

data["text"] = data['text'].astype(str).str[1:]

for txt in data.text: txt = txt[1:]

data['text'] = data['text'].str[1:]

md= CountVectorizer()

cvTrain = md.fit_transform(data.text)

clf = MultinomialNB()

clf.fit(cvTrain,data.target)

t = int(input())
lines = []
for i in range(t):
    line = input()
    lines.append(line)

test = md.fit_transform(lines)
pred = clf.predict(test)
for i in pred:
    print(pred[0])