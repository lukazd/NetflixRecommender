import pickle
from surprise import SVD, SVDpp, KNNBasic, CoClustering
from surprise import Dataset, Reader
from surprise import evaluate, print_perf, accuracy

num_models=2
num_predictions = 1408342

with open('/Shared/bdagroup7/download/predictions_svd.dat', 'rb') as f:
    model_1 = pickle.load(f)
with open('/Shared/bdagroup7/download/predictions_co_clustering.dat', 'rb') as f:
    model_2 = pickle.load(f)

A=[p.est for p in model_1]
B=[p.est for p in model_2]

e_predictions=[]

zipped=zip(A,B)

e_ests=[item[0]*.8 + item[1]*.2 for item in zipped]

for i in range(0, num_predictions):
    e_predictions.append((model_1[i][0], model_1[i][1], model_1[i][2], e_ests[i], model_1[i][4]))


rmse = accuracy.rmse(e_predictions, verbose=True)

print("RMSE is: ")
print(rmse)
