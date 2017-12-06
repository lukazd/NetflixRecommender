# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:43:17 2017

@author: CReichlen9
"""

import os
import sys
import time
import pickle
import pandas as pd
import numpy as np

proberatings = 1408396

movieids = []
userids = []

probe = 'C:/Users/CReic/.spyder-py3/input_files/download/probe.txt'
lines = open(probe).read().split('\n')
movie_id = 0
user_id = 0
counter = 0

for i in range(len(lines)):
    
    if lines[i].endswith(':'):
        movie_id = int(lines[i][:-1])
        counter += 1
        print('Reading movie', counter, flush=True)
        
    else:
        user_id = np.int32(lines[i])
        movie_id = movie_id
        movieids.append(movie_id)
        userids.append(user_id)

DICT = {'userids': userids, 'movieids': movieids}
#dfp = pd.DataFrame.from_dict(DICT, orient='columns', dtype=None)
#print('Saving probe data')
#dfp.to_pickle('probe_array.pkl')
#print('Complete')
size = len(userids)
df = pd.read_pickle('C:/Users/CReic/.spyder-py3/flixpdframe.pkl')
probedict = {'user_id': np.empty(int(size)), 'movie_id': np.empty(int(size)),
'rating_value': np.empty(int(size))}
df1 = pd.DataFrame.from_dict(probedict, orient='columns', dtype=None) 
#indx_df = df.set_index(['user_id', 'movie_id', 'rating_value'])
#indx_df1 = df1.set_index(['user_id', 'movie_id', 'rating_value'])
#print('stripping probe data...')
#for i in range(size):
#    if userids[i] == userids1[i] and movieids[i] == movieids1[i]:
#        probedict.append('user_id': userids1[i], 'movie_id': movieids1[i],
#                         'rating_value': ratings[i])
#        df.drop(df.index[i])
   
#for i in range(size):
#    umatch = df.loc[df['user_id']==float(userids[i])].index
#    mmatch = df.loc[df['movie_id']==movieids[i]].index
#    print(df[umatch & mmatch])
#    df1.append(df[imatch])
#    df.drop(df[imatch])
