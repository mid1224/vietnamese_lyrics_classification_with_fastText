import fasttext

# Train the model
model = fasttext.train_supervised(
    input="dataset/dataset.train",
    lr=0.2,             # Lower learning rate is often better for OVA
    epoch=25,           # The number of times each examples is seen
    wordNgrams=3,       # N-gram
    bucket=200000,      # allocate space for how many unique vectors for the n-grams.
                        # A larger bucket size allows for more distinct n-gram representations (fewer collisions)
    dim=100,            # Vector embedding dimension
    loss='softmax',     # Use used loss function
)

# Non-augmented: lr=0.5, ngram=2
# Augmented: lr=0.2, ngram=3

# model = fasttext.train_supervised(input="dataset/dataset.train", autotuneValidationFile='dataset/dataset.valid', autotuneMetric="f1:__label__life")

# Save the model
model.save_model("trained_models/model_1.bin")

print("Model trained. Saved model_1 to /trained_models")