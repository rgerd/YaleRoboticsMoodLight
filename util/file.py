import os

# opens a file and writes to it storing the user query and the color 
def writeToFile(dictQuery, rgbcolor):
	# opens file if it exists
	if os.path.exists('/Data/fileInfo.txt'):
		file = open('/Data/fileInfo.txt', 'r+')
	else:
		file = open('/Data/fileInfo.txt', 'w+')
	file.write('{}\n{}'.format(dictQuery, rgbcolor))
	file.close()



