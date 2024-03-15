import numpy as np

A = np.array([[1, 1, 1],
 [2, 2, 2],
 [5, 5, 5]])
B = np.array([[0, 1, 0],
 [1, 1, 0],
 [1, 1, 1]])

print(np.einsum('ij,jk->ik', A, B))
print(A@B)
print(np.einsum('ij,jk->i', A, B)) #sum rows

print(np.einsum('ij,jk->j', A, B))


import matplotlib.pyplot as plt
import numpy as np

def plot_grid(Xs, Ys, axs=None):
    ''' Aux function to plot a grid'''
    t = np.arange(Xs.size) # define progression of int for indexing colormap
    if axs:
        axs.plot(0, 0, marker='*', markersize=7, color='r', linestyle='none') #plot origin
        axs.scatter(Xs,Ys, c=t, cmap='jet', marker='o') # scatter x vs y
        axs.axis('scaled') # axis scaled
    else:
        plt.plot(0, 0, marker='*', color='r',markersize=7, linestyle='none') #plot origin
        plt.scatter(Xs,Ys, c=t, cmap='jet', marker='o') # scatter x vs y
        plt.axis('scaled') # axis scaled

# let's see it with numpy
nX, nY, res = 10, 10, 21 # boundary of our space + resolution
X = np.linspace(-nX, +nX, res) # give me 21 points linear space from -10, +10 
Y = np.linspace(-nX, +nX, res) # give me 21 points linear space from -10, +10
# meshgrid is very useful to evaluate functions on a grid
# z = f(X,Y)
# please see https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html
Xs, Ys = np.meshgrid(X, Y) #NxN, NxN
plot_grid(Xs, Ys)
plt.show()
# plt.imshow(Ys, cmap='jet')


# Transformation
# 2x2
A = np.array([[1,2],[-1,3]])
A = np.array([[0,-1],[1,0]])
A = np.array([[2,-1],[4,-2]]) # this is not linearly dependent (det = 0) so you make the data linear, and lose info
#playing with these numbers will rotate/stretch/ ?move the array

# axis 0 1 2
# [NxN,NxN] -> NxNx2 # add 3-rd axis, like adding another layer
src = np.stack((Xs,Ys), axis=2)
# flatten first two dimension
# (NN)x2
src_r = src.reshape(-1,src.shape[-1]) #ask reshape to keep last dimension and adjust the rest
# 2x2 @ 2x(NN)
dst = A @ src_r.T # 2xNN
#(NN)x2 and then reshape as NxNx2
dst = (dst.T).reshape(src.shape)
# Access X and Y
Xd, Yd = dst[:,:,0], dst[:,:,1]
plot_grid(Xd, Yd) # plot
plt.show()
print("reached end....")
