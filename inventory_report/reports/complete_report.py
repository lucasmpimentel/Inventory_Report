from inventory_report.reports.simple_report import SimpleReport
from abc import abstractmethod


class CompleteReport(SimpleReport):
    @abstractmethod
    def generate(list):
        simple_report = SimpleReport.generate(list)
        lista_de_empresas = {}

        for product in list:
            if product["nome_da_empresa"] in lista_de_empresas:
                lista_de_empresas[product["nome_da_empresa"]] += 1
            else:
                lista_de_empresas[product["nome_da_empresa"]] = 1

        complete_report = simple_report + "\nProdutos estocados por empresa:\n"

        for listed in lista_de_empresas.items():
            complete_report += f"- {listed[0]}: {listed[1]}\n"

        return complete_report
