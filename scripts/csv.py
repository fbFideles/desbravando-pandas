import pandas as pd

#|%%--%%| <Amt248WCte|dRNaG0jyc0>
r"""°°°
Importando dados de .csv
°°°"""
#|%%--%%| <dRNaG0jyc0|XSrveOIIrZ>

df = pd.read_csv("./data/pedido.csv")

#|%%--%%| <XSrveOIIrZ|FNxWVwUZDp>
r"""°°°
Dataframes são agregados de d
°°°"""
#|%%--%%| <FNxWVwUZDp|ArZbhZ7kDz>

df.columns

#|%%--%%| <ArZbhZ7kDz|POfgsYtZGr>

df.index

#|%%--%%| <POfgsYtZGr|U3IiUlBMhJ>

df.shape

#|%%--%%| <U3IiUlBMhJ|G3T8qtPEPr>

df.head()

#|%%--%%| <G3T8qtPEPr|2uoJv8ZgsO>

df.tail()

#|%%--%%| <2uoJv8ZgsO|n42zd64uTc>

df.sample(10)

#|%%--%%| <n42zd64uTc|knNn6Fz9hX>

df.info(memory_usage='deep')

#|%%--%%| <knNn6Fz9hX|tqw2OJ8FyN>

tipos_coluna = df.dtypes
tipos_coluna

#|%%--%%| <tqw2OJ8FyN|4NLWBDhR68>

df[['idPedido', 'dtPedido']]
#|%%--%%| <4NLWBDhR68|86cFiUWOOf>

sample_100 = df.sample(100)

#|%%--%%| <86cFiUWOOf|oSplZsgxZt>
## Posição no dataset
sample_100.iloc[0:4]
sample_100.iloc[0]

#|%%--%%| <oSplZsgxZt|PkY6MpQf7G>
## Posição no index do dataset
sample_100.loc[855]

