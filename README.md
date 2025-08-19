Automated PDF Invoice Extractor
This project is a Python-based tool designed to automate the extraction of key information from PDF invoices. It addresses the common business challenge of manual data entry, which is often slow, repetitive, and prone to human error.

The script processes a directory of PDF invoices, extracts crucial data points such as the invoice number, date, and total amount, and then structures this information into a clean, ready-to-use CSV summary file. This serves as a powerful prototype for business process automation and operational efficiency.

🎯 Key Features
Automated Text Extraction: Reads text content directly from multiple PDF files.

Intelligent Data Parsing: Uses tailored regular expressions to find and extract specific data fields, even from unstructured text.

Robust Data Handling: Implements flexible strategies (e.g., finding the largest monetary value for the total) to handle variations in invoice layouts.

Structured Output: Aggregates the extracted data from all processed invoices into a single, clean invoices_summary.csv file.

Modular Codebase: The project is organized into logical modules for extraction, parsing, and orchestration, making it easy to understand and extend.

🚀 How to Use
Follow these steps to set up and run the project on your local machine.

1. Prerequisites
   Python 3.7+

2. Setup and Installation
   a. Clone the repository (or download the files):

git clone https://github.com/Sheulydsp/invoice-automator.git
cd invoice-automator

b. Create and activate a virtual environment:
This keeps the project's dependencies isolated.

# Create the environment

python -m venv venv

# Activate on macOS/Linux

source venv/bin/activate

# Activate on Windows

venv\Scripts\activate

c. Install the required libraries:

pip install -r requirements.txt

(Note: You will need to create a requirements.txt file by running pip freeze > requirements.txt in your active venv).

3. Running the Script
   a. Add your PDF invoices:
   Place all the PDF invoices you want to process into the /invoices directory.

b. Run the main script:
Execute the main.py script from the root of the project folder.

python main.py

c. Check the output:
Once the script finishes, a new file named invoices_summary.csv will be created in the root directory containing all the extracted data.

📂 Project Structure
invoice-automator/
│
├── invoices/ # Directory for all input PDF invoices
│ ├── sample_invoice_1.pdf
│ └── ...
│
├── venv/ # Virtual environment folder
│
├── extractor.py # Module to extract raw text from PDFs
├── parser.py # Module containing regex functions to parse text
├── main.py # Main script to orchestrate the entire process
│
├── invoices_summary.csv # The final, structured output file
└── README.md # This file

extractor.py: Contains the extract_text_from_pdf() function, which uses the PyMuPDF library to read and return the text content of a PDF file.

parser.py: Contains the specialized functions (extract_invoice_number(), extract_date(), etc.) that use regular expressions to find and return specific data points from the raw text.

main.py: The entry point of the application. It iterates through the /invoices folder, calls the extractor and parser for each file, and saves the results to a CSV file using the pandas library.

💡 Future Improvements
Add OCR Support: Integrate an Optical Character Recognition (OCR) library like pytesseract to handle scanned or image-based invoices.

Expand Regex Patterns: Increase the robustness of the parser by adding more regex patterns to support a wider variety of invoice formats.

Build a Simple UI: Develop a simple web interface using Flask or Streamlit to allow users to upload invoices and view the results in their browser.
