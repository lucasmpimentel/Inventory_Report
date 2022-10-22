import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    if sys.argv[1].endswith(".csv"):
        inventory_refactor = InventoryRefactor(CsvImporter)
        print(inventory_refactor.import_data(sys.argv[1], sys.argv[2]), end="")
    elif sys.argv[1].endswith(".json"):
        inventory_refactor = InventoryRefactor(JsonImporter)
        print(inventory_refactor.import_data(sys.argv[1], sys.argv[2]), end="")
    elif sys.argv[1].endswith(".xml"):
        inventory_refactor = InventoryRefactor(XmlImporter)
        print(inventory_refactor.import_data(sys.argv[1], sys.argv[2]), end="")
    else:
        print("Erro de leitura")


# Gostaria de deixar o meu agradecimento a todos os colegas que me ajudaram a
# desenvolver esse projeto, juntamente com as indicações de pesquisa abaixo
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
