F1 score:

# Actual values
actual = ["dog", "cat", "dog", "dog", "cat", "bird", "dog"]

# Predicted by model
predicted = ["dog", "dog", "dog", "cat", "cat", "dog", "dog"]

# Count TP, FP, FN
TP = 0  # True Positives
FP = 0  # False Positives
FN = 0  # False Negatives

for i in range(len(actual)):
    if predicted[i] == "dog":
        if actual[i] == "dog":
            TP += 1
        else:
            FP += 1
    else:
        if actual[i] == "dog":
            FN += 1

# Calculate Precision and Recall
if (TP + FP) != 0:
    precision = TP / (TP + FP)
else:
    precision = 0

if (TP + FN) != 0:
    recall = TP / (TP + FN)
else:
    recall = 0

# Calculate F1 Score
if (precision + recall) != 0:
    f1_score = 2 * (precision * recall) / (precision + recall)
else:
    f1_score = 0

# Print all results
print("Precision:", round(precision * 100, 2), "%")
print("Recall:", round(recall * 100, 2), "%")
print("F1 Score:", round(f1_score * 100, 2), "%")
