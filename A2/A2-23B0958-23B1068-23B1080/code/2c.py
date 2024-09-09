# Satyam Sinoliya, 23B0958
# Vaibhav Singh, 23B1068
# Shaik Awez Mehtab, 23B1080
# Problem number 2, task C

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

N = int(1e5)

def sample(loc, scale):
    x = np.random.uniform(0, 1, N)
    F_X_inverse = norm.ppf(x, loc=loc, scale=scale)
    return F_X_inverse

params = [(0, 0.2), (0, 1.0), (0, 5.0), (-2, 0.5)]
samples = [sample(mu, np.sqrt(sigma2)) for mu, sigma2 in params]

plt.figure(figsize=(10, 6))

for (mu, sigma), samplei in zip(params, samples):
    plt.hist(samplei, bins=500, density=True, alpha=0.6, label=f'μ={mu}, σ={sigma}')

plt.xlim(-5, 5)

plt.title('Gaussian Distribution')
plt.xlabel('X')
plt.ylabel('Frequency Density')
plt.legend()
plt.grid(True)


plt.savefig('../images/2c.png')
plt.show()

