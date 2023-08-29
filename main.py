from flask import Flask, render_template, url_for
import os

app = Flask(__name__)
doc=[]
image=[]
@app.route("/")
def homepage():
    for filename in os.listdir('static/WorkTemplates'):

        name = (filename.rsplit('.docx', 1))
        doc.append("word1")
    return render_template("Chooser.html",templates=doc)

@app.route("/<string:TemplateName>")
def templatePage(TemplateName):
    return render_template("TemplateView.html")
