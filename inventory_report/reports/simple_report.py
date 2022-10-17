from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(list):
        lista_de_fabricacoes = []
        lista_de_validades = []
        lista_de_empresas = {}

        for product in list:
            lista_de_fabricacoes.append(
                datetime.strptime(product["data_de_fabricacao"], "%Y-%m-%d")
            )
            lista_de_validades.append(
                datetime.strptime(product["lista_de_validades"], "%Y-%m-%d")
            )
            if product["nome_da_empresa"] in lista_de_empresas:
                lista_de_empresas[product["nome_da_empresa"]] += 1
            else:
                lista_de_empresas[product["nome_da_empresa"]] = 1
        
        fabricacao_antiga = min(lista_de_fabricacoes).date()
        validade_proxima = min(lista_de_validades).date()
        maior_fornecedor = max(lista_de_empresas, key=lista_de_empresas.get)

        return (
            f"Data de fabricação mais antiga: {fabricacao_antiga}\n"
            f"Data de validade mais próxima: {validade_proxima}\n"
            f"Empresa com mais produtos: {maior_fornecedor}\n"
        )
