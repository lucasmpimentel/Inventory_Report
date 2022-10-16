from inventory_report.inventory.product import Product


def test_relatorio_produto():
    test_product = Product(
        1,
        "Produto Teste",
        "Empresa Fantasma",
        "2022-01-02",
        "2022-12-12",
        "123456",
        "Isso não existe, é só um teste",
    )
    result = test_product.__repr__()
    assert result == (
        f"O produto {test_product.nome_do_produto}"
        f" fabricado em {test_product.data_de_fabricacao}"
        f" por {test_product.nome_da_empresa} com validade"
        f" até {test_product.data_de_validade}"
        f" precisa ser armazenado {test_product.instrucoes_de_armazenamento}."
    )
