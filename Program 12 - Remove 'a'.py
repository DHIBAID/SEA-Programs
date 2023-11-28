with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    output_file.writelines(line for line in input_file if 'a' not in line)
