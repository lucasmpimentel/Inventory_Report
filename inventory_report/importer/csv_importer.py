from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            result = list(csv_info for csv_info in reader)

        return result
