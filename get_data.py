# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:04:17 2017

@author: CReichlen9
"""
import os
import pickle
import pandas as pd
import numpy as N

#movie_arr = np.array([])
#user_arr = np.array([])
#rating_arr= np.array([])

PATH = 'C:/Users/CReichlen9/.spyder-py3/input files/Data/download/training_set/'
PPATH = 'C:/Users/CReichlen9/.spyder-py3/input files/Data/download/probe.tx')
numratings = 100480507
movieratings = N.zeros(numratings, dtype=N.int8)
movieids = N.zeros(numratings, dtype=N.int16)
userids = N.zeros(numratings, dtype=N.int32)
#movieratings = N.empty([], dtype=N.int8)
#movieids = N.empty([], dtype=N.int16)
#userids = N.empty([], dtype=N.int32)
#movieratings = [int()]
#movieids = [int()]
#userids = [int()]

def makearrays(dataloc):
    #from time import mktime
    nummovies = 3500
    #numusers = 480189
#    numratings = 100480507
#
#    movieratings = N.zeros(numratings, dtype=N.int8)
#    movieids = N.zeros(numratings, dtype=N.int16)
#    userids = N.zeros(numratings, dtype=N.int32)
    #dates = N.zeros(numratings, dtype=N.int32)
    counter = 0

    for i in range(nummovies):
        if i % 100 == 0: print('Extracting movie %d' % i)
        f = open(dataloc + 'mv_%07d.txt' % (i+1), 'rt')
        data = f.readlines()
        f.close()

        movieid = int(data.pop(0)[:-2])
        inumratings = len(data)
        movieids[counter:counter+inumratings] = movieid
        

        for j in range(inumratings):
            userid, stars, date = data[j][:-1].split(',')
            #year, month, day = date.split('-')
            #epoch = mktime((int(year), int(month), int(day), 0, 0, 0, 0, 0, 0))
            userids[counter] = int(userid)
            #userids.append(userid)
            movieratings[counter] = int(stars)
            #movieratings.append(stars)
            #dates[counter] = epoch
            #movieids.append(movieid)
            counter += 1

#    print('Finding unique users')
#    allusers = N.unique(userids)
#
#    print('Zero-indexing users and movies')
#    movieids -= 1
#    convertusers = N.zeros(N.max(allusers)+1, dtype=N.int32)
#    convertusers[allusers] = N.r_[0:numusers]
#    userids = convertusers[userids]

    return movieratings, movieids, userids

makearrays(PATH)
DICT = {'movie_id': movieids, 'user_id': userids, 'rating_value': movieratings}
df = pd.DataFrame.from_dict(DICT, orient='columns', dtype=None)
print('Saving dataframe...')
#df.to_pickle('flixpdframe.pkl')
df.to_pickle('flixpd3ksample.pkl')
print('Complete')