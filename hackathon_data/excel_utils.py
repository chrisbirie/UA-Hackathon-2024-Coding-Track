import xlsxwriter

def create_excel_workbook(filename, data):
    # Create a new workbook
    workbook = xlsxwriter.Workbook(filename)

    # Add a worksheet
    worksheet = workbook.add_worksheet()

    # Write headers
    headers = ["Username", "Full Name", "Exercise", "Languages", "Ended At", "Rank", "Score"]
    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header)

    # Write data
    for row_num, row in enumerate(data, start=1):
        for col_num, value in enumerate(row):
            worksheet.write(row_num, col_num, value)

    workbook.close()

    return workbook