import fitz # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Opens a PDF file and extracts all text content."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


if __name__ == '__main__':
    # Replace with the actual path to one of your sample invoices
    invoice_path = 'invoices/invoice_Aaron Bergman_36258.pdf'
    extracted_text = extract_text_from_pdf(invoice_path)
    print(extracted_text)