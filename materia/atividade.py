import pandas as pd

df = pd.read_csv("jogos.csv")

print("\nTipos de dados:")
print(df.dtypes)
print("\nPreço médio:", df["preco"].mean())
print("Nota média:", df["nota"].mean())
print("\nPrimeiros 3 jogos (nome e preço):")
print(df[["nome", "preco"]].head(3))
