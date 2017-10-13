# -*- coding: utf-8 -*-
import pandas as pd
import os

filepath = './data/'
filelists = os.listdir(filepath)
datas = []
#处理原始数据
def convert_data(sale_day):
    sales_list = sale_day.strip('\n').split('\t')
    return [sales_list[2], sales_list[3]]
#读取文件夹中的数据
for file in filelists:
    data = pd.read_csv(filepath + file)
    print data.head()

