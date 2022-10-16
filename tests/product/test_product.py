from inventory_report.inventory.product import Product


def test_cria_produto():
    result = Product(
        1,
        "Produto Teste",
        "Empresa Fantasma",
        "2022-01-02",
        "2022-12-12",
        "123456",
        "Isso não existe, é só um teste",
    )
    assert result.id == 1
    assert result.nome_do_produto == "Produto Teste"
    assert result.nome_da_empresa == "Empresa Fantasma"
    assert result.data_de_fabricacao == "2022-01-02"
    assert result.data_de_validade == "2022-12-12"
    assert result.numero_de_serie == "123456"
    assert result.instrucoes_de_armazenamento == "Isso não existe, é só um teste"
