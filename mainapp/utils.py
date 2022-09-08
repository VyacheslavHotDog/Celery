from fpdf import FPDF
from datetime import date


class PdfGenerator:

    def create(self, pdf_data):
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("Sans", style="", fname="font/NotoSans.ttf", uni=True)
        pdf.set_font("Sans")
        pdf.cell(txt="Здравствуйте, изменилось количество товаров!")
        pdf.ln(10)
        pdf.cell(txt="{} : было - {}, стало - {}".format(
            pdf_data['name'], pdf_data['countBefore'], pdf_data['countAfter']))
        pdf.ln(20)
        pdf.cell(txt=str(date.today()))
        st = pdf.output(dest='S')

        return st