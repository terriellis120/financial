import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import csv

# import data from csv file

data = []
with open('./data/data2.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        data.append(row['close'])

# Find peaks with minimum prominence and minimum distance

x = np.linspace(0, len(data), len(data))
y = np.array([float(i) for i in data])


peaks,_ = find_peaks(y, prominence=5, distance = 10)
valleys,_ = find_peaks(-y, prominence=5, distance= 10)
print(y)


plt.plot(x, y)
plt.plot(x[peaks], y[peaks], "x")
plt.plot(x[valleys], y[valleys], "o")


plt.show()