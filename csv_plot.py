from cProfile import label
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import csv
rows = []
with open("EV\sampleFile.csv","r",newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)


plot1 = plt.title("voltage curve")
plt.plot(rows[0],"rs-",label='voltage')
plt.xticks(rotation=25)
plt.yticks([-2,-1,0,1,2],rotation=0)
plt.legend()
plt.show()