import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

# --- IMPORTANT ---
# If you are on Windows, you may need to tell pytesseract where to find the Tesseract engine.
# Uncomment the line below and set the path to where you installed Tesseract.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF using a hybrid approach.
    First, it tries to extract text directly (for digital PDFs).
    If that fails, it uses OCR to extract text from the PDF images (for scanned PDFs).
    """
    
    # --- Method 1: Direct Text Extraction ---
    doc = fitz.open(pdf_path)
    direct_text = ""
    for page in doc:
        direct_text += page.get_text()
    
    # If we found a reasonable amount of text, assume it's a digital PDF and return.
    # The threshold (e.g., 100 characters) can be adjusted.
    if len(direct_text.strip()) > 100:
        print("Successfully extracted text using direct method.")
        return direct_text

    # --- Method 2: OCR for Scanned PDFs ---
    # If direct extraction yields little or no text, proceed with OCR.
    print("Direct text extraction failed, attempting OCR...")
    ocr_text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        
        # Render the page to an image (pixmap)
        pix = page.get_pixmap(dpi=300) # Higher DPI for better OCR accuracy
        
        # Convert the pixmap to a format Pillow can use
        img_data = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_data))
        
        # Use pytesseract to do OCR on the image
        try:
            page_text = pytesseract.image_to_string(image, lang='eng')
            ocr_text += page_text + "\n"
        except pytesseract.TesseractNotFoundError:
            return "TESSERACT_ERROR: Tesseract is not installed or not in your PATH. Please check your installation."

    return ocr_text

if __name__ == '__main__':
    # You will need to find a scanned/image-based PDF to test this part.
    # Replace 'scanned_invoice.pdf' with the actual name of your scanned file.
    scanned_invoice_path = 'invoices/scanned_invoice.pdf' 
    
    print(f"\n--- Testing Scanned PDF: {scanned_invoice_path} ---")
    print(extract_text_from_pdf(scanned_invoice_path))
