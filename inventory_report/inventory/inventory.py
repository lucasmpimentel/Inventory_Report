import csv
import json
import xml.etree.ElementTree as ElementTree
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(_, path, report):
        with open(path, "r") as arquivo:

            if ".csv" in path:
                result = list(csv.DictReader(arquivo))
            elif ".xml" in path:
                info = ElementTree.parse(arquivo)
                root = info.getroot()
                result = [
                    {elem.tag: elem.text for elem in child} for child in root
                ]
            elif ".json" in path:
                result = json.load(arquivo)

        if report == "completo":
            return CompleteReport.generate(result)

        return SimpleReport.generate(result)
