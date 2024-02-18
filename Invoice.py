# -*- coding: utf-8 -*-
import pdfplumber
import pandas as pd
import xlsxwriter
 

with pdfplumber.open('Invoice_K_billing.pdf') as pdf:
    page= pdf.pages[0]
    text = page.extract_text()
    print(text)
    
    
for row in text.split('\n'):
    if row.startswith("Balance Due"):
        balance=row.split()[-1]
        print("Balance: ",balance)
        
    if row.startswith("Subtotal"):
        subtotal=row.split()[-1]
        print("Subtotal: ",subtotal)
    
    if row.startswith("Shipping"):
        shipping=row.split()[2]
        print("shipping: ",shipping)
        
    if row.startswith("Shipping"):
         tax=row.split()[-1]
         print("tax: ",tax)
         
df = pd.DataFrame({'Balance':[balance],
                   'SubTotal':[subtotal],
                   'Shipping':[shipping],
                   'Tax':[tax]  
                   })

writer = pd.ExcelWriter('Invoice_K_billing.xlsx', engine='xlsxwriter')

# write data to the excel sheet
df.to_excel(writer, sheet_name='Sheet1', index=False)

# close file
writer.close()
    
    
        
    
    
    
    
