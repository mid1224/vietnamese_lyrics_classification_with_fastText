import re
from underthesea import word_tokenize

def preprocess_vietnamese_lyrics(text: str) -> str:
    # 1. Lowercase
    text = text.lower()
    # 2. Remove special characters (keep underscores/letters/digits/space)
    text = re.sub(r"[^\w\s]", "", text)
    # 3. Remove digits
    text = re.sub(r"\d+", "", text)
    # 4. Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    # 5. Word segmentation (underscores for compounds)
    # text = word_tokenize(text, format="text")
    return text

def preprocess_line(line: str) -> str:
    """
    Preserve the fastText label prefix (__label__xxx) and preprocess only the content after the label.
    """
    stripped = line.strip()
    if not stripped:
        return ""
    m = re.match(r"^(__label__\S+)\s+(.*)$", stripped)
    if m:
        label, content = m.group(1), m.group(2)
        processed = preprocess_vietnamese_lyrics(content)
        return f"{label} {processed}"
    # No label found; preprocess the whole line
    return preprocess_vietnamese_lyrics(stripped)

# --- Main script ---

# 1. Read and preprocess the raw training data
with open("dataset_raw/dataset_raw_train_clean.txt", "r", encoding="utf-8") as f:
    raw_train_lines = f.readlines()

train_data = []
for line in raw_train_lines:
    processed = preprocess_line(line)
    if processed:
        train_data.append(processed)

# 2. Read and preprocess the raw test/validation data
with open("dataset_raw/dataset_raw_test_clean.txt", "r", encoding="utf-8") as f:
    raw_valid_lines = f.readlines()

valid_data = []
for line in raw_valid_lines:
    processed = preprocess_line(line)
    if processed:
        valid_data.append(processed)

# 3. Save the final datasets
with open("dataset/dataset.train", "w", encoding="utf-8") as f:
    f.write("\n".join(train_data))

with open("dataset/dataset.valid", "w", encoding="utf-8") as f:
    f.write("\n".join(valid_data))

print(f"Created dataset.train ({len(train_data)} lines) and dataset.valid ({len(valid_data)} lines).")
print("Data was preprocessed without augmentation.")