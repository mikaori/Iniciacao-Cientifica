%matplotlib inline
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

data = pd.read_csv('dados1.txt')
print(data.shape)
data.head()

coluna1 = data['x'].values
coluna2 = data['y'].values

nsei = np.array(list(zip(coluna1, coluna2)))
plt.scatter(coluna1, coluna2, c='red', s=2)
