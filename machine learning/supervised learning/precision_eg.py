'''Term                     Meaning (Simple)
TP    (True Positive) Model said "Dog", it was Dog ✔️
FP    (False Positive) Model said "Dog", but it wasn't ❌
TN    (True Negative) Model said "Not Dog", and it wasn't ❌ ✔️
FN   (False Negative) Model said "Not Dog", but it was Dog ❌

Formulas for
Accuracy = (TP + TN) / Total

Precision = TP / (TP + FP) → how many predicted positives were correct?

Recall = TP / (TP + FN) → how many actual positives we caught?

F1 Score = 2 × (Precision × Recall) / (Precision + Recall)

Precision:
# Actual correct answers'''

# Actual correct answers
actual = ["dog", "cat", "dog", "dog", "cat", "bird", "dog"]

# What model predicted
predicted = ["dog", "dog", "dog", "cat", "cat", "dog", "dog"]

# Count True Positives (TP), False Positives (FP), True Negatives (TN), and False Negatives (FN)
TP = 0  # Model said dog and it was dog
FP = 0  # Model said dog but it was not dog
TN = 0  # Model said not dog and it was not dog
FN = 0  # Model said not dog but it was dog

for i in range(len(actual)):
    if predicted[i] == "dog":
        if actual[i] == "dog":
            TP += 1
        else:
            FP += 1
    else:  # predicted[i] != "dog"
        if actual[i] != "dog":
            TN += 1
        else:
            FN += 1

# Calculate metrics
total = len(actual)
accuracy = (TP + TN) / total * 100 if total != 0 else 0

precision = (TP / (TP + FP)) * 100 if (TP + FP) != 0 else 0
recall = (TP / (TP + FN)) * 100 if (TP + FN) != 0 else 0
f1_score = (2 * (precision * recall) / (precision + recall)) if (precision + recall) != 0 else 0

# Print results
print("True Positives:", TP)
print("False Positives:", FP)
print("True Negatives:", TN)
print("False Negatives:", FN)
print("Accuracy:", round(accuracy, 2), "%")
print("Precision:", round(precision, 2), "%")
print("Recall:", round(recall, 2), "%")
print("F1 Score:", round(f1_score, 2), "%")