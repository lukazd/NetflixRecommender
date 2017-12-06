import numpy as np 
import pandas as pd

'''
dictionary as probe
'''
                    
def readProbe():
    PROBE_PATH= '/Shared/bdagroup7/download/probe.txt'
    probeFile=open(PROBE_PATH)
    probe={}
    for line in probeFile:
        if ':' in line:
            movie_ID=np.int16(line.split(':')[0])
            valid=False
        else:
            line_list=line.split(',')
            user_ID=np.int32(line_list[0])
            valid = True
        if valid==True:
            probe[(user_ID,movie_ID)]=0
    return probe                  
'''
hardcoded numbers are for testing, not actual numbers. 
'''
def readData():
    probe=readProbe()
    numratings=100480507-1408395
    nummovies=17770
    movieratings=np.zeros(numratings,dtype=np.int8)
    movieids=np.zeros(numratings,dtype=np.int16)
    userids=np.zeros(numratings,dtype=np.int32)
    DIR_PATH = '/Shared/bdagroup7/download/training_set/'
    counter=0
    for i in range(nummovies):
        if i % 100 == 0: print('Extracting movie %d' % i)
        f=open(DIR_PATH + 'mv_%07d.txt' % (i+1), 'rt')
        movie_id=np.int16(i+1)
        for line in f:
            if ':' not in line:
                line_list=line.split(',')
                user_id=np.int32(line_list[0])
                if (user_id,movie_id) not in probe:
                    userids[counter]=user_id
                    movieids[counter]=movie_id
                    rating=np.int(line_list[1])
                    movieratings[counter]=rating
                    counter= counter+1
    DICT={'movie_id':movieids,'user_id':userids,'rating_value':movieratings}
    return(DICT)       
    
d=readData()
df2 = pd.DataFrame.from_dict(d, orient='columns', dtype=None)
print('Saving dataframe...')
#df.to_pickle('flixpdframe.pkl')
df2.to_pickle('flixminusprobe.pkl')
df2.to_csv('flixminusprobe.csv')