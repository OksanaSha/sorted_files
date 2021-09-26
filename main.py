def find_len_file(file_name):
    with open(file_name) as file:
        text = file.readlines()
    return len(text), file_name

def open_file_read(file_name):
    with open(file_name) as file:
        text = file.read()
    return text

file1 = tuple(find_len_file('1.txt'))
file2 = tuple(find_len_file('2.txt'))
file3 = tuple(find_len_file('3.txt'))

all_files = dict(sorted([file1, file2, file3]))

with open('new_file.txt', 'w') as file:
    for len_file, file_name in all_files.items():
        file.write(f'{file_name}\n'
                   f'{len_file}\n'
                   f'{open_file_read(file_name).rstrip()}\n')

with open ('new_file.txt') as file:
    print(file.read())