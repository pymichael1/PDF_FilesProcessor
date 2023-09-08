import PyPDF2
import sys

input = sys.argv[1:]
output = sys.argv[2:]

def pdf_combiner(pdf_files):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_files:
        print(pdf)
        merger.append(pdf)
    merger.write('superpdf.pdf')
    print('All PDFs merged')
