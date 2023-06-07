import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


def max_prominence(valuedata):
    max_value = max(valuedata)
    min_value = min(valuedata)
    return max_value - min_value

def find_swinglowhigh(data) :
    for date_data in data:
        cur_date = date_data[0][1].split(' ')[0]
        cur_date = cur_date.replace('/', '-')
        timestamp = np.linspace(0, len(date_data), len(date_data))
        close_data = np.array([float(i[0]) for i in date_data])

        max_prom = max_prominence(close_data)/20;

        peaks,_ = find_peaks(close_data, prominence=max_prom, distance = 10)
        valleys,_ = find_peaks(-close_data, prominence=max_prom, distance= 10)

        fig = plt.figure(figsize=(1200/96,500/96), dpi=96)
        plt.title(cur_date)
        plt.plot(timestamp, close_data)
        
        plt.plot(timestamp[peaks], close_data[peaks], "x")
        plt.plot(timestamp[valleys], close_data[valleys], "o")
        
        plt.savefig('./plots/'+cur_date+'.png')  
        plt.close(fig)
    pass


def find_trendlines(data) :
          
    pass