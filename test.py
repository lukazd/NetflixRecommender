from surprise import SVD
from surprise import Dataset, Reader
from surprise import evaluate, print_perf

reader_params=dict(line_format='user item rating timestamp',
                   rating_scale=(1, 5),
                   sep='\t')
reader = Reader(**reader_params)

data = Dataset.load_builtin('ml-100k')
data = Dataset.load_from_file(file_path='/Shared/bdagroup7/download/ml-100k/u.data', reader=reader)
data.split(n_folds=3)

algo = SVD()

perf = evaluate(algo, data, measures=['RMSE', 'MAE'])

print_perf(perf)
