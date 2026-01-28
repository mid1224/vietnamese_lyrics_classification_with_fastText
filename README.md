# vietnamese_lyrics_classification_with_fastText

- Chay data_preprocess.py de tao data khong tang cuong (Sua ten file o dong 31 va 41 de thay dataset)
- Chay data_preprocess_augment.py de tao data co tang cuong (Sua ten file o dong 62 va 72 de thay dataset)

How to build model:
- Run "python3 model_train.py"

Trained model will be stored inside "trained_models" folder.

Toi uu model:
- Chinh sua cac tham so trong model_train.py
- Sua dong 86-104 trong data_preprocess_augment.py chinh sua tang cuong

Run "python3 model_test_single.py" or "python3 model_test_dataset_valid.py" to test.