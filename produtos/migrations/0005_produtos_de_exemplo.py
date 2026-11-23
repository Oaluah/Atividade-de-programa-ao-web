from django.db import migrations


def adicionar_produtos(apps, schema_editor):
    Produto = apps.get_model("produtos", "Produto")
    Marca = apps.get_model("produtos", "Marca")
    Categoria = apps.get_model("produtos", "Categoria")

    exemplos = [
        ("Café especial", "Café da Serra", "Alimentos", "Café moído de torra média, perfeito para começar o dia.", "32.90", 18),
        ("Caneca de cerâmica", "Casa & Cia", "Casa", "Caneca artesanal para deixar sua pausa mais gostosa.", "39.90", 12),
        ("Bolsa de lona", "Viva Leve", "Acessórios", "Bolsa prática e resistente para acompanhar a rotina.", "79.90", 8),
        ("Vela aromática", "Casa & Cia", "Casa", "Vela com aroma suave para criar um clima aconchegante.", "29.90", 15),
        ("Biscoito artesanal", "Sabor da Vila", "Alimentos", "Biscoitos crocantes feitos em pequenos lotes.", "18.50", 20),
    ]

    for nome, marca_nome, categoria_nome, descricao, preco, estoque in exemplos:
        if Produto.objects.filter(nome=nome).exists():
            continue
        marca, _ = Marca.objects.get_or_create(nome=marca_nome)
        categoria, _ = Categoria.objects.get_or_create(nome=categoria_nome)
        Produto.objects.create(
            nome=nome,
            marca=marca,
            categoria=categoria,
            descricao=descricao,
            preco=preco,
            quantidade_estoque=estoque,
        )


class Migration(migrations.Migration):
    dependencies = [("produtos", "0004_produto_descricao_produto_foto")]

    operations = [migrations.RunPython(adicionar_produtos, migrations.RunPython.noop)]
