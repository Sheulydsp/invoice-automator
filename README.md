Automated PDF Invoice Extractor with OCR Support
This project is a powerful Python-based tool designed to automate the extraction of key information from a wide variety of PDF invoices. It addresses the common business challenge of manual data entry by providing a robust, hybrid solution that can handle both digital and scanned (image-based) documents.

The script processes a directory of PDF invoices, intelligently determines the best extraction method (direct text or OCR), and uses a flexible, multi-pattern regex engine to parse key data fields. The final, structured data is saved to a clean CSV summary file, creating a powerful prototype for significant business process automation.

🎯 Key Features
Hybrid Extraction Engine: Automatically uses direct text extraction for digital PDFs and seamlessly switches to Optical Character Recognition (OCR) for scanned or image-based invoices.

Robust & Expandable Parser: Employs a list of multiple regex patterns for each data field, allowing it to handle a wide variety of invoice formats.

Comprehensive Data Extraction: Captures key invoice details, including:

Invoice Number

Invoice Date

Due Date

Total Amount

Shipping Cost

Discounts

Intelligent Total Calculation: Reliably identifies the final total amount by finding the largest monetary value on the page, a method resilient to layout changes.

Structured Output: Aggregates all extracted data into a single, clean invoices_summary.csv file, ready for analysis or system import.

🚀 How to Use
Follow these steps to set up and run the project on your local machine.

1. Prerequisites
Python 3.7+

Tesseract OCR Engine: This is required for processing scanned invoices.

Windows: Download and install from Tesseract at UB Mannheim. Make a note of the installation path.

macOS: brew install tesseract

Linux: sudo apt-get install tesseract-ocr

2. Setup and Installation
a. Clone the repository (or download the files):

git clone https://github.com/your-username/invoice-automator.git
cd invoice-automator

b. Create and activate a virtual environment:

# Create the environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate

c. Install the required libraries:
Create a requirements.txt file by running pip freeze > requirements.txt, then install from it.

pip install -r requirements.txt

3. Running the Script
a. Configure Tesseract Path (Windows Only):
Open the extractor.py file and uncomment the line for pytesseract.pytesseract.tesseract_cmd, ensuring the path points to your Tesseract installation.

b. Add your PDF invoices:
Place all the PDF invoices (both digital and scanned) you want to process into the /invoices directory.

c. Run the main script:

python main.py

d. Check the output:
A new file named invoices_summary.csv will be created in the root directory containing all the extracted data.

📂 Project Structure
invoice-automator/
│
├── invoices/                  # Directory for all input PDF invoices
│
├── extractor.py               # Hybrid module for direct text and OCR extraction
├── parser.py                  # Module with robust regex functions
├── main.py                    # Main script to orchestrate the process
│
├── requirements.txt           # List of project dependencies
├── invoices_summary.csv       # The final, structured output file
└── README.md                  # This file
