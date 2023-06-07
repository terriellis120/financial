'''
Project Name: Financial Data Analysis
Description:
    * Find Swing high/low points from the financial data
    * draw the upward/downward trendline
    * plot all
@author : DaXiang Long

'''

from open_csv import *
from financial_data_process import *

if __name__ == '__main__':

    # open csv file and separate by date
    data = open_csvfile('./data/sample_data_1_month.csv')
    date_data = separate_by_date(data)
    # 
    find_swinglowhigh(date_data)
    pass