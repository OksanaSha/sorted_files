def file_to_string(file_name):
    with open(file_name) as file:
        text = file.readlines()
        text_str = file_name + '\n' + str(len(text)) + '\n' + '' \
                                                              ''.join(text)
    return len(text), text_str

file1 = tuple(file_to_string('1.txt'))
file2 = tuple(file_to_string('2.txt'))
file3 = tuple(file_to_string('3.txt'))

all_files = dict(sorted([file1, file2, file3]))

print(all_files)

# with open('new_file.)


