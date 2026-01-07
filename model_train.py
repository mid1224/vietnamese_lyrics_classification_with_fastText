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
    epoch=25,
    wordNgrams=2,
    bucket=200000,
    dim=300,
    loss='ova',          # Enable multi-label loss
    pretrainedVectors="pretrained_vectors/cc.vi.300.vec"
)
# Precision: 0.79

# Save the model
model.save_model("trained_models/model_1.bin")

print("Model trained. Saved model_1 to trained_models.")