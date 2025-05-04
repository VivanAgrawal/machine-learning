actual = ["cat", "dog", "cat", "bird", "dog", "dog", "cat"]

# Model's predicted answers
predicted = ["cat", "dog", "dog", "bird", "cat", "dog", "cat"]

# Count how many predictions are correct
correct = 0

for i in range(len(actual)):
    if actual[i] == predicted[i]:
        correct += 1

# Calculate accuracy
accuracy = (correct / len(actual)) * 100


print("Correct Predictions:", correct)
print("Total Predictions:", len(actual))
print("Accuracy:", round(accuracy, 2), "%")

