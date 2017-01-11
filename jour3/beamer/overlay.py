import numpy as np
import matplotlib.pyplot as plt

p = np.poly1d([1,-2,-3]) # Polynomial

x = np.linspace(-2, 4, 100)
y = p(x)

fig = plt.figure()
plt.plot(x,y)
plt.yticks([0])
plt.grid()
plt.xticks([])
plt.savefig("parabola_1.pdf")

plt.xticks(p.r)
plt.savefig("parabola_2.pdf")

