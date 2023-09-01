from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def homepage():
    doc = []
    for filename in os.listdir('static/WorkTemplates'):

        size= len(filename)
        name=filename[:size - 5]
        doc.append(name)
    return render_template("Chooser.html",templates=doc)

@app.route("/<string:TemplateName>")
def templatePage(TemplateName):
    return render_template("TemplateView.html")

def returnPDF(ToBeConverted):
    return render_template()