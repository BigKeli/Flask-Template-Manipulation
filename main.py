import datetime

from flask import Flask, render_template, url_for, request
import os
import controllers as con
from docx2pdf import convert
from datetime import date

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

@app.route("/<string:TemplateName>", methods=['GET', 'POST'])
def templatePage(TemplateName):
    if request.method=='POST':
        if request.form['type']==1:
            con.merge_Receipt(datetime.date, request.form['SAddress2'],request.form['Seller'],
            request.form['BState'], request.form['SCity'], request.form['SAddress'], request.form['SPhone'],
            request.form['BCity'], request.form['SState'], request.form['BName'], request.form['BAddress2'],
            0,request.form['BPhone'], request.form['Item'], '' )
    return render_template("TemplateView.html", Template=TemplateName)
# def returnPDF(ToBeConverted):
#     convert("static/WorkTemplates/Contract_Temp.docx", "static/PDF/output.pdf")
#
#     return render_template()