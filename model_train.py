import fasttext

# Train the model
#model = fasttext.train_supervised(input="dataset.train") # Precision: 0.56

#model = fasttext.train_supervised(
    #input="dataset.train",
    #lr=1.0,           # Learning rate
    #epoch=25,         # Number of epochs
    #wordNgrams=2      # Use word bigrams
#)
# Precision: 0.77

model = fasttext.train_supervised(
    input="dataset/dataset.train",
    lr=0.5,             # Lower learning rate is often better for OVA
    epoch=25,           # The number of times each examples is seen
    wordNgrams=2,       # N-gram
    bucket=200000,      # allocate space for 200000 unique vectors for the n-grams.
                        # A larger bucket size allows for more distinct n-gram representations (fewer collisions) 
                        # but increases the size of the .bin model file.
    dim=300,            # Vector embedding dimension
    loss='ova',         # Use one vs all (ova) loss
    # pretrainedVectors="pretrained_vectors/cc.vi.300.vec" # Minimal improvement
)
# Precision: 0.79 (old dataset with 784 samples)
# Precision: 0.835 (new dataset with 2103 samples)

# Save the model
model.save_model("trained_models/model_1.bin")

print("Model trained. Saved model_1 to trained_models.")