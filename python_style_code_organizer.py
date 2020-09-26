from pathlib import Path
from re import split

bracket = 0
empty_lines = 0

# this method is just for the first line of the file
# without it an extra, empty line would be created at the start
def first_line(original_list):
	if len(original_list[0]) != 0:
		# if neither brackets are in the list
		if '{' not in original_list[0] and '}' not in original_list[0]:
			output_file.write('\t'*bracket + original_list[0].strip())
		#if a bracket is in the list
		else:
			line_list = split(r"([{}])", original_list[0])
			parse_brackets(line_list)
	else:
		output_file.write('\n')

# this method seperates brackets if there are multiple in 1 line
def parse_brackets(line_list):
	global bracket
	global empty_lines

	#cycles through the line
	for x in range(0, len(line_list)):
		line_list[x] = str(line_list[x].strip())
		# if neither brackets are in the list
		if '{' not in line_list[x] and '}' not in line_list[x] and line_list[x] != '':
			# simply rewrite the line
			output_file.write('\n' + '\t'*bracket + line_list[x])
		if line_list[x] == '}':
			bracket -= 1
			# if bracket != 0:
				# output_file.write('\n'*empty_lines)
			output_file.write(' }')
		elif '{' in line_list[x]:
			bracket += 1
			output_file.write(' {')

original_file = Path(input("\nWhat is your file's location? (folder/directory path including the file name)"
"\n\nFor example (for Windows)- C:\\Users\\James\\Documents\\example.txt\n\n"))

raw_text = original_file.read_text()
# a list of every line from the original file
original_list = raw_text.split('\n')

output_file = open('new_' + original_file.name, 'w')

# this method is just for the first line of the file
# without it an extra, empty line would be created at the start
first_line(original_list)

for x in range (1, len(original_list)):
	if len(original_list[x]) != 0:
		# if neither brackets are in the list
		if '{' not in original_list[x] and '}' not in original_list[x]:
			# simply rewrite the line
			output_file.write('\n' + '\t'*bracket + original_list[x].strip())
		# if a bracket is in the list
		else:
			# makes a list of all words in the line that are not brackets
			line_list = split(r"([{}])", original_list[x])
			parse_brackets(line_list)
	elif bracket != 0:
		output_file.write('\n')
