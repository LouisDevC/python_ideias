import pandas as pd

# Dados de treinamento de exemplo
dados = {
    "carta1": ["o envelope", "chicote", "A cegonha", "O buque", "A mulher", "O anel", "A cobra", "A casa", "O homem", "A chave", "O navio"],
    "carta2": ["O jardim", "Os lírios", "AS nuvens", "O urso", "A cruz", "A lua", "O cachorro", "O caixão", "O sol", "O trevo", "A foice"],
    "carta3": ["A ancôra", "Os peixes", "A torre", "O cavaleiro", "O livro", "Os ratos", "A raposa", "As estrelas", "A criança", "Os pássaros", "O coração"],
    "significado": [
        "Novo projeto com base sólida",
        "Conflitos seguidos de tranquilidade e abundância",
        "Mudança inesperada que traz isolamento",
        "Recebendo apoio e proteção na jornada",
        "Sofrimento associado ao conhecimento oculto",
        "Parceria ou contrato sob ameaça",
        "Amizade com intenções enganosas",
        "Fim de uma fase doméstica, novos sonhos",
        "Início positivo e inocente para um homem",
        "Solução rápida através de comunicação",
        "Viagem que termina em mudança emocional"
    ]
}

# Criar um DataFrame
df = pd.DataFrame(dados)

# Salvar em um arquivo CSV
df.to_csv('significados_cartas.csv', index=False)
print("Dados salvos em 'significados_cartas.csv'")
