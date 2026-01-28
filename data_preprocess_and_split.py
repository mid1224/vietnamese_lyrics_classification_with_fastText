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
    if len(words) < 16: # Don't augment very short lines
        return None

    sentences = []
    # Group words into chunks to simulate sentences/lines.
    chunk_size = random.randint(8, 15)
    for i in range(0, len(words), chunk_size):
        sentences.append(" ".join(words[i:i+chunk_size]))

    # Shuffle the sentences
    random.shuffle(sentences)
    
    augmented_content = " ".join(sentences)
    return f"{label} {augmented_content}"


# --- Main script ---

# 1. Read and preprocess the raw training data
with open("dataset/dataset_raw_train.txt", "r", encoding="utf-8") as f:
    raw_train_lines = f.readlines()

train_data = []
for line in raw_train_lines:
    processed = preprocess_line(line)
    if processed:
        train_data.append(processed)

# 2. Read and preprocess the raw test/validation data
with open("dataset/dataset_raw_test.txt", "r", encoding="utf-8") as f:
    raw_valid_lines = f.readlines()

valid_data = []
for line in raw_valid_lines:
    processed = preprocess_line(line)
    if processed:
        valid_data.append(processed)

# 3. Augment ONLY the training data, creating 2 augmented versions for each original
augmented_train_data = []
for line in train_data:
    # Create the first augmented version
    augmented_line_1 = augment_sentence_shuffle(line)
    if augmented_line_1:
        augmented_train_data.append(augmented_line_1)
    
    # Create the second augmented version
    augmented_line_2 = augment_sentence_shuffle(line)
    if augmented_line_2:
        augmented_train_data.append(augmented_line_2)

# 4. Combine original training data with augmented data and shuffle
final_train_data = train_data + augmented_train_data
random.seed(42)
random.shuffle(final_train_data)

# 5. Save the final datasets
with open("dataset/dataset.train", "w", encoding="utf-8") as f:
    f.write("\n".join(final_train_data))

with open("dataset/dataset.valid", "w", encoding="utf-8") as f:
    f.write("\n".join(valid_data))

print(f"Created dataset.train ({len(final_train_data)} lines) and dataset.valid ({len(valid_data)} lines).")
print("Training data was augmented. Validation data remains untouched.")