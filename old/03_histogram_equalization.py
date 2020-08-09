import numpy as np
from matplotlib import pyplot as plt

def cal_histogram_norm(img):
	L = img.shape[1]
	M = img.shape[0]
	h = np.zeros([255])

	for i in range(0,M):
		for j in range(0, L):
			#print(img[i, j])
			h[img[i, j]] = h[img[i, j]] + 1

	h_norm = np.zeros([255])
	for j in range(0, 255):
		h_norm[j] = h[j]/(M*L)
	return h_norm


def cal_histogram(img):
	L = img.shape[1]
	M = img.shape[0]
	h = np.zeros([255])

	for i in range(0,M):
		for j in range(0, L):
			print(int(img[i, j]))
			h[int(img[i, j])] = h[int(img[i, j])] + 1

	return h



def init_histogram_mapping_table(h, img):
	M = img.shape[0]
	L = img.shape[1]

	table = list([])
	#print("--- histogram mapping table ----")
	for i in range(0, 255):
		x = list([0, 0, 0, 0, 0])
		x[0] = i
		x[1] = h[i]
		x[2] = x[1]
		for j in range(0, i):
			x[2] = x[2] + h[j]
		x[3] = x[2] * (L-1)
		x[4] = round(x[3])
		#print(x)
		table.append(x)
	#print("")
	table = np.array(table)
	#print(table)
	return table




def histogram_equalization(h, img):
	table = init_histogram_mapping_table(h, img)
	M = img.shape[0]
	L = img.shape[1]
	
	e_img = np.zeros([L, M])
	for i in range(0, M):
		for j in range(0, L):
			e_img[i, j] = table[img[i, j], 4]			

	print("--- equalized img ---")
	print(e_img)
	print("")
	return e_img

def visualize_histogram(h_norm):
	plt.bar(range(0, 255), h_norm)
	plt.show()



def main():
	img = [
		[3, 2, 2, 2, 2, 3, 3, 4],
		[3, 2, 2, 2, 3, 4, 3, 3],
		[4, 3, 3, 4, 4, 4, 3, 3],
		[5, 4, 4, 4, 5, 4, 3, 3],
		[5, 4, 3, 4, 5, 4, 3, 2],
		[6, 5, 4, 4, 5, 4, 3, 2],
		[6, 6, 5, 5, 4, 3, 2, 2],
		[6, 5, 4, 5, 4, 3, 2, 2]
	]
	img = np.array(img)


	print("--- img ---")
	print(img)
	print("")
	h_norm = cal_histogram_norm(img)

	"""
	print("--- h_norm ---")
	print(h_norm)
	print("")
	"""
	e_img = histogram_equalization(h_norm, img)
	h = cal_histogram(e_img)

	visualize_histogram(h)


if __name__ == "__main__":
	main()	 