import xlwt
from xlwt import Workbook
import requests

headers = {'content-type': 'application/json', 'x-access-token': "5443b693E341cb0ab695Xb8"}
url = "https://safe-payy.herokuapp.com/api/v1/safepay/querypayment/initiated"

r = requests.get(url=url, headers=headers)
response = r.json()
records = response.get("data")

# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0, 0, 'INITIATED_DATE')
sheet1.write(0, 1, 'PAYMENT_REF')
sheet1.write(0, 2, 'MERCHANT_ID')
sheet1.write(0, 3, 'BUSINESS_NAME')
sheet1.write(0, 4, 'PRODUCT_AMOUNT')

for index, entry in enumerate(records):
    sheet1.write(index+1, 0, entry.get("initiating_date"))
    sheet1.write(index+1, 1, entry.get("paymentref"))
    sheet1.write(index+1, 2, entry.get("merchant_id"))
    sheet1.write(index+1, 3, entry.get("business_name"))
    sheet1.write(index+1, 4, entry.get("product_amount"))

  
wb.save('samson.xls')
