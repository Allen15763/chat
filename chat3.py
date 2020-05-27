import os

def read_file(filename):
	lines = []
	with open('3.txt', 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	for line in lines:
		s = line.split(' ')
		time = s[0][:5] #0取到第5個字；前5
		name = s[0][5:] #從5開始取             ；s[-2:]從後面開始
		print(name, 'sent at', time)



def main():
    filename = '3.txt'
    lines = []

    if os.path.isfile(filename): #檢查檔案存在
        print('Found the file！')
        lines = read_file(filename)
    else:
        print('Can not find file！')

    lines = convert(lines)
    #write_file('output.txt', lines)

main()
