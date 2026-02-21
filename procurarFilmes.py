line = "="
titulo = "SAMUELFLIX"

print(titulo.center(67, "="))
print(line * 25, "PROCURAR FILMES", line * 25)

filmes = ["O Poderoso Chefão", "Titanic", "Vingadores: Ultimato", "Interestelar", "O Senhor dos Anéis: A Sociedade do Anel", "Matrix", "Gladiador", "Clube da Luta", "Forrest Gump", "A Origem", "Jurassic Park", "Homem-Aranha: Sem Volta Para Casa", "Coringa", "Avatar", "Pantera Negra", "Harry Potter e a Pedra Filosofal", "Star Wars: Uma Nova Esperança", "O Rei Leão", "De Volta para o Futuro", "Os Vingadores"]

while True:
    procurarFilmes= input("Digite o filme que você procura(ou 'Sair' para encerrar): \n")
    if procurarFilmes.lower() == "sair":
        print("Processo Encerrado")
        break
    filmeEncontrado = [filme for filme in filmes if procurarFilmes.lower() in filme.lower()]
    if filmeEncontrado:
        print(f"Filmes(s) encontrado(s): ")
        print("\n".join(sorted(filmeEncontrado)))
    else:
        print(line * 67)
        print("Filme não encontrado")
        print(line * 67)

