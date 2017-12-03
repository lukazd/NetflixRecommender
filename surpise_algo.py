# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:31:23 2017

@author: CReichlen9
"""
import numpy as np
import pandas as pd
import surprise
#from surprise import prediction_algorithms as pa
#from surprise import dataset
import pickle

#df = pd.read_pickle('flixpdframe.pkl')
print('Loading data...')
df = pd.read_pickle('flixpd3ksample.pkl')
df2 = df.take(np.random.permutation(len(df))[:20000])
print('Rearranging columns...')
cols = df2.columns.tolist()
cols = cols[-1:] + cols[:-1]
df2 = df2[cols]
print('Reading data...')
reader = surprise.dataset.Reader(rating_scale=(1, 5),
                        skip_lines=1)
data = surprise.dataset.Dataset.load_from_df(df2, reader)
print('Building training set...')
#trainset = surprise.dataset.DatasetAutoFolds(reader=reader, df=df)
trainset = data.build_full_trainset()
print('Building test set...')
test_set = trainset.build_testset()

bsl_options = {'method': 'sgd',
             'learning_rate': .0005
             }

sim_options = {'name': 'cosine',
               'user_based': True, 
               }

algo1 = surprise.KNNBasic(bsl_options=bsl_options,
                 sim_options=sim_options)

algo2 = surprise.KNNWithMeans(k=15, min_k=5,
                     sim_options=sim_options)

algo3 = surprise.SVD(n_factors=20000, n_epochs=20, biased=False,
            init_mean=0, init_std_dev=0.1, lr_all=0.005,
            lr_bu=None, lr_bi=None, lr_qi=None, reg_all=None, reg_bu=0,
            reg_bi=0, reg_pu=0, reg_qi=0, verbose=True)

#algo4 = surprise.SVDpp(n_factors=20, n_epochs=20, init_mean=0, init_std_dev=0.1,
#                       lr_all=0.005, reg_all=None, verbose=True)

print('Training model...')
algo1.train(trainset)
print('Making predictions...')
predictions = algo1.test(test_set)
print('Evaluating results...')
surprise.accuracy.rmse(predictions, verbose=True)
print('All done.')

