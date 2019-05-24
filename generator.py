import numpy as np
import random
import string
import names
import pandas as pd
from random import randint

#Providing number of members
n= 30

def randomString(stringLength):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

names = []

for i in range(n):
    # print ("Random String is ", randomString(randint(1, 9)) )
    names.append(randomString(randint(3, 12)))

print(names)

a = np.random.randint(100000, size=n)

print(a)

df = pd.DataFrame(data={"Name": names, "Income": a})
df.to_csv("datas.csv", sep=',',index=False)





