# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:37:19 2018

@author: someshwar.kale
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

test = pd.read_csv('big_mart_sell_test.csv')
train = pd.read_csv('big_mart_sell_train.csv')

## data exploration univariate analysis
'''
Hypothesis
1. 'Outlet_Identifier','Item_Identifier' are redundant variables
2. sell of visible items is more
3. low fat contain item sale is high
4. establishment year inversly proporational to the sale
5. house hold and dairy products and fruits and vagetables having more sale
'''

train.columns
identifiers = ['Outlet_Identifier','Item_Identifier']
catagorical_variables = ['Item_Fat_Content','Item_Type', 'Outlet_Establishment_Year','Outlet_Location_Type','Outlet_Type']
numerical_variables = ['Item_Visibility','Item_MRP']
target_variable = 'Item_Outlet_Sales'

plt.figure(1)
count = 1
for i in catagorical_variables:
    plt.subplot(5,2,count)
    train[i].value_counts(normalize=True).plot.bar(figsize=(5,10), title= '%s'%i)
    plt.grid(True)
    count = count+1
plt.show()

plt.figure(1)
count = 1
for i in identifiers:
    plt.subplot(5,2,count)
    train[i].value_counts(normalize=True).plot.bar(figsize=(5,10), title= '%s'%i)
    plt.grid(True)
    count = count+1
plt.show()

train.isnull().sum()
train['Item_Weight'] = train['Item_Weight'].fillna((train['Item_Weight'].mean()))
## for now drop the item weight and out let size due to large missing data
train = train.drop(['Item_Weight'],axis = 1 )
train = train.drop('Outlet_Size', axis = 1)

count = 1
for variable in numerical_variables:
    plt.subplot(3,2,count)
    sns.distplot(train[variable]);
    plt.subplot(3,2,count+1)
    train[variable].plot.box(figsize=(5,3))
    plt.grid(True)
    count = count+1
    plt.show()

train['Item_MRP'].value_counts
