#2) count_values_in_bins(data, bin_edges)
#   We want to count how many values fall into each numeric bin.
#   - data is a 1-D NumPy array of numbers.
#   - bin_edges is a 1-D NumPy array of length B+1, strictly increasing.
#   These edges define B bins:
#      Bin 0: [bin_edges[0], bin_edges[1])
#      Bin 1: [bin_edges[1], bin_edges[2])
#      ...
#      Bin B-2: [bin_edges[B-2], bin_edges[B-1])
#      Bin B-1: [bin_edges[B-1], bin_edges[B]]   (last bin is inclusive on the right)
#   Values outside [bin_edges[0], bin_edges[-1]] are ignored.
#   Return a 1-D NumPy array of length B with the counts per bin.

# Wir wollen zählen, wie viele Werte in jedem numerischen „Bin“ (Intervall) liegen.
# Eingaben:
# - data: ein 1D-NumPy-Array mit Zahlen
# - bin_edges: ein 1D-NumPy-Array mit Länge B+1, streng aufsteigend
# Diese Kanten definieren B Intervalle („Bins“)
# Definition der Bins:
#  Bin 0: [bin_edges[0], bin_edges[1]) → inklusive links, exklusiv rechts
#  Bin 1: [bin_edges[1], bin_edges[2])
#  ...
#  Bin B-2: [bin_edges[B-2], bin_edges[B-1])
# Letzter Bin (B-1): [bin_edges[B-1], bin_edges[B]] → inklusive rechts
# Werte außerhalb von [bin_edges[0], bin_edges[-1]] werden ignoriert.
# Ausgabe: Ein 1D-NumPy-Array der Länge B, das die Anzahl der Werte pro Bin enthält.

# Ich habe:
# Ein Array mit Zahlen, z. B.:
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Array mit „Bin-Grenzen“ (Intervallgrenzen), z. B.:
# bin_edges = [0, 3, 6, 9]
# Zahlen in 3 Intervalle einordnen:
# Bin	Intervall; Welche Zahlen passen rein?
# 0	[0, 3)	1, 2
# 1	[3, 6)	3, 4, 5
# 2	[6, 9]	6, 7, 8, 9

import numpy as np

data = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], dtype = int)
bin_edges = np.array ([3,5,11,12,16], dtype = int)


B = len(bin_edges) - 1
for b in range(B):
    print(bin_edges[b])
    

data[bin_edges[0]:bin_edges[1]]


def count_values_in_bins(data, bin_edges):
    
    B = len(bin_edges) - 1
    counts = np.zeros(B, dtype = int)

    for b in range(B):
        left = bin_edges[b]
        right = bin_edges[b+1]
        
        if b < B - 1:
            subset = data[(data >= left) & (data < right)]
        else:
            subset = data[(data >= left) & (data <= right)]
            
        counts[b] = len(subset)
        
    return counts            
    pass


bin_counts = count_values_in_bins(data, bin_edges)

print(bin_counts)




