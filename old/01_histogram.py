import numpy as np
from matplotlib import pyplot as plt


def cal_histogram(img):
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

	return [h, L]

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
[h, L] = cal_histogram(img)
print("h : ", h)

x = range(0, L)
plt.bar(x, h)
plt.axis('auto')
plt.show()