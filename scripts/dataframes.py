import pandas as pd
#|%%--%%| <wBi2XCqeLv|yIhA7KmzXT>
r"""°°°
Na linguagem python a estrutura dicionario permite aplicar indeces
a n tipos de dados diferentes ex.: string: list[]
°°°"""
#|%%--%%| <yIhA7KmzXT|jc9DFP6uSV>
data = {
    "nome":["Téo", "Nah", "Maria", "José", "Marina", "Jessica", "InfoSlack"],
    "idade":[30, 33, 2, 45, 65, 43, 40],
    "cor": ["Preto", "Verde", "Azul", "Vermelho", "Amarelo", "Verde", "Azul"],
    "renda": [3566, 1345, 0, 6576, 4325, 5326, 10244]
}
data["idade"]
#|%%--%%| <jc9DFP6uSV|S8V9XvP1OQ>
r"""°°°
No Pandas temos os pd.DataFrames que agregam pd.Series de forma analoga
(mas não equivalente) essas series que posteriormente podem ser acessadas
de diversas formas vide exemplo ex.: coluna idade
°°°"""
#|%%--%%| <S8V9XvP1OQ|Sie7qSURCf>
df = pd.DataFrame(data)
df.idade
#|%%--%%| <Sie7qSURCf|A3QvvsiJGF>
## melhor pois podemos acessar de forma programatica por exemplo ex.: col = "idade"; df[col]
df = pd.DataFrame(data)
df["idade"]
#|%%--%%| <A3QvvsiJGF|kQBKTs6XwK>
df.mean(numeric_only=True)
