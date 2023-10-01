import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    soft = []
    for i in range(len(L)):
        soft.append(np.exp(L[i]))
    return soft / np.sum(np.exp(L))