from flask import Flask, render_template, url_for
import os
from docx2pdf import convert


app = Flask(__name__)

@app.route("/")
def homepage():
    doc = []
    # convert("static/WorkTemplates/Contract_Temp.docx", "static/PDF/output.pdf")

    for filename in os.listdir('static/WorkTemplates'):

        size= len(filename)
        name=filename[:size - 5]
        doc.append(name)
    return render_template("Chooser.html",templates=doc)

@app.route("/<string:TemplateName>")
def templatePage(TemplateName):
    return render_template("TemplateView.html",Template=TemplateName)

# def returnPDF(ToBeConverted):
#     convert("static/WorkTemplates/Contract_Temp.docx", "static/PDF/output.pdf")
#
#     return render_template()