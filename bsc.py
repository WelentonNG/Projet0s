cesta_de_feira = ['maça', 'limão', 'laranja', 'banana']
cesta_de_feira.sort()

nova_cesta = [
    {
        "nome": "banana",
        "preço": 5.50,
        "stand": "T01",
        "validade": "2 dias"
    },
    {
        "nome": "laranja",
        "preço": 6.50,
        "stand": "T03",
        "validade": "7 dias"
    }
]

for item in nova_cesta:
    print(f"Cesta com o item {item['nome']},custa R$ {item['preço']} ")