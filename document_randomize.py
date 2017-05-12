import numpy as np

file_input = open('dataset/twitter-fix', 'r')
file_output = open('dataset/twitter', 'w')

lines = file_input.read().split('\n')
np.random.shuffle(lines)

i = 0

for line in lines:
	
	if i < len(lines):
		file_output.write(line + '\n')
	else:
		file_output.write(line)

	i += 1

file_input.close()
file_output.close()