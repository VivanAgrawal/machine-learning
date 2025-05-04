#Term                     Meaning (Simple)
#TP    (True Positive) Model said "Dog", it was Dog ✔️
#FP    (False Positive) Model said "Dog", but it wasn't ❌
#TN    (True Negative) Model said "Not Dog", and it wasn't ❌ ✔️
#FN   (False Negative) Model said "Not Dog", but it was Dog ❌

#Formulas for
#Accuracy = (TP + TN) / Total

#Precision = TP / (TP + FP) → how many predicted positives were correct?

#Recall = TP / (TP + FN) → how many actual positives we caught?

#F1 Score = 2 × (Precision × Recall) / (Precision + Recall)