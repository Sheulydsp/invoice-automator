import re

def extract_invoice_number(text):
    """
    Tries a list of regex patterns to find the invoice number.
    Returns the first match found.
    """
    patterns = [
        r"Invoice No[:\s]+([\w-]+)",           # Pattern 1: "Invoice No: 123-ABC"
        r"Invoice #\s*(\d+)"            # Pattern 2: "Invoice #: 123-ABC"
        r"INVOICE\n#\s(\d+)",                  # Pattern 3: "INVOICE" on one line, "# 12345" on the next
        r"Invoice Number[:\s]+([\w-]+)",       # Pattern 4: "Invoice Number: 123-ABC"
        r"Reference[:\s]+([\w-]+)"             # Pattern 5: "Reference: 123-ABC"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1) # Return the first successful match
    
    return None # Return None if no patterns match

def extract_date(text):
    """
    Tries a list of regex patterns to find the invoice date.
    Returns the first match found.
    """
    patterns = [
        r"Date[:\s]+(\d{1,2}/\d{1,2}/\d{4})",   # Pattern 1: "Date: 01/15/2025"
        r"Date[:\s]+(\w+\s\d{1,2},\s\d{4})",  # Pattern 2: "Date: Jan 15, 2025"
        r"([A-Za-z]+\s\d{1,2}\s\d{4})",       # Pattern 3: Just the date itself "Mar 06 2012"
        r"(\d{1,2}-\w+-\d{4})" ,
        r"Invoice Date\s*(\d{2}\/\d{2}\/\d{4})"             # Pattern 4: "15-Jan-2025"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
            
    return None

def extract_due_date(text):
    """
    Tries a list of regex patterns to find the due date.
    Returns the first match found.
    """
    patterns = [
        r"Due Date[:\s]+(\d{1,2}/\d{1,2}/\d{4})",    # Pattern 1: "Due Date: 01/30/2025"
        r"Payment Due[:\s]+(\w+\s\d{1,2},\s\d{4})",# Pattern 2: "Payment Due: Jan 30, 2025"
        r"Pay By[:\s]+(\d{1,2}-\w+-\d{4})"          # Pattern 3: "Pay By: 30-Jan-2025"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
            
    return None

def extract_discount(text):
    """
    Tries to find a discount, either as a percentage or a monetary amount.
    """
    pattern = r"Discount.*?(\(?\d+%\)?|\$?\d+\.\d{2})"
    
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1)
        
    return None

def extract_shipping_cost(text):
    """
    Tries to find the shipping cost.
    """
    pattern = r"Shipping[:\s]+\$?(\d+\.\d{2})"
    
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1) # Return the captured amount
        
    return None

def extract_total_amount(text):
    """
    Finds all monetary values and returns the largest one.
    This is often the most reliable method for finding the total.
    """
    pattern = r"\$?(\d+\.\d{2})" # Finds values like $123.45 or 123.45
    
    
    matches = re.findall(pattern, text)
    
    if matches:
        amounts = [float(match) for match in matches]
        return max(amounts)
        
    return None

if __name__ == '__main__':
    # You can create a sample text block here to test your new patterns
    sample_text = """
    INVOICE
    # 36258
    Date: Jan 15, 2025
    Payment Due: Feb 14, 2025
    Discount (10%): $5.01
    Shipping: $15.00
    Total Due: $50.10
    """
    
    print(f"Invoice Number: {extract_invoice_number(sample_text)}")
    print(f"Invoice Date: {extract_date(sample_text)}")
    print(f"Due Date: {extract_due_date(sample_text)}")
    print(f"Discount: {extract_discount(sample_text)}")
    print(f"Shipping: {extract_shipping_cost(sample_text)}")
    print(f"Total Amount: {extract_total_amount(sample_text)}")

