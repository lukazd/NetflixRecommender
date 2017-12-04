from surprise import SVD
from surprise import Dataset, Reader
from surprise import evaluate, print_perf

reader_params=dict(line_format='item rating user',
                   rating_scale=(1, 5),
                   sep='\t')
reader = Reader(**reader_params)

data = Dataset.load_from_file(file_path='/Shared/bdagroup7/download/ratings.csv', reader=reader)
training_set = data.build_full_trainset()
test_set = training_set.build_testset()
#data.split(n_folds=3)

algo = SVD()

#perf = evaluate(algo, data, measures=['RMSE', 'MAE'])

#print_perf(perf)

algo.train(training_set)

predctions = algo.test(test_set)

# TODO: Ensemble

rmse = surprise.accuracy.rmse(predictions, verbose=True)

print("RMSE is: ")
print(rmse)
