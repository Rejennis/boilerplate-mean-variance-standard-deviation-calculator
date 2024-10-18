import numpy as np

def calculate(list):
	# This to check if list has exactly 9 elements
	if len(list) !=9:
		raise ValueError("List must contain nine numbers.")

	# This to convert list into a 3x3 NumPy array
	matrix = np.array(list).reshape(3,3)

	# This is to perform the calculations along axes 0 (rows), 1 (columns), and flattened (entire matrix)
	calculations = {
		'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
		'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
		'standard deviation':[matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
		'max':[matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
		'min':[matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
		'sum':[matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
	}
	return calculations
