'''
@author : DaXiang Long
Description: open csv file and preprocess data to sepearte the data by date
'''

import csv

def open_csvfile(csv_Filename):
    data = []
    with open(csv_Filename, 'r', encoding = 'utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append((row['close'], row['timestamp']))
    return data
        
def separate_by_date(data):

    separate_data = []
    current_date = data[0][1].split()[0]
    per_date_list = []
    for items in data:
        if items[1].split()[0] != current_date:
            current_date = items[1].split()[0]
            separate_data.append(per_date_list)
            per_date_list = []
        per_date_list.append(items)
    separate_data.append(per_date_list)
    return(separate_data)
    pass        