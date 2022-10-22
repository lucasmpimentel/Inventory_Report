from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    mock = [
                {
                    "id": "1",
                    "nome_do_produto": "Produto Teste",
                    "nome_da_empresa": "Empresa Fantasma",
                    "data_de_fabricacao": "2022-01-02",
                    "data_de_validade": "2022-12-12",
                    "numero_de_serie": "123456",
                    "instrucoes_de_armazenamento": "Isso é só um teste"
                },
                {
                    "id": "2",
                    "nome_do_produto": "Produto Teste 2",
                    "nome_da_empresa": "Empresa Fantasma",
                    "data_de_fabricacao": "2022-02-02",
                    "data_de_validade": "2023-12-12",
                    "numero_de_serie": "654321",
                    "instrucoes_de_armazenamento": "Isso não existe"
                },
                {
                    "id": "3",
                    "nome_do_produto": "Produto Teste 3",
                    "nome_da_empresa": "Empresa FAKE",
                    "data_de_fabricacao": "2022-03-02",
                    "data_de_validade": "2022-12-11",
                    "numero_de_serie": "456789",
                    "instrucoes_de_armazenamento": "é só um teste"
                }
    ]
    pass_results = {
        "fab": "2022-01-02",
        "val": "2022-12-11",
        "emp": "Empresa Fantasma"
    }

    result = ColoredReport(SimpleReport).generate(mock)

    assert result == (
        f"\033[32mData de fabricação mais antiga:\033[0m \033[36m{pass_results['fab']}\033[0m\n"
        f"\033[32mData de validade mais próxima:\033[0m \033[36m{pass_results['val']}\033[0m\n"
        f"\033[32mEmpresa com mais produtos:\033[0m \033[31m{pass_results['emp']}\033[0m"
    )
