import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if not file.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(file) as data:
            return json.load(data)
