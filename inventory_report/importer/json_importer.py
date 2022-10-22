import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(path, encoding="utf-8") as file:
            reader = json.load(file)

        return reader
