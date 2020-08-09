import numpy as np
from matplotlib import pyplot as plt


def cal_histogram_norm(img):
	print(img.shape)
	L = img.shape[1]
	M = img.shape[0]
	print("L : ",  L)
	print("M : ",  M)
	h = np.zeros([L])

	for i in range(0,M):
		for j in range(0, L):
			#print(img[i, j])
			h[img[i, j]] = h[img[i, j]] + 1

	h_norm = np.zeros([L])
	for j in range(0, L):
		h_norm[j] = h[j]/(M*L)
	return [h_norm, L]

img = [
	[3, 2, 2, 4, 4, 4, 3, 2, 2],
	[3, 2, 2, 2, 2, 2, 3, 2, 2],
	[3, 3, 0, 3, 2, 2, 3, 3, 3],
	[3, 3, 3, 3, 2, 2, 4, 4, 4],
	[3, 2, 2, 2, 2, 2, 2, 2, 4],
	[3, 3, 3, 3, 2, 4, 4, 4, 4],
	[5, 5, 5, 5, 2, 2, 2, 2, 3],
	[2, 2, 2, 2, 2, 3, 3, 3, 3]
]
img = np.array(img)

print(img)
[h_norm, L] = cal_histogram_norm(img)
print("h : ", h_norm)

x = range(0, L)
plt.bar(x, h_norm)
plt.axis('auto')
plt.show()