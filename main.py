import datetime

from flask import Flask, render_template, url_for, request
import os
import controllers as con
from docx2pdf import convert
<<<<<<< HEAD

from controllers import merge_Receipt, merge_Contract
=======
from datetime import date
>>>>>>> 9a3e7707b303d368aeb09b0cbafdf0a1f4468532

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
<<<<<<< HEAD
    if TemplateName == "Receipt_Temp":
      if request.method == "POST":
        date = request.form.get("date")
        receipt_no = request.form.get("receiptId")
        seller = request.form.get("Seller")
        address = request.form.get("SAddress")
        address_2 = request.form.get("date")
        city = request.form.get("SCity")
        state = request.form.get("SState")
        phone = request.form.get("SPhone")
        buyer_name = request.form.get("Buyer")
        buyer_address = request.form.get("BAddress")
        buyer_address2 = request.form.get("BAddress2")
        buyer_city = request.form.get("BCity")
        buyer_state = request.form.get("BState")
        buyer_phone = request.form.get("BPhone")
        itemString = request.form.get("Item")
        total_total = request.form.get("Total")
        merge_Receipt(date,address_2,seller, total_total,buyer_state,city,address,phone,buyer_city,state,buyer_name,buyer_address2,buyer_address,receipt_no,buyer_phone,itemString)
    elif TemplateName=="Contract_Temp":
       if request.method == "POST":
         end_date=request.form.get("endDate")
         contract_notes=request.form.get("ContractNotes")
         second_party_notes=request.form.get("SecondPartyNotes")
         first_party_notes=request.form.get("FirstPartyNotes")
         first_party=request.form.get("FirstParty")
         start_date=request.form.get("startDate")
         state=request.form.get("State")
         second_party=request.form.get("SecondParty")
         merge_Contract(end_date, contract_notes, second_party_notes, first_party_notes, first_party, start_date, state, second_party)
    return render_template("TemplateView.html",Template=TemplateName)



=======
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
>>>>>>> 9a3e7707b303d368aeb09b0cbafdf0a1f4468532
