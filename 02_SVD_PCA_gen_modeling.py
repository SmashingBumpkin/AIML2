import numpy as np
import cv2  # opencv
import matplotlib.pyplot as plt
import random

# Reproducibility stuff
np.random.seed(42)  # initialize NumPy's RNG
random.seed(0)  # initialize Python's built-in RNG

from matplotlib.colors import ListedColormap

cmap = ListedColormap(["green", "white", "red"])
im = np.array(
    [
        [
            1,
        ]
        * 50
        + [
            2,
        ]
        * 50
        + [
            3,
        ]
        * 50
        for _ in range(100)
    ]
)  # 100 x 150
plt.imshow(im, cmap=cmap, interpolation="nearest")
plt.axis("off")
# plt.show()
U, S, Vh = np.linalg.svd(im, False)
plt.imshow(U)
plt.show()
