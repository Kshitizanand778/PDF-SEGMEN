import os
import pdfplumber
from PyPDF2 import PdfWriter, PdfReader

def segment_pdf(input_pdf_path, output_folder, significant_space_threshold, num_cuts):
    # Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    try:
        # Open the PDF file with pdfplumber for text extraction
        with pdfplumber.open(input_pdf_path) as pdf:
            all_segments = []
            
            # Read the original PDF with PyPDF2
            reader = PdfReader(input_pdf_path)

            # Iterate through each page in the PDF
            for page_number in range(len(pdf.pages)):
                page = pdf.pages[page_number]
                text = page.extract_text()
                if text:
                    lines = text.split('\n')
                    whitespace_gaps = []
                    
                    # Analyze the whitespace between lines
                    for i in range(1, len(lines)):
                        current_line_height = page.height - page.bbox[1] - (page.bbox[3] - page.bbox[1]) / len(lines)
                        previous_line_height = page.height - page.bbox[1] - (page.bbox[3] - page.bbox[1]) / len(lines)
                        
                        # Calculate vertical space between lines
                        space_between = abs(previous_line_height - current_line_height)
                        
                        if space_between > significant_space_threshold:
                            whitespace_gaps.append(i)

                    # Make cuts based on the largest whitespace gaps
                    cuts = sorted(whitespace_gaps, reverse=True)[:num_cuts]
                    
                    # Create segments based on identified cuts
                    start = 0
                    for cut in cuts:
                        segment = '\n'.join(lines[start:cut])
                        all_segments.append(segment)
                        start = cut
                    
                    # Add the remaining lines as the last segment
                    if start < len(lines):
                        all_segments.append('\n'.join(lines[start:]))

    except FileNotFoundError:
        print(f"Error: The file '{input_pdf_path}' was not found.")
        return
    except pdfplumber.exceptions.PDFSyntaxError:
        print(f"Error: The file '{input_pdf_path}' is not a valid PDF.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Save each segment to a new PDF file using PyPDF2
    for i, segment in enumerate(all_segments):
        output_pdf_path = os.path.join(output_folder, f'segment_{i + 1}.pdf')
        writer = PdfWriter()
        
        # Create a new PDF page with the segment text
        try:
            writer.add_page(reader.pages[i])  # Add the corresponding original page
            
            with open(output_pdf_path, 'wb') as output_pdf:
                writer.write(output_pdf)
        
        except IndexError:
            print(f"Warning: Not enough pages in the original PDF to create segment {i + 1}.")
            continue

    print(f"Segmented {len(all_segments)} sections into '{output_folder}'.")

# Main execution block
if __name__ == "__main__":
    try:
        input_pdf_path = input("Enter the path to your input PDF file: ")
        output_folder = input("Enter the path to save segmented PDFs: ")
        
        significant_space_threshold = int(input("Enter significant whitespace threshold (in points): "))
        num_cuts = int(input("Enter number of cuts to make: "))  # Allow user to specify number of cuts

        # Run the segmentation
        segment_pdf(input_pdf_path, output_folder, significant_space_threshold, num_cuts)

    except ValueError:
        print("Invalid input! Please enter numeric values for threshold and number of cuts.")