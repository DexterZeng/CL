import numpy as np
# load a file and return a list of tuple containing $num integers in each line
def loadfile(fn, num=1):
	print('loading a file...' + fn)
	ret = []
	with open(fn, encoding='utf-8') as f:
		for line in f:
			th = line[:-1].split('\t')
			x = []
			for i in range(num):
				x.append(int(th[i]))
			ret.append(tuple(x))
	return ret


def get_ent2id(fns):
	ent2id = {}
	for fn in fns:
		with open(fn, 'r', encoding='utf-8') as f:
			for line in f:
				th = line[:-1].split('\t')
				ent2id[th[1]] = int(th[0])
	return ent2id

def loadNe(path):
	f1 = open(path)
	vectors = []
	for i, line in enumerate(f1):
		id, word, vect = line.rstrip().split('\t', 2)
		vect = np.fromstring(vect, sep=' ')
		vectors.append(vect)
	embeddings = np.vstack(vectors)
	return embeddings
