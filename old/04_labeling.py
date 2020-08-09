import numpy as np
from matplotlib import pyplot as plt


def labeling(img):
	L = img.shape[1]
	M = img.shape[0]

	for i in range(0, M):
		for j in range(0, L):

			

			"""
			img[i + 1, j]
			img[i, j - 1]
			img[i, j]
			img[i, j + 1]
			img[i - 1, j]
			"""
			mat = np.zeros([3, 3])
			if (i != 0):
				mat[0, 1] = img[i + 1, j]

			if (j != 0):
				mat[1, 0] = img[i, j - 1]

			mat[1,1] = img[i, j]

			if (j != L):
				mat[1,2]= img[i, j + 1]

			if (i != M):
				mat[2,1] = img[i - 1, j]

			print("--- connect component --- curr pixel : ", i, j)
			print(mat)
			print("")


def main():

	img = np.array([
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
		[0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
		[0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
		[0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
		[0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	])

	print("--- input image ---")
	print(img)
	print("")

	labeling(img)

if __name__ == "__main__":
	main()