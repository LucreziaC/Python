from fpdf import FPDF
import pandas as pd


pdf= FPDF(orientation= "P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0) #set 

df= pd.read_csv("topics.csv")

for index, row in df.iterrows():
        
    #set the header for 1st page
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100,100,100) #RGB color
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln = 1)
    pdf.line(10, 22, 200,22)
    
    #set the footer for 1st page
    pdf.ln(260) # add 260 mm
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100,100,100) #RGB color
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln = 1)
    
    #add pages
    for numR in range(row["Pages"]-1):
        pdf.add_page()
        #set the footer
        pdf.ln(272) # add 260 mm + 12 mm (font size)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100,100,100) #RGB color
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln = 1)    
    





pdf.output("output.pdf")