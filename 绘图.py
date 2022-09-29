import numpy as np
import matplotlib.pyplot as plt
# import os, sys
# os.chdir(sys.path[0])

accus9_ideal = np.loadtxt('accus9_ideal.txt')
accus9_qxs = np.loadtxt('accus9_qxs.txt')

plt.plot(accus9_ideal, label='ideal')
plt.plot(accus9_qxs, label='qxs')
plt.legend()
plt.show()