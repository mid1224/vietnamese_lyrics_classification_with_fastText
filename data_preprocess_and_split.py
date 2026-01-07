import random
import re
from underthesea import word_tokenize

def preprocess_vietnamese_lyrics(text: str) -> str:
    # 1. Lowercase
    text = text.lower()
    # 2. Remove special characters (keep underscores/letters/digits/space)
    text = re.sub(r"[^\w\s]", "", text)
    # 3. Word segmentation (underscores for compounds)
    text = word_tokenize(text, format="text")
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

# Read the full dataset
with open("dataset/raw_dataset.txt", "r", encoding="utf-8") as f:
    raw_lines = f.readlines()

# Preprocess each non-empty line
processed_lines = []
for line in raw_lines:
    processed = preprocess_line(line)
    if not processed:
        continue
    processed_lines.append(processed + "\n")

# Shuffle lines deterministically for reproducibility
random.seed(42)
random.shuffle(processed_lines)

# Split the data ~80/20 (1783 for training, 400 for validation, total 2103)
train_data = processed_lines[:1703]
valid_data = processed_lines[1703:2103]

# Save the training file
with open("dataset/dataset.train", "w", encoding="utf-8") as f:
    f.writelines(train_data)

# Save the validation file
with open("dataset/dataset.valid", "w", encoding="utf-8") as f:
    f.writelines(valid_data)

print(f"Created dataset.train ({len(train_data)} lines) and dataset.valid ({len(valid_data)} lines).")