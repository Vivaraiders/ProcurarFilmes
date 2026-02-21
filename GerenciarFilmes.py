import pprint

pp = pprint.PrettyPrinter(depth = 4)
listaFilmes = {}
'''listaFilmes = {                               //Para teste e não ter que ficar criando os filmes toda hora
    "Batman": {
        "Ano de Lançamento": 2020,
        "Nota do Filme": 9.0,
        "Valor do Filme": 30.00
    },
    "deadpoll": {
        "Ano de Lançamento": 2022,
        "Nota do Filme": 8.0,
        "Valor do Filme": 20.00
    },
    "homem aranha": {
        "Ano de Lançamento": 2024,
        "Nota do Filme": 9.2,
        "Valor do Filme": 45.00
    }
}'''

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
            "Ano de Laçamento": AnoLancamento,
            "Valor do Filme": ValorFilme,
            "Nota do Filme": NotaFilme
        }

        print(f"{Filme.title()} ({AnoLancamento}) - R$ {ValorFilme:.2f} - Nota: {NotaFilme}")
AdicionarFilmes()


pp.pprint(listaFilmes)  # Mostra o Dicionario formatado para melhor visialização

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
    
DeletarFilme()

pp.pprint(listaFilmes)
         
        
