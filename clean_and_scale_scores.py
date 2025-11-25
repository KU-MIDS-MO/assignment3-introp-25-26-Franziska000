# 1) clean_and_scale_scores(scores, min_score, max_score)
#   We have exam scores stored in a NumPy array (1D or 2D).
#  - First, replace all values smaler than min_score by min_score,
#   and all values larger than max_score by max_score.
# 
#  - Then linearly scale all values to the range [0, 1] using:
#   scaled = (value - min_score) / (max_score - min_score)
#  Return a new NumPy array of floats with the same shape as scores

# 1) clean_and_scale_scores(scores, min_score, max_score)
#   Wir haben Prüfungsergebnisse, gespeichert in einem NumPy-Array (1D oder 2D).
#  - Zuerst: Ersetze alle Werte, die kleiner als min_score sind, durch min_score,
#    und alle Werte, die größer als max_score sind, durch max_score.
# 
#  - Dann: Skaliere alle Werte linear auf den Bereich [0, 1] mit der Formel:
#    skaliert = (wert - min_score) / (max_score - min_score)
#  - Rückgabe: Ein neues NumPy-Array vom Typ float mit derselben Form wie scores


import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    scores = np.array(scores)
    scaled = []
    
    if scores.ndim == 1:
        
        for value in scores:
            if value < min_score:
                value = min_score
            if value > max_score:
                value = max_score
            
            value = float(value - min_score) / float(max_score - min_score)
            
            scaled.append(value)
            
        return np.array(scaled, dtype= float)
    
    else:
        for row in scores:
            new_row = []
            for value in row:
                if value < min_score:
                    value = min_score
                if value > max_score:
                    value = max_score
                
                value = (value - min_score) / (max_score - min_score)
                new_row.append(value)
            scaled.append(new_row)
            
        return np.array(scaled, dtype=float)

    pass

scores = [4, 5, 0]
print(clean_and_scale_scores(scores, 0, 8))