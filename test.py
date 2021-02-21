#python2 pacman.py --pacman RandomAgent
#python2 pacman.py --pacman RandomishAgent
#python2 pacman.py --pacman ClassifierAgent

training_dataset = [#[Colour, Diameter, label] 
	['Green', 3, 'Apple'],
	['Yellow', 3, 'Apple'],
	['Red', 1, 'Grape'],
	['Red', 1, 'Grape'],
	['Yellow', 1, 'Lemon']
]

training_data = [#[size, peel, label] 
	[1, 0, 'Apple'],
	[1, 0, 'Apple'],
	[0, 0, 'Grape'],
	[0, 0, 'Grape'],
	[1, 1, 'Lemon']
]

def class_counts(rows):
	"""Counts the number of each type of example in a dataset."""
	counts = {}  # a dictionary of label -> count.
	for row in rows:
		# in our dataset format, the label is always the last column
		label = row[-1]
		if label not in counts:
			counts[label] = 0
		counts[label] += 1
	return counts #{'Lemon': 1, 'Grape': 2, 'Apple': 2}


def partition(data, column):
	"""
	Partitions a dataset.

	For each row in the data set check whether the given column index
	is true (1) or false (0) and split accordingly.
	return arrays of both cases.
	"""
	true_rows, false_rows = [], []
	for row in data:
		if row[column] == 1:
			true_rows.append(row)
		else:
			false_rows.append(row)
	return true_rows, false_rows

#true_rows, false_rows = partition(training_data, 0)
#print true_rows

def gini(rows):
	"""
	Calculate the Gini Impurity for a list of rows.
	"""
	counts = class_counts(rows)
	impurity = 1
	for lbl in counts:
		prob_of_lbl = counts[lbl] / float(len(rows))
		impurity -= prob_of_lbl**2
	return impurity

no_mixing = [['Apple'], ['Apple']]
some_mixing = [['Apple'], ['Orange']]
lots_of_mixing = [['Apple'], ['Orange'], ['Grape'], ['Grapefruit'], ['Blueberry']]

print gini(no_mixing)
lots_of_mixing = [['Apple'],
                  ['Orange'],
                  ['Grape'],
                  ['Grapefruit'],
                  ['Blueberry']]