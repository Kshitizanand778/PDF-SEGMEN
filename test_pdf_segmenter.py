import unittest
import os

class TestPDFSegmentation(unittest.TestCase):

    def setUp(self):
        self.input_pdf_path = "applsc.pdf"  # Path to a test PDF file.
        self.output_folder = "numpyArray"
        self.significant_space_threshold = 10
        self.num_cuts = 10
        
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