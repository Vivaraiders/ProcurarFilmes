import GerenciarFilmes



while True:
    print(GerenciarFilmes.line * 40, GerenciarFilmes.titulo.upper(), GerenciarFilmes.line * 40)
    status = int(input("Você deseja: 1 - listar os filmes / 2 - Adicionar filme / 3 - Excluir Filme / 4 - Para sair: \n"))
    if status == 1:
        GerenciarFilmes.MostrarFilmes()
    elif status == 2:
        GerenciarFilmes.AdicionarFilmes()
    elif status == 3:
        GerenciarFilmes.DeletarFilme()
    elif status == 4:
        (print("Processo Encerrado"))
        break
    else:
        print("Caractere invalido")
