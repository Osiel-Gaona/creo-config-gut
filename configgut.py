import os


def name(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)  
    return  mainString

os.system('cls')
f = open('config_A.pro', 'r', encoding='utf8')
k = open('main.txt', 'w+', encoding='utf8')
line = f.readline()

while line:
	for i in line:
		if 'mapkey' not in line:
			if line.split() != []:
				k.write(line)
		if 'mapkey ' in line:
			b = name(line.split(' ')[1]+'.txt',['*','"',"'",'/','\\',':',';',','],'-')
			a = open(b, 'a')
			a.write(line)
		elif 'mapkey(continued)' in line:
			a.write(line)
				




		line = f.readline()
f.close()
k.close()