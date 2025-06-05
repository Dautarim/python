
# motrar algo na tela
# print("olá mundo")
# print(10*20)

# # calcular
# n1 = int(input("digite um numero"))
# n2 = int(input("digite outro numero"))
# print(n1+n2)

# # condicionador
# n3 = n1+n2
# if n3 >= 10:
#     print("mais que me")
# else:
#     print("tá com medo de numeros?")

# repetidor

beldas = [
    {
        "nome": "Larissa Monteiro",
        "idade": 27,
        "ultimo_encontro": "2025-05-20",
        "tempo_relacionamento": "1 ano e 3 meses"
    },
    {
        "nome": "Camila Duarte",
        "idade": 30,
        "ultimo_encontro": "2025-06-01",
        "tempo_relacionamento": "2 anos"
    },
    {
        "nome": "Jéssica Carvalho",
        "idade": 24,
        "ultimo_encontro": "2025-04-15",
        "tempo_relacionamento": "6 meses"
    },
    {
        "nome": "Bianca Almeida",
        "idade": 29,
        "ultimo_encontro": "2025-05-10",
        "tempo_relacionamento": "3 anos e 2 meses"
    },
    {
        "nome": "Tatiane Souza",
        "idade": 26,
        "ultimo_encontro": "2025-05-28",
        "tempo_relacionamento": "8 meses"
    }
]

for item in beldas:
    print(item["nome"])