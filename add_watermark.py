import PyPDF2
import sys


def add_watermark(input_pdf, watermark_pdf, output_pdf):
    """
    Add a watermark to a PDF file.

    Args:
        input_pdf (str): The path to the input PDF file.
        watermark_pdf (str): The path to the watermark PDF file.
        output_pdf (str): The path to the output PDF file.

    Returns:
        Watermarked PDF
    """
    # Open the input PDF and watermark PDF files in read mode
    with open(input_pdf, 'rb') as pdf_file, open(watermark_pdf, 'rb') as watermark_file:
        # Create PDF reader and writer objects
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()

        # Load the watermark page as a PDF object
        watermark_page = PyPDF2.PdfFileReader(watermark_file).getPage(0)

        # Iterate through each page of the input PDF and add the watermark
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            page.mergePage(watermark_page)
            pdf_writer.addPage(page)

        # Save the modified PDF to the output file
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

# User input
if __name__ == "__main__":
    try:
        print('Add watermark to PDF')
        print('first argument: input PDF, second argument: watermark PDF, third argument: output PDF')
        input_pdf = sys.argv[1]          # Replace with your input PDF file
        watermark_pdf = sys.argv[2]      # Replace with your watermark PDF file
        output_pdf = sys.argv[3]        # Replace with your desired output file name
        print(f'DONE!!! Combined {input_pdf} and {watermark_pdf} into watermarked version of {output_pdf}')
    except IndexError as err:
        print('Please enter the input PDF, watermark PDF, and output PDF as arguments: ', err)
        quit()

    add_watermark(input_pdf, watermark_pdf, output_pdf)
