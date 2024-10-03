Done By Ashish

# PDF Segmentation Application

This Python application segments a system-generated PDF into distinct sections based on whitespace between blocks of text. It identifies logical sections such as headings and paragraphs and saves them as separate PDF files.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [How to Run the Application](#how-to-run-the-application)
- [Examples of Usage](#examples-of-usage)
- [Unit Tests](#unit-tests)

## Setup Instructions

1. **Install vs code and python in it**:
    

2. **Install Required Packages**:
    # Make sure you have Python 3.11 installed.Then install the required libraries using pip:

bash
pip install pdfplumber PyPDF2

## How to Run the Application
Open the Terminal in VS Code if it’s not already open.
Navigate to the Project Directory (if not already there):

bash
cd path/to/your/project/directory


Execute the script with:

bash
python pdfim.py

4. **Run the Application**:
   
   python pdfim.py
   

4. **Follow the Prompts**:
   - Enter the path to the input PDF file.
   - Enter the output folder path.
   - Enter the significant whitespace threshold (in points).
   - Enter the number of cuts.

## Examples of Usage

 **Segmenting a PDF**:
   
   python pdfim.py

   
4. **Provide Input When Prompted**:
 -  Enter the path to your input PDF file.
 -  Enter the path where you want to save segmented PDFs.
 -  Enter the significant whitespace threshold (in points).

   ## Examples of Usage

   ### Example Command-Line Interaction

Enter the path to your input PDF file: C:\Users\Kshit\OneDrive\Desktop\pdff\applsc.pdf
Enter the path to save segmented PDFs: C:\Users\Kshit\OneDrive\Desktop\pdff\numpyArray
Enter significant whitespace threshold (in points): 10 
Enter the number of cuts: 6

## Unit Tests
# This will segment myfile.pdf into multiple PDFs saved in numpyArray folder based on the specified whitespace threshold.

# To ensure that the application works correctly and handles edge cases, unit tests can be created using Python's built-in unittest framework.


# Create a file named test_pdf_segmenter.py in your project directory:


import unittest
import os

class TestPDFSegmentation(unittest.TestCase):

    def setUp(self):
        self.input_pdf_path = "test_input.pdf"   # Path to a test PDF file.
        self.output_folder = "test_output" # Path to the output folder.
        self.significant_space_threshold = 10 # Threshold for significant whitespace.
        self.num_cuts = 6  # Number of cuts to make.

    def test_segment_pdf(self):
        from pdfim import segment_pdf  # Importing the function to be tested.

        # Create test output directory if it doesn't exist.
        os.makedirs(self.output_folder, exist_ok=True)

        # Call the function to be tested.
        
        # Create test output directory if it doesn't exist.
        os.makedirs(self.output_folder, exist_ok=True)

    def test_segment_pdf(self):
        from pdfim import segment_pdf  # Importing segment_pdf from your main script.
        
        # Run segmentation on a test PDF.
        segment_pdf(self.input_pdf_path, self.output_folder, self.significant_space_threshold, num_cuts=5)
        
        # Check if output files are created.
        output_files = os.listdir(self.output_folder)
        self.assertGreater(len(output_files), 0, "No output files were created.")

    def tearDown(self):
        # Clean up: Remove output files after tests.
        for filename in os.listdir(self.output_folder):
            file_path = os.path.join(self.output_folder, filename)
            os.remove(file_path)
        os.rmdir(self.output_folder)

if __name__ == '__main__':
    unittest.main()

# Running Unit Tests

python -m unittest test_pdf_segmenter.py
