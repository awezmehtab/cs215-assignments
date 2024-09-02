# Satyam Sinoliya, 23B0958
# Vaibhav Singh, 23B1068
# Shaik Awez Mehtab, 23B1080
# Problem number 2, task C

# Importing the libraries
import numpy as np
from scipy.stats import norm 
import matplotlib.pyplot as plt
import seaborn as sb

N = int(1e5)

def sample(loc, scale):
    x = np.random.uniform(0, 1, N)
    F_X_inverse = norm.ppf(x, loc=loc, scale=scale)
    return F_X_inverse

# Define the four parameter choices for (mean, variance)
params = [(0, 0.2), (0, 1.0), (0, 5.0), (-2, 0.5)]
samples = [sample(mu, sigma) for mu, sigma in params]

# Step 4: Plot the results
x = np.linspace(-5, 5, 1000)
plt.figure(figsize=(10, 6))

for (mu, sigma), samplei in zip(params, samples):
    n,x,_ = plt.hist(samplei,1000,histtype=u'step')
    bin_centers = 0.5*(x[1:]+x[:-1])
    sb.distplot(x, hist=False)
    # plt.plot(bin_centers,n, label=f'μ={mu}, σ={sigma}')

plt.title('Probability Density Functions of Gaussians')
plt.xlabel('X')
plt.ylabel('φ(x)')
plt.legend()
plt.grid(True)
plt.show()

