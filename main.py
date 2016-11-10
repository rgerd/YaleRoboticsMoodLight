import os.path

from flask import Flask
app = Flask(__name__)

def readFile(fileName):
    filePtr = open(fileName, 'r')
    contents = filePtr.read()
    return contents

@app.route("/")
def showIndex():
    return showPage("index");

@app.route("/<pageName>")
def showPage(pageName):
    if(os.path.isfile(pageName)):
        return readFile(pageName)
    return getCode(pageName, "index.html");

@app.route("/web/<pageName>/<fileName>")
def getCode(pageName, fileName):
    return readFile("web/" + pageName + "/" + fileName)

if __name__ == "__main__":
  app.run()
