import os


def read_spreadsheet_file(filename: str):
    _, file_extension = os.path.splitext(filename)

    match file_extension:
        case ".csv":
            return _read_csv(filename)
        case ".xlsx":
            return _read_xlsx(filename)
        case _:
            raise ValueError("File with provided format not supported")


def _read_xlsx(filename: str) -> list[tuple]:
    import openpyxl as op

    xlsx_workbook = op.load_workbook(filename)

    first_sheet_name = xlsx_workbook.get_sheet_names()[0]
    sheet = xlsx_workbook.get_sheet_by_name(first_sheet_name)

    sheet_values = list(sheet.values)

    result = []
    for line in sheet_values[3:]:
        result.append(line[:-2])

    return result


def _read_csv(filename: str) -> list[tuple]:
    import csv

    result = []
    with open(filename) as f:
        for line in csv.reader(f.readlines()[3:], delimiter=","):
            result.append(
                tuple([int(value) if value.isdecimal() else value for value in line])
            )

    return result
