import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
from calculateData import *

#X = pd.read_csv('motordata.txt', sep="\t", header=None)
#X = pd.read_excel('motordata.xlsx')
X = calculateData()
print(X)
y= []

# implement selection for right or left side of the figure or maybe start plotting in the left after yno>3

for j in X.columns:
    print(j, end='\t\t')
x = input('\nEnter data for x-axis: ')

yno = input('Number of y-axes: ')

for i in range(0,int(yno)):
    for j in X.columns:
        print(j, end='\t\t')
    y.append(input('\nEnter data for #%d y-axis: '%(i+1) ))

twin = []

fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(right=0.65)

if int(yno) > 1:
    for i in range(0,int(yno)-1):
        twin.insert(i,ax.twinx())


yno_increment = 1.2+float(yno)*.2
for (i,j) in zip(np.arange(1.2,yno_increment,.2),range(1,int(yno)-1)):
       twin[j].spines.right.set_position(("axes", i))

p = [0]*int(yno)
p[0], = ax.plot(X.iloc[:,1], X.loc[:,y[0]], "r-", label=y[0])
ax.set_xlabel("Current")
ax.set_ylabel(str(y[0]))
ax.set_xlim(X['I'].min(),X['I'].max())
ax.set_ylim(X[y[0]].min(),X[y[0]].max())
ax.xaxis.set_major_locator(ticker.AutoLocator())
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.yaxis.set_major_locator(ticker.LinearLocator(6))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.grid(color = 'green', linestyle = '--', linewidth = 0.5)

for (i,j) in zip(range(0,int(yno)),range(1,int(yno))):
    p[i], = twin[i].plot(X.iloc[:,1],X.loc[:,y[j]],label=y[i])
    twin[i].set_ylabel(str(y[j]))
    twin[i].set_xlim(X['I'].min(), X['I'].max())
    twin[i].set_ylim(X[y[j]].min(), X[y[j]].max())
    twin[i].yaxis.set_major_locator(ticker.LinearLocator(6))
    twin[i].yaxis.set_minor_locator(ticker.AutoMinorLocator())
#   ax.legend()


# twin1.set_ylim(0, 4)
# twin2.set_ylim(1, 65)
# twin3.set_ylim(0,8000)
##
# ax.yaxis.label.set_color(p1.get_color())
# twin1.yaxis.label.set_color(p2.get_color())
# twin2.yaxis.label.set_color(p3.get_color())
# twin3.yaxis.label.set_color(p4.get_color())

plt.show()