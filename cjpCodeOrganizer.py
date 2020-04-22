from pathlib import Path
from re import split

bracket = 0
empty_lines = 0

def parse_brackets(word_list):
	global bracket
	global empty_lines

	for x in range(0, len(word_list)):
		word_list[x] = str(word_list[x].strip())
		if '}' not in word_list[x] and '{' not in word_list[x] and word_list[x] != '':
			output_file.write('\n' + '\t'*bracket + word_list[x])
		elif word_list[x] == '}':
			bracket -= 1
			# print(bracket)
			if bracket != 0:
				output_file.write("\n" *empty_lines)
			output_file.write("\n"*second_bracket + ' '*abs(second_bracket-1) + '}')
		elif '{' in word_list[x]:
			bracket += 1
			output_file.write("\n"*first_bracket + ' '*abs(first_bracket-1) + '{')

original_file = Path(input("\nWhat is your file's location? (folder/directory path including the file name)"
"\n\nFor example (for Windows)- C:\\Users\\James\\Documents\\example.txt\n\n"))

style = input("\nWhat coding style do you want? (c, j, p):\n\n"
"C-Style (c) - Brackets in their own lines"
"\nJava Style (j) - First bracket following text, second in it's own line"
"\nPython Style (p) - All brackets following text\n\n")

if style == "c":
	first_bracket = 1
	second_bracket = 1
elif style == "j":
	first_bracket = 0
	second_bracket = 1
elif style == "p":
	first_bracket = 0
	second_bracket = 0

raw_text = original_file.read_text()
original_list = raw_text.split('\n')

output_file = open('new_' + original_file.name, 'w')

for x in range (0, len(original_list)):
	if len(original_list[x]) != 0:
		if '}' not in original_list[x] and '{' not in original_list[x]:
			output_file.write('\n' + '\t'*bracket + original_list[x].strip())
		else:
			line_list = split(r"([{}])", original_list[x])
			parse_brackets(line_list)
	else:
		empty_lines += 1
