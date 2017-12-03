#KNN

#we need: 

#similarity function
    #must only consider 
#function that takes in one vector and finds k nearest vectors
#function that averages

import numpy
from scipy.spatial import distance

#normal version 
def extract_overlap(a,b,length):
    new_a=np.array([])
    new_b=np.array([])
    for i in range(0,length):
        if a[i]!=0 and b[i]!=0:
            new_a=np.append(new_a,a[i])
            new_b=np.append(new_b,b[i])
    return[new_a,new_b]

# for stupid numpy matrix

def extract_overlap_mat(a,b,length): #uses global ratings variable? #a and b now specify user rows
    global user_movie_mat 
    new_a=np.array([])
    new_b=np.array([])
    for i in range(0,length):
        if user_movie_mat[a,i]!=0 and user_movie_mat[b,i]!=0:
            new_a=np.append(new_a,user_movie_mat[a,i])
            new_b=np.append(new_b,user_movie_mat[b,i])
    return[new_a,new_b]

def find_k_neighbors(k,user,movie): #find k neighbors of user in order to find its rating for movie
    global user_movie_mat
    distances=np.array([])
    for i in range(0,480189):
        if user_movie_mat[i,movie]==0:
            distances=np.append(distances,9999.0)#do not consider this neighbor (this will include itself) 
        else:
            overlap=extract_overlap_mat(user,i,17770)
            distances=np.append(distances,distance.euclidean(overlap[0],overlap[1]))
    k_neighbors=np.argsort(distances)[0:k]
    return(k_neighbors)

def estimate_rating(k,k_neighbors,movie):
    global user_movie_mat 
    total=0
    for neighbor in k_neighbors:
        total=total+ user_movie_mat[neighbor,movie]
    return(total/k) 
            
    

#for every user in the test set
#extract overlap with every user in the training set (only if they have rated movie of interest- otherwise, overlap is -5)
# 

#figure out cosine similaritiy
#store cosine similarity in an array
#get indices of k smallest arrays by using argsort of the distance array and taking the first k indices
#indices represent row of user in original matrix with similarity

#have a sorted list of top 2 best matches so far [-3,-4,-5]
#min to be on this list : at least -5
#




            
        
            
            
