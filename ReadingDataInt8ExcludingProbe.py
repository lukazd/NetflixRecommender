
 

import os as os
import numpy as np

num_movies= 17770
num_users=480189


DIR_PATH = r"C:\Users\neeva\Documents\Big Data Analytics\Training Set"
PROBE_PATH = r"C:\Users\neeva\Documents\Big Data Analytics"


probeFile=open(PROBE_PATH + '\\' + 'probe.txt')
probe=[]

for line in probeFile:
    if ':' in line:
        movie_ID=int(line.split(':')[0])
        valid=False 
    else:
        line_list=line.split(',')
        user_ID=int(line_list[0])
        valid = True
    if valid==True:
        probe.append((user_ID,movie_ID))
        
        
#user-moving ratings matrix 
user_movie_mat=np.matrix(np.zeros((num_users,num_movies),dtype=np.uint8))

# collect all movie file names given training set directory 
files_array = []
os.chdir(DIR_PATH)
for files in os.listdir("."):
    if files.endswith(".txt") :
      files_array.append(files)


#dictionary maps user IDs to indices in the user-moving ratings matrix 
ID_map={}
row=0

#loops through each movie file and reads data 
for fileName in files_array:
    f=open(DIR_PATH+ '\\'+fileName)
    colNum = fileName.split('mv_')
    fileNumList = colNum[1].split('.')        
    colNum = int(fileNumList[0])-1 #index for movies are movie ID - 1
    for line in f: 
        if ':' not in line:
            line_list=line.split(',')
            Real_ID=int(line_list[0]) #get user ID 
            if Real_ID not in ID_map.keys(): #if user ID has not been encountered 
                ID_map[Real_ID]=row #add a new entry to the mapping dictionary 
                rowNum=row #row index for this user ID will be the new row 
                row=row+1
            else:
                rowNum=ID_map[Real_ID] #find the row index for this user ID
            if (Real_ID,colNum+1) not in probe:
                user_movie_mat[rowNum,colNum]=np.uint8(line_list[1])#add rating to matrix 
  
    

