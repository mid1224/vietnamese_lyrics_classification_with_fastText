import random
import re

# Set the seed for reproducibility of all random operations
random.seed(42)

def preprocess_text(text: str) -> str:
    # Lowercase
    text = text.lower()
    # Remove special characters (excluding underscore)
    text = re.sub(r"[^\w\s]", "", text)
    # Remove digits
    text = re.sub(r"\d+", "", text)
    # Remove any extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Preserve the fastText label prefix (__label__xxx) and preprocess only the content after the label.
def preprocess_line(line: str) -> str:
    stripped = line.strip()
    match = re.match(r"^(__label__\S+)\s+(.*)$", stripped)

    label, content = match.group(1), match.group(2)

    processed = preprocess_text(content)
    return f"{label} {processed}"

# Preprocess the raw training data
with open("dataset_raw/dataset_raw_train_clean_trans.txt", "r", encoding="utf-8") as f:
    raw_train_lines = f.readlines()

train_data = []
for line in raw_train_lines:
    processed = preprocess_line(line)
    train_data.append(processed)
random.shuffle(train_data)

# Preprocess the raw test data
with open("dataset_raw/dataset_raw_test_clean_trans.txt", "r", encoding="utf-8") as f:
    raw_valid_lines = f.readlines()

valid_data = []
for line in raw_valid_lines:
    processed = preprocess_line(line)
    valid_data.append(processed)
random.shuffle(valid_data)

# Save preprocessed datasets
with open("dataset/dataset.train", "w", encoding="utf-8") as f:
    f.write("\n".join(train_data))

with open("dataset/dataset.valid", "w", encoding="utf-8") as f:
    f.write("\n".join(valid_data))

print(f"Preprocess completed. Created dataset.train ({len(train_data)} lines) and dataset.valid ({len(valid_data)} lines).")