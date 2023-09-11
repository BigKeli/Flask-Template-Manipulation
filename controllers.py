from mailmerge import MailMerge
from datetime import date
from docx2pdf import convert

#'end_date', 'contract_notes',
#'second_party_notes', 'first_party_notes',
#'first_party', 'start_date', 'state', 'second_party', 'today_date'
def merge_Contract(end_date, contract_notes, second_party_notes,
                   first_party_notes, first_party, start_date, state,
                   second_party):
    document = MailMerge("static/WorkTemplates/Contract_Temp.docx")

    doc = document.merge(end_date=end_date, contract_notes=contract_notes, second_party_notes=second_party_notes,
                   first_party_notes=first_party_notes, first_party=first_party, start_date=start_date,
                   state=state, second_party=second_party, today_date="data sot rooopt")
    document.write("static/Contract.docx")
    convert("static/Contract.docx")
#'date', 'address_2', 'seller', 'total_total',
#'buyer_state', 'city', 'total', 'address', 'phone',
#'quantity', 'buyer_city', 'state', 'buyer_name', 'buyer_address2',
#'buyer_address', 'receipt_no', 'item', 'price', 'buyer_phone'
def merge_Receipt(date, address_2, seller, total_total,
                  buyer_state, city, address, phone,
                  buyer_city, state, buyer_name,
                  buyer_address2, buyer_address, receipt_no,
                  buyer_phone, itemString):
    document = MailMerge("static/WorkTemplates/Receipt_Temp.docx")
    document.merge(date=date, address_2=address_2, seller=seller, total_total=total_total,
                    buyer_state=buyer_state, city=city, address=address, phone=phone,
                    buyer_city=buyer_city, state=state, buyer_name=buyer_name,
                    buyer_address2=buyer_address2, buyer_address=buyer_address, receipt_no=receipt_no,
                    buyer_phone=buyer_phone)
    itemList = itemString.split(" ")
    sales_history = []
    for i in range(0, len(itemList) - 2, 3):
        sales_history.append(dict(item=itemList[i], quantity=itemList[i + 1], unitPrice=itemList[i + 2],
                                  total=str(int(itemList[i + 2]) * int(itemList[i + 1]))))
    doc = document.merge_rows('item', sales_history)
    document.write("static/Receipt.docx")
    convert("static/Receipt.docx")
def merge_Week(end_date, name_surname, wednesday, plans_for_next_week, monday,
               tuesday, thursday, issue_notes, start_date, friday, req_prop):
    document = MailMerge("static/WorkTemplates/Weekly_Temp.docx")
    document.merge(end_date=end_date, name_surname=name_surname, wednesday=wednesday, plans_for_next_week=plans_for_next_week,
monday=monday, tuesday=tuesday, thursday=thursday, issue_notes=issue_notes , start_date=start_date,
friday=friday, req_prop=req_prop)
    document.write("static/Week.docx")
    convert("static/Week.docx")
#'end_date', 'name_surname', 'wednesday', 'plans_for_next_week',
# 'monday', 'tuesday', 'thursday', 'issue_notes', 'start_date',
# 'friday', 'req_prop'
def returnPDF(ToBeConverted):
    convert(ToBeConverted, "static/PDF/output.pdf")
