
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:42:45 2017

@author: CReic
"""
import pandas as pd
import numpy as np
import surprise
import pickle

df = pd.read_pickle('flixpdframe.pkl')
reader = surprise.dataset.Reader(rating_scale=(1, 5))
data = surprise.dataset.Dataset.load_from_df(df, reader)

bsl_options = {'method': 'sgd',
             'n_epochs': 5,
             'reg_u': 12,
             'reg_i: 5
             }

sim_options = {'name': 'pearson_baseline',
               'shrinkage': 0  
               }

algo1 = KNNBasic(bsl_options=bsl_options, 
                 sim_options=sim_options)

algo2 = KNNWithMeans(k=10, min_k=5, 
                     sim_options=sim_options)

algo3 = SVD(n_factors=100, n_epochs=20, biased=True,
            init_mean=0, init_std_dev=0.1, lr_all=0.005, 
            lr_bu=None, lr_bi=None, lr_qi=None, reg_all=None,
            reg_bi=None, reg_pu=None, reg_qi=None, verbose=False)

algo4 = SVDpp(n_factors=20, n_epochs=20, biased=True,
            init_mean=0, init_std_dev=0.1, lr_all=0.005, 
            lr_bu=None, lr_bi=None, lr_qi=None, reg_all=None,
            reg_bi=None, reg_pu=None, reg_qi=None, verbose=False)
