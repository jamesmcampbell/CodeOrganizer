from pathlib import Path
from re import split


def parse_brackets(word_list):
    # line is an array of all the words in the given line
    global bracket

    for x in range(0, len(word_list)):
        word_list[x] = str(word_list[x].strip())
        if '}' not in word_list[x] and '{' not in word_list[x] and word_list[x] != '':
            output_file.write('\n' + '\t'*bracket + word_list[x])
            # print(word_list[x])
        elif word_list[x] == '}':
            bracket -= 1
            output_file.write('}')
        elif '{' in word_list[x]:
            bracket += 1
            output_file.write(' {')


original_file = Path(input("\nSpecify your file's location (folder/directory path including the file name)"
                       "\n   For example (for Windows) - C:\\Users\\James\\Documents\\Python\\style.css: "))
#This line is for testing purposes, so I can input the path directly into the code so I don't have to type it in when I run it
#original_file = Path('style.css')

raw_text = original_file.read_text()
original_list = raw_text.split('\n')

output_file = open('boxified_' + original_file.name, 'w')

bracket = 0

for x in range (0, len(original_list)):
    if len(original_list[x]) != 0:
        if '}' not in original_list[x] and '{' not in original_list[x]:
            # print(no_spaces(original_list[x]))
            output_file.write('\n' + '\t'*bracket + original_list[x].strip())
            # print(no_spaces(original_list[x]))
        else:
            line_list = split(r"([{}])", original_list[x])
            # print(line_list)
            parse_brackets(line_list)
    else:
        output_file.write('\n')
