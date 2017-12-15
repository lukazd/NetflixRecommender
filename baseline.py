import pickle
from surprise import SVD, SVDpp, KNNBasic, CoClustering, BaselineOnly
from surprise import Dataset, Reader
from surprise import evaluate, print_perf, accuracy

reader_params=dict(line_format='user item rating',
                   rating_scale=(1, 5),
                   sep=',')
reader = Reader(**reader_params)

train_data = Dataset.load_from_file(file_path='/Shared/bdagroup7/download/train.data', reader=reader)
probe_data = Dataset.load_from_file(file_path='/Shared/bdagroup7/download/probe.data', reader=reader)
training_set = train_data.build_full_trainset()
test_set_temp = probe_data.build_full_trainset()
test_set = test_set_temp.build_testset()

# Save training and test_set
#with open('/Shared/bdagroup7/download/test_set.dat', "wb") as f:
#    pickle.dump(test_set, f)
#with open('/Shared/bdagroup7/download/training_set.dat', "wb") as f:
#    pickle.dump(training_set, f)

# Read the dataset
#test_set = None
#training_set = None
#with open('/Shared/bdagroup7/download/test_set.dat', "rb") as f:
#    test_set = pickle.load(f)
#with open('/Shared/bdagroup7/download/training_set.dat', "rb") as f:
#    training_set = pickle.load(f)

# Learning options

sim_options = {'name' : 'cosine', 'min_support': 50, 'user_based' : True}
bsl_options = {'method' : 'sgd', 'learning_rate' : .0005}

# Algorithms (only select one)
#algo = SVD()
#algo = KNNBasic(k=10, min_k=8, sim_options=sim_options)
#algo = KNNWithMeans(k=15, min_k=5, sim_options=sim_options)
#algo = CoClustering()
#algo = SVDpp()
algo = BaselineOnly()

algo.train(training_set)

predictions = algo.test(test_set)

with open('/Shared/bdagroup7/download/predictions_baseline.dat', "wb") as f:
    pickle.dump(predictions, f)

# TODO: Ensemble

rmse = accuracy.rmse(predictions, verbose=True)

print("RMSE is: ")
print(rmse)
