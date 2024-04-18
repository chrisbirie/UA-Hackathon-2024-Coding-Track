import unittest
import os
from openpyxl import load_workbook
from hackathon_data.excel_utils import create_excel_workbook 

class TestCreateExcelWorkbook(unittest.TestCase):
    def test_create_excel_workbook(self):
        # Define the test file name
        test_filename = 'test_output.xlsx'

        # Mock data
        data = [
            ["user1", "John Doe", "Exercise1", "Python", "2024-04-18 12:00:00", "8 kyu", 50],
            ["user2", "Jane Smith", "Exercise2", "Java", "2024-04-18 13:00:00", "7 kyu", 40]
        ]

        # Call the function
        workbook = create_excel_workbook(test_filename, data)

        # Assertions
        self.assertTrue(os.path.exists(test_filename))  # Check if the file was created

        # Read the Excel file using openpyxl
        workbook = load_workbook(filename=test_filename)
        sheet = workbook.active

        # Ensure headers are correct
        headers = ["Username", "Full Name", "Exercise", "Languages", "Ended At", "Rank", "Score"]
        for col_num, header in enumerate(headers, start=1):
            self.assertEqual(sheet.cell(row=1, column=col_num).value, header)

        # Ensure data is correct
        for row_num, row_data in enumerate(data, start=2):
            for col_num, expected_value in enumerate(row_data, start=1):
                self.assertEqual(sheet.cell(row=row_num, column=col_num).value, expected_value)

        # Remove the test file
        os.remove(test_filename)

if __name__ == "__main__":
    unittest.main()