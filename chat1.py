
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip()) #strip=remove \n
	return lines

def convert(lines):
	new = []
	person = None #預設無，則不進行加進字串
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #if有person則進行下列
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	filename = 'input.txt'
	lines = read_file(filename)
	lines = convert(lines)
	write_file('output.txt', lines)

main()
