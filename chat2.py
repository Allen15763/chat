import os

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip()) #strip=remove \n
    return lines

def convert(lines):
    new = []
    person = None #預設無，則不進行加進字串
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_image_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ') #切完變清單故設s [time name content]
        time = s[0]
        name = s[1]
        if name == 'Allen':
        	if s[2] =='貼圖':
        		allen_sticker_count += 1
        	elif s[2] == '圖片':
        		allen_image_count += 1
        	else:
        	    for m in s[2:]:
        		    allen_word_count += len(m)
        elif name == 'Viki':
        	if s[2] =='貼圖':
        		viki_sticker_count += 1
        	elif s[2] == '圖片':
        		viki_image_count += 1
        	else:
        	    for m in s[2:]:
        		    viki_word_count += len(m)
    print('allen說了', allen_word_count, '、傳了', allen_sticker_count, '個貼圖、', allen_image_count, 'photos')
    print('viki說了', viki_word_count, '、傳了', viki_sticker_count, '個貼圖、', viki_image_count, 'photos')


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    filename = 'LINE-Viki.txt'
    lines = []

    if os.path.isfile(filename): #檢查檔案存在
        print('Found the file！')
        lines = read_file(filename)
    else:
        print('Can not find file！')

    lines = convert(lines)
    #write_file('output.txt', lines)

main()
