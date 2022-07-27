import numpy as np
import matplotlib.pyplot as plt


grades = np.array([58,64,80,90,95,100,98])

print("MEAN: " ,np.mean(grades))
print("MEDIAN: " ,np.median(grades))
print("MAX: " ,np.max(grades))
print("MAX: " ,np.std(grades))
print("PERCENTIL: " ,np.percentile(grades, 50))

plt.scatter([40,50,60,70,80,90,100],grades)

plt.show()