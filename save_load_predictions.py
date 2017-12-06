#to save predictions
with open('predictions.data', "wb") as f:
	pickle.dump(predictions, f)

#to load predictions

with(open('predictions.dat', "rb") as f:
	g = pickle.load(f)