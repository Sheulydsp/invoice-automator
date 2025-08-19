import os
import pandas as pd
from extractor import extract_text_from_pdf
from parser import extract_invoice_number, extract_date, extract_total_amount

# The folder where all your sample invoices are stored
INVOICE_DIR = 'invoices'

def main():
    """
    Orchestrates the entire invoice processing pipeline.
    """
    processed_data = [] # A list to hold the data from each invoice

    # Loop through every file in the specified directory
    for filename in os.listdir(INVOICE_DIR):
        if filename.endswith('.pdf'):
            print(f"Processing {filename}...")

            # Create the full path to the PDF file
            pdf_path = os.path.join(INVOICE_DIR, filename)

            # 1. Extract raw text from the PDF
            raw_text = extract_text_from_pdf(pdf_path)

            # 2. Parse the text to get our data points
            invoice_number = extract_invoice_number(raw_text)
            invoice_date = extract_date(raw_text)
            total_amount = extract_total_amount(raw_text)

            # Here you could add validation logic if needed!
            # For now, we will just store the extracted data.

            # 3. Store the structured data
            invoice_data = {
                'filename': filename,
                'invoice_number': invoice_number,
                'invoice_date': invoice_date,
                'total_amount': total_amount
            }
            processed_data.append(invoice_data)

    # 4. Create a DataFrame and save it to a CSV file
    df = pd.DataFrame(processed_data)
    df.to_csv('invoices_summary.csv', index=False)

    print("\nProcessing complete!")
    print("Summary saved to invoices_summary.csv")

if __name__ == '__main__':
    main()