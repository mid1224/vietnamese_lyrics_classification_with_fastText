import os

data_folder = 'dataset_raw/data_6_school'           
label = '__label__school' 
train_file = 'dataset_merge_label/school_train.txt'   
test_file = 'dataset_merge_label/school_test.txt'     
num_samples_to_take = 100                   

def process_data_fixed_test_size():
    files = [f for f in os.listdir(data_folder)]

    all_data_lines = []

    for file in files:
        path = os.path.join(data_folder, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Gộp dòng, xóa khoảng trắng thừa
        clean_text = content.replace('\n', ' ').strip()
        clean_text = " ".join(clean_text.split())

        # Bỏ qua nếu dưới 50 ký tự
        if len(clean_text) < 50:
            continue

        # Thêm nhãn vào đầu dòng
        line = f"{label} {clean_text}"
        all_data_lines.append(line)

    # data split
    # Lấy 100 bài đầu tiên làm Test
    test_data = all_data_lines[:num_samples_to_take]
    
    # Lấy toàn bộ số còn lại làm Train
    train_data = all_data_lines[num_samples_to_take:]

    # Lưu file Test
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(test_data))
    
    # Lưu file Train
    with open(train_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(train_data))

    print(f"File Test ({test_file}):  {len(test_data)}")
    print(f"File Train ({train_file}): {len(train_data)}")

process_data_fixed_test_size()