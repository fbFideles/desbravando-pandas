import pandas as pd
#|%%--%%| <dp4D8qkeCJ|gDePxkng7c>
df = pd.read_csv("./data/pedido.csv")
#|%%--%%| <gDePxkng7c|ahvNYqZneC>
r"""°°°
Filtrando apenas pelos pedidos feitos em sao paulo
°°°"""
filtro_uf = df["descUF"] == "São Paulo" 
df[filtro_uf]
#|%%--%%| <ahvNYqZneC|jMGt3Hll9C>
r"""°°°
Filtrando pelos pedidos de são paulo que pediram ketchup
°°°"""
filtro_uf = df["descUF"] == "São Paulo" 
filtro_ketchup = df["flKetchup"] == True
df[filtro_uf][filtro_ketchup]
#|%%--%%| <jMGt3Hll9C|LVju4RLNea>
r"""°°°
Filtrando pelos pedidos de são paulo que pediram ketchup - Notação &
°°°"""
#|%%--%%| <LVju4RLNea|cXl7Qw8dwo>
filtro = (df["descUF"] == "São Paulo")&(df["flKetchup"])
df[filtro]
#|%%--%%| <cXl7Qw8dwo|d9Pnul9eyL>
r"""°°°
Filtrando de forma composta Parana, São Paulo, Rio de Janeiro e Ketchup
°°°"""
#|%%--%%| <d9Pnul9eyL|pZGxZmavcn>
filtro = ((df["descUF"] == "São Paulo") | (df["descUF"] == "Paraná") | (df["descUF"] == "Rio de Janeiro")) & (df["flKetchup"])
df[filtro]["descUF"]
#|%%--%%| <pZGxZmavcn|40iy6gG7QY>
r"""°°°
Testando unicidade do filtro de UF e de Ketchup
°°°"""
#|%%--%%| <40iy6gG7QY|VL4zD2NG7j>
pd.Series(df[filtro]["descUF"]).unique()
#|%%--%%| <VL4zD2NG7j|lmvLHVINs0>
pd.Series(df[filtro]["flKetchup"]).unique()
#|%%--%%| <lmvLHVINs0|aEQFbsTmU5>
r"""°°°
Filtrando de forma composta (Parana, São Paulo, Rio de Janeiro) e Ketchup - metodo pd.Series.isin
°°°"""
#|%%--%%| <aEQFbsTmU5|P6Xhy9hp0i>
filtro = df["descUF"].isin(["São Paulo", "Paraná", "Rio de Janeiro"]) & (df["flKetchup"])
df[filtro]
#|%%--%%| <P6Xhy9hp0i|nZsYCLsUio>
r"""°°°
Filtrando pelos pedidos que não deixaram recado usando pd.Series.isna
°°°"""
df[df["txtRecado"].isna()]
# alias pd.Series.isnull
