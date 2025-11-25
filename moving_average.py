#3) moving_average(signal, window_size)
#   We want to smooth a 1-D NumPy array using a centered moving average.
#  - signal is a 1-D NumPy array of numbers
#   - window_size is a positive odd integer (1, 3, 5,...).
#   Let k = (window_size - 1) // 2
#   For each index i, consider the indices from max(0, i-k) to min(n-1, i+k),
#   where n is the length of signal, and take the average of those values.
#   Return a new 1-D NumPy array of floats with the same length as signal.



import numpy as np


signal = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90], dtype = float)


def moving_average(signal, window_size):
    
    n = len(signal)
    k = (window_size-1)//2
    result = np.zeros (n, dtype = float)
    
    for i in range (n):
        left = max(0,i-k)
        right = min(n-1, i+k)
        
        total = 0
        average = 0
        
        for j in range (left, right+1):
            total += signal[j]
            
        average = total / (right + 1 - left)
        
        result[i] = average
    
    return result
    pass


smooth_signal = moving_average(signal, 5)


for i in smooth_signal:
    print(i)



#%%


# signal = ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# n = 10
# window_size = 7
# k = (window_size - 1) // 2 = 3

#   For each index i, consider the indices from max(0, i-k) to min(n-1, i+k),
#   where n is the length of signal, and take the average of those values.
#   Return a new 1-D NumPy array of floats with the same length as signal.

# i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# FROM max(0, i-k) =>
#     0, 0, 0, 0, 1, 2, 3, 4, 5, 6
# TO min(n-1, i+k) =>
#     3, 4, 5, 6, 7, 8, 9, 9, 9, 9



