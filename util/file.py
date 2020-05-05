import os
from flask import render_template_string, make_response



# opens a file and writes to it storing the user query and the color 
def writeToFile(dictQuery, rgbcolor):

	# opens file if it exists
	if os.path.exists('Data/fileInfo.txt'):
		file = open('Data/fileInfo.txt', 'r+')
	else:
		file = open('Data/fileInfo.txt', 'w+')
	text = '{}\n{}\n'.format(dictQuery, rgbcolor)
	file.write(text)
	file.close()	
	return text

# returns the file 
def returnFile():
	if os.path.exists('Data/fileInfo.txt'):
		file = open('Data/fileInfo.txt', 'r+')
	else:
		file = open('Data/fileInfo.txt', 'w+')
	text = file.read()
	return text

