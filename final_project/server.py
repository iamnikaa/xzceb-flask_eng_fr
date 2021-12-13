"""Server side implementation of language translator webpage using flask"""
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/englishToFrench")
def englishToFrench():
    """Configures route for english to french button"""
    textToTranslate = request.args.get('textToTranslate')
    if textToTranslate != "":
        return translator.englishToFrench(textToTranslate)
    else:
        return "Invalid Input"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    """Configures route for french to english button"""
    textToTranslate = request.args.get('textToTranslate')
    if textToTranslate != "":
        return translator.frenchToEnglish(textToTranslate)
    else:
        return "Invalid Input"

@app.route("/")
def renderIndexPage():
    """Renders homepage"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
