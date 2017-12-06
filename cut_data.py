# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 23:02:32 2017

@author: CReic
"""

import pandas as pd
dmp = pd.read_csv('C:/Users/CReic/.spyder-py3/input_files/download/flixminusprobe.csv', sep=',')
pro = pd.read_csv('C:/Users/CReic/.spyder-py3/input_files/download/flixprobe.csv', sep=',')

dmp = dmp.drop(dmp.columns[0], axis=1)
dmp = dmp.take(np.random.permutation(len(df2))[:50000])

pro = pro.drop(pro.columns[0], axis=1)
pro = pro.take(np.random.permutation(len(df2))[:5000])

dmp.to_csv('C:/Users/CReic/.spyder-py3/input_files/download/flix50kmp.csv')
pro.to_csv('C:/Users/CReic/.spyder-py3/input_files/download/flix10kp.csv')