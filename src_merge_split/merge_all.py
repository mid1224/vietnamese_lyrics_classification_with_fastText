input_files = [
    "dataset_merge_label/family_test.txt",
    "dataset_merge_label/love_test.txt",
    "dataset_merge_label/hometown_test.txt",
    "dataset_merge_label/life_test.txt",
    "dataset_merge_label/occasion_test.txt",
    "dataset_merge_label/school_test.txt"
]

output_file = "dataset_merged_test.txt"

def merge():    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in input_files:          
            with open(filename, 'r', encoding='utf-8') as infile:
                content = infile.read()
                
                outfile.write(content)
                
                # Thêm xuống dòng để tránh 2 file bị dính liền nhau
                if not content.endswith('\n'):
                    outfile.write('\n')

    print(f"\n Completed: {output_file}")

merge()