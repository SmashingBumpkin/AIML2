X = [(2.44, 0.96), (2.28, 1.06), (1.45, 4.23), (1.91, 3.82), (2.13, 1.62), (0.92, 4.51)]
mu1 = (1.4, 3)
mu2 = (1.8, 2)
Xass = []
for x in X:
    dist1 = (x[0] - mu1[0]) ** 2 + (x[1] - mu1[1]) ** 2
    dist2 = (x[0] - mu2[0]) ** 2 + (x[1] - mu2[1]) ** 2

    if dist1 < dist2:
        Xass.append("mu1")
    else:
        Xass.append("mu2")
print(Xass)

mu1Ass = [(2.44, 0.96), (2.28, 1.06), (2.13, 1.62)]
mu2Ass = [(1.45, 4.23), (1.91, 3.82), (0.92, 4.51)]

mu1New = (0, 0)
mu2New = (0, 0)
for i in range(3):
    mu1New = (mu1Ass[i][0] + mu1New[0], mu1Ass[i][1] + mu1New[1])
    mu2New = (mu2Ass[i][0] + mu2New[0], mu2Ass[i][1] + mu2New[1])

# mu1New = mu1New / 3
# mu2New = mu2New / 3

print(mu1New, mu2New)
