import pprint

line = "="
titulo = "samuelflix"
pp = pprint.PrettyPrinter(depth = 4)
listaFilmes = {                              
    "Batman": {
        "Ano de Lançamento": 2020,
        "Nota do Filme": 7.8,
        "Valor do Filme": 30.00
    },
    "deadpoll": {
        "Ano de Lançamento": 2022,
        "Nota do Filme": 8.3,
        "Valor do Filme": 20.00
    },
    "homem aranha": {
        "Ano de Lançamento": 2024,
        "Nota do Filme": 9.2,
        "Valor do Filme": 45.00
    }
}

def AdicionarFilmes():
    QuantidadeFilme = int(input("Quantos Filmes Quer Adicionar: \n"))       

    for i in range(QuantidadeFilme):            #Loop na quantidade de vezes que o usuário escolheu
        Filme = input("Digite o Nome do Filme: \n")

        AnoLancamento = int(input("Digite Ano Em Que o Filme Foi Lançado: \n"))
        while AnoLancamento > 2026 or AnoLancamento < 1900:     #Escolher o ano de 1900 pra cá
            print("Ano Invalido, Digite o Ano Denovo: ")
            AnoLancamento = int(input())

        ValorFilme = float(input("Valor Do Filme: \nR$ "))

        NotaFilme = float(input("Digite a Nota Do Filme: \n"))
        while NotaFilme > 10 or NotaFilme < 0:          #Não escolher uma nota maior ou menor que 10
                print("A Nota Não Pode Ser Maior Do que 10, Tente Novamente: ")
                NotaFilme = float(input())

        listaFilmes[Filme.title()] = {          #Acrescenta tudo na Lista
            "Ano de Lançamento": AnoLancamento,
            "Valor do Filme": ValorFilme,
            "Nota do Filme": NotaFilme
        }

        print(f"{Filme.title()} ({AnoLancamento}) - R$ {ValorFilme:.2f} - Nota: {NotaFilme}")

#########################################################################################

def DeletarFilme():
    DesejaDeletar = input("Deseja Deletar algum Filme? (Sim ou Não)\n")
    FilmeOrdenados = []
    
    while DesejaDeletar.lower() != "sim" and DesejaDeletar.lower() != "não":
        print("Não Entendi, tente Novamente")
        DesejaDeletar = input()

    if DesejaDeletar == "sim":
        FilmeParaDeletar = input("Digite o Filme Que Deseja Deletar: \n")
        for i in listaFilmes:                              #A variável i vai receber os filmes que estão da Lista
            if FilmeParaDeletar.lower() in i.lower():       #Se existir as palavras que o usuário digitou na Lista de filmes(VARIÁVEL I)
                FilmeOrdenados.append(i)                #Encrementa o FILME(Não só os caracteres)

        FilmeOrdenados.sort()                          #Para ordernar em ordem alfabética e melhor visualização
        print(f"O(s) Filme(s) Achado(s) Foi:")
        for f in FilmeOrdenados:                        #fiz um laço para que os filmes não sejam mostrados em formato de lista
            print(f)
        
        ConfirmaDeletar = input("Escreva EXATAMENTE o Filme Que Você Deseja Deletar: \n")
        filme_para_deletar = None


        for filme in FilmeOrdenados:                    #Filme vai receber os Filmes para que eu compare na base de dados e se existir, irá excluir(Tem que estar escrito estritamente igual para que não apague dados errados)
            if ConfirmaDeletar == filme:
                filme_para_deletar = filme
                break                                   #O break é pra quando achar o filme, parar o laço e não procurar mais
        
        if filme_para_deletar:                          #Se tiver achado um filme(True) irá deletar
            del listaFilmes[filme_para_deletar]
            print(f"{filme_para_deletar} Foi Deletado")

        else:
            print("Filme Não Encontrado")
            
        
    else:
        print("Processo Encerrado")
        exit()
         
#########################################################################################
def MostrarFilmes():
    cor_vermelha = "\033[31m"
    reset = "\033[0m"
    for nome, info in listaFilmes.items():
        print(line * 92,f"\nNome do Filme: {cor_vermelha}{nome}{reset}, Ano de Publicação: {info['Ano de Lançamento']}, Valor do Filme: {info['Valor do Filme']}, Nota do filme: {info['Nota do Filme']}\n")

#########################################################################################

while True:
    print(line * 40, titulo.upper(), line * 40)
    status = int(input("Você deseja: 1 - listar os filmes / 2 - Adicionar filme / 3 - Excluir Filme / 4 - Para sair: \n"))
    if status == 1:
        MostrarFilmes()
    elif status == 2:
        AdicionarFilmes()
    elif status == 3:
        DeletarFilme()
    elif status == 4:
        (print("Processo Encerrado"))
        break
    else:
        print("Caractere invalido")
