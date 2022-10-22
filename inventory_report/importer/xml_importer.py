from inventory_report.importer.importer import Importer
from xml.etree import ElementTree


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(path, encoding="utf-8") as file:
            reader = ElementTree.parse(file).getroot()
            result = list(
                {info.tag: info.text for info in xml_info}
                for xml_info in reader
            )

        return result
