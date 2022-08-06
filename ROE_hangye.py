# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 11:49:35 2022

@author: yhj
"""
import pandas as pd
data=pd.read_excel('C:/Users\yhj\Desktop\ROE_ANALYSIS.xlsx')
print(data.columns)
#print(data)
#data.dropna(inplace=True)
#data['ROE22除以21'][3].astype('float')
for i in range(len(data['ROE22除以21'])):
    if type(data['ROE22除以21'][i])!=float:
        #print(data['ROE22除以21'][i])
        data['ROE22除以21'][i]=0
        #print(data['ROE22除以21'][i])
data.dropna(inplace=True)
"""
for i in range(len(data['ROE22除以21'])):
    if type(data['ROE22除以21'][i])!=float:
        #print(data['ROE22除以21'][i])
        #data['ROE22除以21'][i]=None
        print(data['ROE22除以21'][i])
"""
#print(data)
#print(type(data['所属申万行业指数\n2级'].value_counts()))
#print(data['所属申万行业指数\n2级'].value_counts().index)
#这里计算的是去年申万三级各行业中的企业数量
"""
for index in data['所属申万行业指数\n2级'].value_counts().index:
    print(index)

#print(data['所属申万行业指数\n2级'].value_counts()[1])
for index in data[float(data['ROE22除以21'])>1.15]['所属申万行业指数\n2级'].value_counts().index:
    print(index)
    """ 
series_origin=data['所属申万行业指数\n2级'].value_counts()
series_2=data[data['ROE22除以21']>1.15]['所属申万行业指数\n2级'].value_counts()
#print(data['所属申万行业指数\n2级'].value_counts().index)
print(data['所属申万行业指数\n2级'].value_counts())
#print(data[data['ROE22除以21']>1.15]['所属申万行业指数\n2级'].value_counts().index)    
#print(series_origin.loc['汽车零部件Ⅱ(申万)'])
#print(series_2.loc['汽车零部件Ⅱ(申万)'])
list_1=[]
list_2=[]
for index_origin in series_origin.index:
    for index_2 in series_2.index:
        if index_origin==index_2:
            list_1.append(index_origin)
            #print(index_origin)
            list_2.append(series_2.loc[index_origin]/series_origin.loc[index_origin])
            #print(series_2.loc[index_origin]/series_origin.loc[index_origin])
    
print(type(list_1))
print(type(list_2))
final_series=pd.Series(list_2,index=list_1)
print(final_series)
data_final={
    '名称':list_1,
    '22相对21S1数据变化':list_2
    
    }
data_final=pd.DataFrame(data_final)
data_final.to_excel('C:/Users\yhj\Desktop/final_data.xlsx',index=False)
    