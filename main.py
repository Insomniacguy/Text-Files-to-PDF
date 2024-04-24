import fpdf
import pathlib
import glob

pdf = fpdf.FPDF(orientation='p', unit='mm', format='A4')

# extracting filepaths in a list and sorting them
filepaths = glob.glob("TextFiles/*.txt")
print(filepaths)
filepaths.sort()
print(filepaths)

# converting to special path obj and extracting filename without extension using stem property
for filepath in filepaths:
    filename = pathlib.Path(filepath).stem
    filename = filename.title()
    print(filename)
    pdf.add_page()
    pdf.set_font(family='Helvetica', size=12, style='B')
    pdf.cell(50, 12, txt=filename, ln=1)
    # pdf.multi_cell(w=12, h=12, txt=str())

    # get the content of each text file
    with open(filepath, 'r') as file:
        file_contents = file.read()
    # add file_contents to pdf

    pdf.set_font(family='Times', size=10)
    pdf.multi_cell(0, 6, txt=file_contents)

# produce the pdf
pdf.output("PDF/output.pdf")
