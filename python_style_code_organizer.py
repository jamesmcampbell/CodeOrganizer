from pathlib import Path
from re import split

indent = 0
empty_lines = 0

def write_to_file(original_list, x, new_file):
	global indent
	global empty_lines

	# if neither brackets are in the list
	if '{' not in original_list[x] and '}' not in original_list[x]:
		# simply rewrite the line
		new_file.write('\n'*empty_lines + '\n' + '\t'*indent + original_list[x].strip())
		empty_lines = 0
	# if a bracket is in the list
	else:
		# makes a list where each entry is of either one of the brackets or any other segments of text
		line_list = split(r"([{}])", original_list[x])
		#cycles through the line
		for y in range(0, len(line_list)):
			# this line removes spaces from around each segment of text in the line_list
			# if the entry is only a space, it will become an empty entry, in which case it won't be rewritten
			line_list[y] = str(line_list[y].strip())
			# if the item in the list is not one of the brackets
			if x == 0 and y == 0:
				new_file.write(line_list[y])
			elif '{' != line_list[y] and '}' != line_list[y] and line_list[y] != '':
				# simply rewrite the line
				new_file.write('\n'*empty_lines + '\n' + '\t'*indent + line_list[y])
			elif '{' == line_list[y]:
				indent += 1
				new_file.write(' {')
			elif '}' == line_list[y]:
				indent -= 1
				new_file.write(' }')
		empty_lines = 0

original_file = Path(input("\nWhat is your file's location? (folder/directory path including the file name)"
"\n\nFor example (for Windows)- C:\\Users\\James\\Documents\\example.txt\n\n"))

# stores all the text from the file
raw_text = original_file.read_text()

# makes a list where each entry is a line from the original file
original_list = raw_text.split('\n')

# this will be a new file containing the modified text
# the name will be "new_" followed by the original file name
new_file = open('new_' + original_file.name, 'w')

# this segment of code is for all the rest of the lines in the file
for x in range (0, len(original_list)):
	if indent == 0:
		# this checks if the first line is empty or just spaces
		if original_list[x].strip() == '':
			new_file.write('\n')
		else:
			write_to_file(original_list, x, new_file)
	else:
		if original_list[x].strip() == '':
			empty_lines += 1
		else:
			write_to_file(original_list, x, new_file)
