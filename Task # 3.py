dict_result = {}

with open('1.txt', 'r', encoding='utf-8') as f1:
    quantity_str_f1 = len(f1.readlines())
    dict_result[quantity_str_f1] = '1.txt'

with open('2.txt', 'r', encoding='utf-8') as f2:
    quantity_str_f2 = len(f2.readlines())
    dict_result[quantity_str_f2] = '2.txt'

with open('3.txt', 'r', encoding='utf-8') as f3:
    quantity_str_f3 = len(f3.readlines())
    dict_result[quantity_str_f3] = '3.txt'

with open('total.txt', 'w+', encoding='utf-8') as t:
    for p in range(1, len(dict_result) + 1):
        with open(dict_result[min(dict_result.keys())], 'r+', encoding='utf-8') as f1:
            t.write(dict_result[min(dict_result.keys())] + '\n')
            t.write(str(min(dict_result)) + '\n')
            t.write(f1.read() + '\n')
            dict_result.pop(min(dict_result))
    t.seek(0)
    print(t.read())