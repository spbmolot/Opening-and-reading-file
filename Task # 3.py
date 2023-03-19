import os

current = os.getcwd()
folder = 'for task 3'
full_path = os.path.join(current, folder)
os.chdir(full_path)

dict_result = {}
quantity_files = 0


def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        quantity_str_f = len(f.readlines())
        dict_result[file] = quantity_str_f


def get_key(dict_result, value):
    for key, v in dict_result.items():
        if v == value:
            return key


for file in os.listdir():
    if file.endswith(".txt"):
        quantity_files += 1
        read_text_file(f"{full_path}\{file}")


with open('total.doc', 'w+', encoding='utf-8') as t:
    for i in range(quantity_files):
        key_ = get_key(dict_result, min(dict_result.values()))
        with open(key_, 'r+', encoding='utf-8') as f:
            t.write(key_ + '\n')
            t.write(str(min(dict_result.values())) + '\n')
            t.write(f.read() + '\n')
            dict_result.pop(key_)
    t.seek(0)
    print(t.read())