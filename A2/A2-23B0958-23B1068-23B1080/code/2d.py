import numpy as np
import matplotlib.pyplot as plt

def galton_board(h, N):
    steps = np.random.choice([-1, 1], size=(N, h))
    positions = np.sum(steps, axis=1)
    return positions

N = 100000
heights = [10, 50, 100]


for idx, h in enumerate(heights):
    positions = galton_board(h, N)
    freq, bins = np.histogram(positions, bins=np.arange(-h, h+2), density=True)
    
    plt.figure()
    plt.bar(bins[:-1], freq, align='center', width=1)
    plt.xlabel('Final Position')
    plt.ylabel('Probability')
    plt.title(f'Distribution for h = {h}')
    
    plt.savefig(f'../images/2d{idx+1}.png')
    plt.show()
