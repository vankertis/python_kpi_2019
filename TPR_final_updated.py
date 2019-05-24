import numpy as np
import random
import string
import names
import pandas as pd
import matplotlib.pyplot as plt

#Reading data from the csv file
df = pd.read_csv("Datas.csv")

n_s = df['Income'].count()

#Creating dictionary
d = {df['Name'][i]: [df['Income'][i], i+1] for i in range (n_s)}
print(d)

#Sorting by income
sorted_dict = sorted(d.items(), key=lambda kv: kv[1])

#Creating array of incomes
b1 = []
for i in range(df['Income'].count()):
    b1.append(sorted_dict[i][1][0])

#Providing data regarding the total cost
cost1= 1200000

#Summation of incomes
def income_sum(inc_array):
    summar = 0
    for i in range(len(inc_array)):
        summar += inc_array[i]
    return summar

#Function for the first type of the tax (for person type)
def for_person(c,summ,n,b_acum):
    x =[]
    a = c/n
    #Making first loop without xi
    if a > b_acum[0]:
        x.append(b_acum[0])
    else:
        for j in range(n):
            x.append(a)
        return x
    #Creating another loop for the rest of elements (starting from the second element)
    for i in range(1,n):
        a = (c-x[i-1])/(n-i)
        #Updating c for the next iteration
        c = c - x[i-1]
        #If element is bigger than income, we add income value to the list
        if a>b_acum[i]:
            x.append(b_acum[i])
        #If element is smaller than income then we are starting the filling for the rest of elements
        else:
            for j in range(i, n):
                x.append(a)
            break
    return x

#Function for the second type of the tax (proportional type)
def proportional (c, summ, n, b_acum):
    x = []
    coef = c/summ
    for i in range(n):
        x.append(b_acum[i]*coef)
    return x


#Function for the third type of the tax (level type)
def level (c, summ, n, b_acum):
    x = []
    #Creating a loop
    for i in range(n):
        a = (summ-c)/(n-i)
        if a>b_acum[i]:
            x.append(0)
            summ = summ-b_acum[i]
        else:
            for j in range(i, n):
                x.append(b_acum[j]-a)
            break
    return x

def calculate_nCore(incomes, required_tax):
    """Calculate nCore tax"""
    taxes=[]
    ind, inc = zip(*sorted(enumerate(incomes),key = lambda t: t[1]))
    if required_tax < sum(inc) / 2:
        a = (required_tax - sum[taxes]) / (len(inc) - i)
        taxes = [inc[0] / 2 if (a > inc[0] / 2) else a]

        for i in range(1,len(inc)):
            a = (required_tax - sum[taxes]) / (len(inc) - i)
            taxes.append(inc[i] / 2 if (a > inc[i]) / 2) else a)
    else:
        for i in range(n):
            a = (sum(inc) - required_tax) - sum(taxes) / len(inc) - i)
            if a > inc[i] / 2:
                taxes.append(inc[i] / 2)
            else:
                taxes += [(inc[j] - a) for j in range (i, len(inc)]
                break
    return taxes

def nCore (c, summ, n, b_acum):
    what_half = summ / 2
    x = []
    if c < what_half:
        a = c / n
        # Making first loop without xi
        if a > b_acum[0] / 2:
            x.append(b_acum[0] / 2)
        else:
            for j in range(n):
                x.append(a)
            return x
        # Creating another loop for the rest of elements (starting from the second element)
        for i in range(1, n):
            a = (c - x[i - 1]) / (n - i)
            # Updating c for the next iteration
            c = c - x[i - 1]
            # If element is bigger than income, we add income value to the list
            if a > b_acum[i] / 2:
                x.append(b_acum[i] / 2)
            # If element is smaller than income then we are starting the filling for the rest of elements
            else:
                for j in range(i, n):
                    x.append(a)
                break
        return x
    else:
        for i in range(n):
            a = (summ-c) / (n-i)
            if a>(b_acum[i] / 2):
                x.append(b_acum[i] / 2)
                summ = summ-(b_acum[i] / 2)
            else:
                for j in range(i, n):
                    x.append(b_acum[j]-a)
                break
        return x

tot_income = income_sum(b1)

print("Summa is: "+ str(tot_income))

tax1 = for_person(cost1,tot_income,n_s,b1)
tax2 = level(cost1,tot_income, n_s, b1)
tax3 = proportional(cost1,tot_income,n_s,b1)
tax4 = nCore(cost1,tot_income,n_s,b1)

feedback = f'For person tax:  {tax1}\n' \
        f'Level tax:  {tax2}\n'\
        f'Proportional tax: {tax3}\n' \
        f'N-Core: {tax4}'

print(feedback)

for i in range(n_s):
    sorted_dict[i][1].append([tax1[i],tax2[i],tax3[i],tax4[i]])
print(sorted_dict)


sorted_dict1=sorted(sorted_dict, key=lambda x: x[1][1])

print (sorted_dict1)
t1 = []
t2 = []
t3 = []
t4 = []
for i in range(n_s):
    t1.append(sorted_dict1[i][1][2][0])
    t2.append(sorted_dict1[i][1][2][1])
    t3.append(sorted_dict1[i][1][2][2])
    t4.append(sorted_dict1[i][1][2][3])

df['For person tax'] = t1
df['Level tax'] = t2
df['Proportional tax'] = t3
df['nCore tax'] = t4
df.to_csv('datas.csv')

service = []
for i in range(30):
    service.append(i+1)

plt.plot (service, for_person(cost1,tot_income,n_s,b1))
plt.plot (service, level(cost1,tot_income,n_s,b1))
plt.plot (service, proportional(cost1,tot_income,n_s,b1))
plt.plot (service, nCore(cost1,tot_income,n_s,b1))

plt.show()
