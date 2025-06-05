import json  # Módulo para trabalhar com arquivos JSON
import os    # Módulo para verificar se o arquivo existe

bitches = [
    {
        "nome": "Camila Torres",
        "idade": 27,
        "ultimo_encontro": "2025-05-30",
        "atração": "Aquele olhar safado e a risada que me desmonta.",
        "apelido": "Mila Malvada",
        "tempo_relacionamento": "2 meses"
    },
    {
        "nome": "Bianca Lima",
        "idade": 24,
        "ultimo_encontro": "2025-06-01",
        "atração": "A cintura fina com aquele rebolado hipnotizante.",
        "apelido": "Bibi",
        "tempo_relacionamento": "1 ano"
    },
    {
        "nome": "Juliana Souza",
        "idade": 31,
        "ultimo_encontro": "2025-05-20",
        "atração": "A boca carnuda que sabe o que faz.",
        "apelido": "Ju Delícia",
        "tempo_relacionamento": "3 semanas"
    },
    {
        "nome": "Larissa Mendes",
        "idade": 26,
        "ultimo_encontro": "2025-05-15",
        "atração": "As coxas grossas e aquele olhar de quem manda.",
        "apelido": "Lari Braba",
        "tempo_relacionamento": "4 meses"
    },
    {
        "nome": "Tatiane Rocha",
        "idade": 29,
        "ultimo_encontro": "2025-06-03",
        "atração": "O jeito como geme meu nome, sem pudor.",
        "apelido": "Tati Tentação",
        "tempo_relacionamento": "2 anos"
    },
    {
        "nome": "Fernanda Alves",
        "idade": 22,
        "ultimo_encontro": "2025-05-10",
        "atração": "A pele macia e aquele cheiro que me deixa louco.",
        "apelido": "Fezinha",
        "tempo_relacionamento": "6 meses"
    },
    {
        "nome": "Aline Dias",
        "idade": 25,
        "ultimo_encontro": "2025-05-18",
        "atração": "O quadril que dança até quando caminha.",
        "apelido": "Ali Gostosa",
        "tempo_relacionamento": "8 meses"
    },
    {
        "nome": "Vanessa Martins",
        "idade": 28,
        "ultimo_encontro": "2025-05-22",
        "atração": "As mãos firmes e a língua afiada.",
        "apelido": "Nessa Quente",
        "tempo_relacionamento": "3 anos"
    },
    {
        "nome": "Priscila Castro",
        "idade": 30,
        "ultimo_encontro": "2025-06-02",
        "atração": "A risada maliciosa e o jeito que provoca com o olhar.",
        "apelido": "Prizinha",
        "tempo_relacionamento": "1 mês"
    },
    {
        "nome": "Bruna Oliveira",
        "idade": 23,
        "ultimo_encontro": "2025-05-28",
        "atração": "A voz rouca e o corpo que parece feito sob medida.",
        "apelido": "Bru",
        "tempo_relacionamento": "7 meses"
    },
    {
        "nome": "Gabriela Costa",
        "idade": 27,
        "ultimo_encontro": "2025-05-14",
        "atração": "A forma como me domina sem nem encostar.",
        "apelido": "Gabi Selvagem",
        "tempo_relacionamento": "5 meses"
    },
    {
        "nome": "Patrícia Ramos",
        "idade": 32,
        "ultimo_encontro": "2025-05-26",
        "atração": "As curvas que fazem curva e o jeito atrevido.",
        "apelido": "Paty",
        "tempo_relacionamento": "2 anos e meio"
    },
    {
        "nome": "Renata Silva",
        "idade": 26,
        "ultimo_encontro": "2025-06-01",
        "atração": "O jeito como morde os lábios quando quer algo.",
        "apelido": "Rê Caliente",
        "tempo_relacionamento": "1 ano"
    },
    {
        "nome": "Thaís Morais",
        "idade": 25,
        "ultimo_encontro": "2025-05-19",
        "atração": "A energia louca entre quatro paredes.",
        "apelido": "Tata",
        "tempo_relacionamento": "3 meses"
    },
    {
        "nome": "Isabela Ferreira",
        "idade": 29,
        "ultimo_encontro": "2025-05-30",
        "atração": "O jeito tímido que explode na cama.",
        "apelido": "Isa Fogo",
        "tempo_relacionamento": "4 anos"
    },
    {
        "nome": "Carolina Borges",
        "idade": 21,
        "ultimo_encontro": "2025-05-11",
        "atração": "A ousadia escondida por trás da carinha de anjo.",
        "apelido": "Carolzinha",
        "tempo_relacionamento": "2 semanas"
    },
    {
        "nome": "Jéssica Andrade",
        "idade": 28,
        "ultimo_encontro": "2025-05-23",
        "atração": "O jeito como geme no meu ouvido, só dela.",
        "apelido": "Jessy",
        "tempo_relacionamento": "1 ano e meio"
    },
    {
        "nome": "Letícia Moraes",
        "idade": 24,
        "ultimo_encontro": "2025-05-25",
        "atração": "A bunda empinada e o sorriso malicioso.",
        "apelido": "Leti Louca",
        "tempo_relacionamento": "9 meses"
    },
    {
        "nome": "Andreia Luz",
        "idade": 27,
        "ultimo_encontro": "2025-05-31",
        "atração": "Os olhos que dizem 'vem me pegar'.",
        "apelido": "Deinha",
        "tempo_relacionamento": "10 meses"
    },
    {
        "nome": "Tatiana Gomes",
        "idade": 30,
        "ultimo_encontro": "2025-05-16",
        "atração": "A pegada firme e o jeito selvagem.",
        "apelido": "Tati Selvagem",
        "tempo_relacionamento": "3 anos"
    },
    {
        "nome": "Michele Duarte",
        "idade": 26,
        "ultimo_encontro": "2025-05-20",
        "atração": "A risada safada e os beijos molhados.",
        "apelido": "Mi Amor",
        "tempo_relacionamento": "11 meses"
    },
    {
        "nome": "Natália Reis",
        "idade": 25,
        "ultimo_encontro": "2025-05-24",
        "atração": "Aquele olhar que me despiu antes da roupa cair.",
        "apelido": "Nati",
        "tempo_relacionamento": "1 mês e meio"
    },
    {
        "nome": "Daniela Pires",
        "idade": 29,
        "ultimo_encontro": "2025-05-29",
        "atração": "A forma como gruda no meu colo.",
        "apelido": "Dani",
        "tempo_relacionamento": "7 meses"
    },
    {
        "nome": "Raquel Nunes",
        "idade": 27,
        "ultimo_encontro": "2025-06-02",
        "atração": "Os gemidos que viram trilha sonora.",
        "apelido": "Kelzinha",
        "tempo_relacionamento": "2 anos"
    },
    {
        "nome": "Amanda Rocha",
        "idade": 23,
        "ultimo_encontro": "2025-05-21",
        "atração": "Aquela carinha de safada disfarçada de anjo.",
        "apelido": "Mandinha",
        "tempo_relacionamento": "6 semanas"
    },
    {
        "nome": "Sabrina Melo",
        "idade": 28,
        "ultimo_encontro": "2025-05-27",
        "atração": "O quadril que me hipnotiza só de andar.",
        "apelido": "Sá",
        "tempo_relacionamento": "5 anos"
    },
    {
        "nome": "Elaine Braga",
        "idade": 31,
        "ultimo_encontro": "2025-05-30",
        "atração": "A sensualidade que exala em cada toque.",
        "apelido": "Lainha",
        "tempo_relacionamento": "2 anos e meio"
    },
    {
        "nome": "Luana Teixeira",
        "idade": 24,
        "ultimo_encontro": "2025-05-13",
        "atração": "Os beijos que me deixam sem ar.",
        "apelido": "Lulu",
        "tempo_relacionamento": "1 ano e 3 meses"
    },
    {
        "nome": "Cláudia Ribeiro",
        "idade": 30,
        "ultimo_encontro": "2025-05-17",
        "atração": "A inteligência que me excita junto com o decote.",
        "apelido": "Clau Sensual",
        "tempo_relacionamento": "8 meses"
    },
    {
        "nome": "Marina Brito",
        "idade": 22,
        "ultimo_encontro": "2025-05-26",
        "atração": "A forma como me olha como se já estivesse nua.",
        "apelido": "Mari Perigosa",
        "tempo_relacionamento": "3 meses"
    },
]


# def listar():
    
#     print("---------- LISTA DE CONTATOS ---------- \n")
#     for bitch in bitches:
#         print(bitch['nome'])
#         print("___",bitch["apelido"])
#         print("___",bitch["ultimo_encontro"], "\n \n")

# def criar():
#        bitches.append({
#         "nome": "DOCINHA",
#         "idade": 20,
#         "ultimo_encontro": "Hoje de manhã",
#         "atração": "Tudo de bom, o amor da minha vida.",
#         "apelido": "My baby",
#         "tempo_relacionamento": "5 meses" })
       
#        listar()

# def atualizar():
#     print("atualizado")
#     listar()

# def apagar():
#     print("apagado")
#     listar()
     
# def pesquisar(nome):
#     for item in bitches:
#         if(nome == item["nome"]):
#            return item

# def menuInicial():

#     listar()
#     print("\n \n \n")
#     print("1--🔍  Peneirar \n")
#     print("2--♻️   Atualizar \n")
#     print("3--❌  Apagar \n")
#     print("4--➕  Criar \n")
#     print("\n \n")

#     opcao = int(input("OPCAO NUMERO => "))

#     match opcao:
#         case 1:
#             pesquisar()
#         case 2:
#             atualizar()
#         case 3:
#             apagar()
#         case 4:
#             criar()
            
    
# menuInicial()


ARQUIVO = 'bitches.json'  # Nome do arquivo onde vamos guardar os dados

# Se o arquivo ainda não existe, cria ele com uma lista vazia dentro
if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, 'w') as f:
        json.dump( bitches, f)  # Escreve uma lista vazia no arquivo

# Função para ler os dados do JSON
def ler_dados():
    with open(ARQUIVO, 'r') as f:  # Abre o arquivo no modo leitura
        return json.load(f)  # Converte o conteúdo JSON em objeto Python (lista de dicionários)

# Função para salvar dados no JSON (sobrescreve tudo)
def salvar_dados(dados):
    with open(ARQUIVO, 'w') as f:  # Abre o arquivo no modo escrita
        json.dump(dados, f, indent=2)  # Escreve os dados com indentação bonitinha

# CREATE - Adiciona um novo item à lista
def adicionar_item(nome, preco):
    dados = ler_dados()  # Lê os dados atuais

    # Gera um novo ID (máximo ID atual + 1)
    novo_id = max([item['id'] for item in dados], default=0) + 1

    # Cria um novo item como dicionário
    novo_item = {"id": novo_id, "nome": nome, "preco": preco}

    dados.append(novo_item)  # Adiciona o novo item na lista
    salvar_dados(dados)  # Salva os dados atualizados no arquivo

    print(f"Item '{nome}' adicionado com sucesso!")  # Confirma no terminal

# READ - Lista todos os itens salvos no arquivo
def listar_itens():
    dados = ler_dados()  # Lê os dados

    if not dados:
        print("Nenhum item encontrado.")  # Se a lista estiver vazia
    for item in dados:
        # Mostra os dados de cada item
        print(f"ID: {item['id']} | Nome: {item['nome']} | Preço: R${item['preco']}")

# UPDATE - Atualiza um item com base no ID
def atualizar_item(id_item, novo_nome=None, novo_preco=None):
    dados = ler_dados()  # Lê os dados

    for item in dados:
        if item['id'] == id_item:  # Se o ID bater com algum item
            if novo_nome: item['nome'] = novo_nome  # Atualiza o nome se foi fornecido
            if novo_preco: item['preco'] = novo_preco  # Atualiza o preço se foi fornecido

            salvar_dados(dados)  # Salva as mudanças
            print(f"Item {id_item} atualizado com sucesso.")  # Confirma
            return  # Encerra a função

    print("Item não encontrado.")  # Se nenhum ID bater

# DELETE - Deleta um item pelo ID
def deletar_item(id_item):
    dados = ler_dados()  # Lê os dados

    # Cria nova lista sem o item que queremos deletar
    novos_dados = [item for item in dados if item['id'] != id_item]

    # Se o tamanho mudou, quer dizer que o item foi removido
    if len(novos_dados) != len(dados):
        salvar_dados(novos_dados)  # Salva a nova lista
        print(f"Item {id_item} deletado.")  # Confirma
    else:
        print("Item não encontrado.")  # Caso o ID não exista
