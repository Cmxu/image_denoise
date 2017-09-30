

def unpickle(file):
	import pickle
	with open(file, 'rb') as fo:
		dict = pickle.load(fo, encoding='bytes')
	return dict

print("Loading Dataset")

im_batch_1_file = "../images/cifar_10/data_batch_1"

images = unpickle(im_batch_1_file)


