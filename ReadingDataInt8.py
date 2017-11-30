
 

import os as os
import numpy as np

num_movies= 17770
num_users=480189


DIR_PATH = r"C:\Users\neeva\Documents\Big Data Analytics\Training Set"

user_movie_mat=np.matrix(np.zeros((num_users,num_movies),dtype=np.uint8))

# collect all the file names within the dataset
files_array = []
os.chdir(DIR_PATH)
for files in os.listdir("."):
    if files.endswith(".txt") :
      files_array.append(files)

#

ID_map={}
row=0
for fileName in files_array:
    f=open(DIR_PATH+ '\\'+fileName)
    colNum = fileName.split('mv_')
    fileNumList = colNum[1].split('.')        
    colNum = int(fileNumList[0])-1
    for line in f:
        if ':' not in line:
            line_list=line.split(',')
            Real_ID=int(line_list[0])
            if Real_ID not in ID_map.keys():
                ID_map[Real_ID]=row
                rowNum=row
                row=row+1
            else:
                rowNum=ID_map[Real_ID]
            user_movie_mat[rowNum,colNum]=np.uint8(line_list[1])
  
    

