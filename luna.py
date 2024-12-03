import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer

# Carregar os dados
data = pd.read_csv('significados_cartas.csv')

# Preparar os dados
X = data[['carta1', 'carta2', 'carta3']].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
y = data['significado']

# Converter texto para vetores de contagem
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Treinar o modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Avaliar o modelo
accuracy = model.score(X_test, y_test)
print(f"Acurácia do modelo: {accuracy * 100:.2f}%")

# Função para prever o significado
def prever_significado(carta1, carta2, carta3):
    input_data = vectorizer.transform([f"{carta1} {carta2} {carta3}"])
    return model.predict(input_data)[0]

# Exemplo de uso
significado = prever_significado("o envelope", "O jardim", "A ancôra")
print(f"Significado: {significado}")
