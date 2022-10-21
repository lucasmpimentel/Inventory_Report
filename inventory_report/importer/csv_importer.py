from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        with open(path) as file:
            if path.endswith(".csv"):
                return list(csv.DictReader(file))
            else:
                raise ValueError("Arquivo inválido")
