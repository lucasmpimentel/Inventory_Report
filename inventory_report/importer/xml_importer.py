import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if not file.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(file) as data:
            return xmltodict.parse(data.read())["dataset"]["record"]
