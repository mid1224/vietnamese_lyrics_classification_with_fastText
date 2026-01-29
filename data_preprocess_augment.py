import random
import re
from underthesea import word_tokenize
from collections import Counter

# Set the seed for reproducibility of all random operations
random.seed(42)

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

def augment_sentence_shuffle(line: str) -> str | None:
    """
    Takes a preprocessed line, shuffles its content sentences, and returns a new augmented line.
    """
    stripped = line.strip()
    match = re.match(r"^(__label__\S+)\s+(.*)$", stripped)
    if not match:
        return None

    label, content = match.group(1), match.group(2)
    
    # Split content into words.
    words = content.split()
    if len(words) < 32: # Don't augment very short lines
        return None

    sentences = []
    # Group words into chunks to simulate sentences/lines.
    chunk_size = random.randint(12, 18)
    for i in range(0, len(words), chunk_size):
        sentences.append(" ".join(words[i:i+chunk_size]))

    # Shuffle the sentences
    random.shuffle(sentences)
    
    augmented_content = " ".join(sentences)
    return f"{label} {augmented_content}"

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

# 3. Augment training data based on label frequency
# Count label occurrences
labels = [line.split()[0] for line in train_data if line.strip()]
label_counts = Counter(labels)
max_count = max(label_counts.values()) if label_counts else 0

augmented_train_data = []
if max_count > 0:
    for line in train_data:
        label = line.split()[0]
        count = label_counts[label]
        
        # Calculate how many times to augment
        if count < max_count and count > 0:
            num_augmentations = round((max_count / count) - 1)
            
            for _ in range(num_augmentations):
                augmented_line = augment_sentence_shuffle(line)
                if augmented_line:
                    augmented_train_data.append(augmented_line)

# 4. Combine original training data with augmented data and shuffle
final_train_data = train_data + augmented_train_data
random.shuffle(final_train_data)

# 5. Save the final datasets
with open("dataset/dataset.train", "w", encoding="utf-8") as f:
    f.write("\n".join(final_train_data))

with open("dataset/dataset.valid", "w", encoding="utf-8") as f:
    f.write("\n".join(valid_data))

print(f"Created dataset.train ({len(final_train_data)} lines) and dataset.valid ({len(valid_data)} lines).")
print("Training data was augmented. Validation data remains untouched.")

# Optional: Print new label distribution
final_labels = [line.split()[0] for line in final_train_data if line.strip()]
final_label_counts = Counter(final_labels)
print("\nOriginal label distribution:")
print(label_counts)
print("\nNew label distribution after augmentation:")
print(final_label_counts)