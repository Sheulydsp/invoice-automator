import re
from extractor import extract_text_from_pdf


def extract_invoice_number(text):
    """Finds and returns the invoice number using regex."""
    # This pattern looks for "Invoice Number", "Invoice No", etc., followed by a number.
    # The ([\w-]+) part is a "capturing group" that grabs the actual number.
    pattern = r"INVOICE\n#\s(\d+)"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def extract_date(text):
    """
    Finds and returns the invoice date by looking for a 'Month Day Year' format.
    This is more reliable than using the 'Date:' label for this document.
    """
    # This pattern looks for a word (month), followed by a space, 
    # one or two digits (day), a space, and four digits (year).
    pattern = r"([A-Za-z]+\s\d{1,2}\s\d{4})"
    
    match = re.search(pattern, text)
    
    if match:
        # group(0) returns the entire matched string
        return match.group(0)
        
    return None

def extract_total_amount(text):
    """
    Finds all monetary values on the invoice and returns the largest one,
    which is typically the final total.
    """
    # This pattern finds all instances of a dollar sign followed by a number
    pattern = r"\$(\d+\.\d{2})"
    
    # re.findall() gives us a list of all matches
    matches = re.findall(pattern, text)
    
    if matches:
        # The matches are strings (e.g., ['50.10', '48.71', '9.74', '11.13']).
        # We need to convert them to numbers (floats) to find the largest.
        amounts = [float(match) for match in matches]
        
        # Return the highest value we found
        return max(amounts)
        
    return None





if __name__ == '__main__':
    # Use the same invoice path from the previous module
    invoice_path = 'invoices/invoice_Aaron Bergman_36258.pdf'

    # 1. Extract the raw text
    raw_text = extract_text_from_pdf(invoice_path)

    # 2. Call your parsing functions
    invoice_number = extract_invoice_number(raw_text)
    invoice_date = extract_date(raw_text)
    total_amount = extract_total_amount(raw_text)

    # 3. Print the results
    print(f"--- Extracted Information for {invoice_path} ---")
    print(f"Invoice Number: {invoice_number}")
    print(f"Invoice Date: {invoice_date}")
    print(f"Total Amount: {total_amount}")