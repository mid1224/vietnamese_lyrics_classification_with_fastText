import fasttext

model = fasttext.load_model("trained_models/model_1.bin")

# Test accuracy on the validation set
# The output is a tuple: (number_of_samples, precision@1, recall@1)
results = model.test("dataset/dataset.valid")

print(f"Samples: {results[0]}")
print(f"Precision@1: {results[1]}")
print(f"Recall@1: {results[2]}")
