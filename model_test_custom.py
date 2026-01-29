import fasttext
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the pre-trained model
model = fasttext.load_model("trained_models/model_1.bin")

# Path to the validation dataset
validation_file_path = "dataset/dataset.valid"

y_true = []
y_pred = []

# Manually test the model on the validation set
with open(validation_file_path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        # Split the line into the label and the text
        parts = line.split(' ', 1)
        true_label = parts[0]
        text = parts[1]

        y_true.append(true_label)

        # Predict the label for the text
        prediction = model.predict(text, k=1)
        predicted_label = prediction[0][0]
        y_pred.append(predicted_label)

# --- METRICS CALCULATION ---

# 1. Accuracy
# The proportion of correct predictions among the total number of cases processed.
accuracy = accuracy_score(y_true, y_pred)
print(f"Overall Accuracy: {accuracy:.4f}\n")

# 2. Classification Report
# This report shows the main classification metrics on a per-class basis.
# - Precision: The ability of the classifier not to label as positive a sample that is negative.
# - Recall (Sensitivity): The ability of the classifier to find all the positive samples.
# - F1-Score: A weighted average of the precision and recall.
# - Support: The number of actual occurrences of the class in the specified dataset.
# - Macro Avg: Computes the metric independently for each class and then takes the average (treating all classes equally).
# - Weighted Avg: Computes the metric for each class, and finds their average, weighted by support.
print("Classification Report:")
print(classification_report(y_true, y_pred, zero_division=0, digits=4))


# 3. Confusion Matrix
# A table used to describe the performance of a classification model.
# It shows the number of correct and incorrect predictions for all classes.
labels = sorted(list(set(y_true)))
cm = confusion_matrix(y_true, y_pred, labels=labels)

# Optional: Plot the confusion matrix for better visualization
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.title('Confusion Matrix')
plt.ylabel('Actual Labels')
plt.xlabel('Predicted Labels')
plt.savefig('confusion_matrix.png')
print("Confusion matrix saved to confusion_matrix.png")