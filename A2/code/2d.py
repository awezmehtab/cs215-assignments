import numpy as np
import matplotlib.pyplot as plt

def galton_board(h):
    position = 0
    for i in range(0,h):
        position += np.random.choice([-1,1],1,p=[0.5,0.5])
    return position

N = 1000
heights = [10,50,100]

for idx,h in enumerate(heights):
    freq = np.zeros(2*h+1)
    for i in range(N):
        freq[galton_board(h)+h]+=1
    plt.figure()
    plt.bar(range(-h, h+1), freq, align='center')
    plt.xlabel('Final Position')
    plt.ylabel('Probability')
    plt.title(f'Distribution for h = {h}')
    if idx == 0:
        plt.savefig('../images/2d1.png')
    elif idx == 1:
        plt.savefig('../images/2d2.png')
    else:
        plt.savefig('../images/2d3.png')
    plt.show()
