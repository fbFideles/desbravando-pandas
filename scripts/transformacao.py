import pandas as pd
import numpy as np
#|%%--%%| <8dWALEtvPy|3dtRun43EO>
df = pd.read_csv("./data/produto.csv")
df.info()
#|%%--%%| <3dtRun43EO|u6A377V4uO>
r"""°°°
Criação de colunas novas - Corrigindo preço pela inflação
°°°"""
df["vlPrecoAjustado"] = df["vlPreco"] * 1.09
df["vlPrecoAjustado"] = df["vlPrecoAjustado"].round(2)
df
#|%%--%%| <u6A377V4uO|jXAFVsHpZH>
r"""°°°
Criação de colunas novas - Simplificando arredondamento
°°°"""
df["vlPrecoAjustado"] = (df["vlPreco"] * 1.09).round(2)
df
r"""°°°
Criação de colunas novas - Operação entre colunas - Quanto aumentou
°°°"""
df["txAjuste(%)"] = (100 * ((df["vlPrecoAjustado"] / df["vlPreco"]) - 1)).round(2)
df
r"""°°°
Dropando colunas - Coluna de ajuste 
°°°"""
df = df.drop(columns=["txAjuste"])
df
r"""°°°
Dropando colunas - Coluna de ajuste com (del)
°°°"""
del df["txAjueste(%)"]
df
#|%%--%%| <jXAFVsHpZH|1eZAmi2Itc>
r"""°°°
Aplicando transformações complexas - com numpy
°°°"""
df["log(txAjuste(%))"] = np.log(df["txAjuste(%)"])
df["exp(txAjuste)"] = np.exp(df["txAjuste(%)"])
df

#|%%--%%| <1eZAmi2Itc|dqfFkXKlIK>
r"""°°°
Aplicando transformações complexas - funções personalizadas
Fatorial da parte inteira
°°°"""
def fact(n):
    total = 1
    for i in range(2, int(n)+1):
        total *= i
    return total

df["fact(vlPrecoAjustado)"] = df["vlPrecoAjustado"].apply(fact)
df

#|%%--%%| <dqfFkXKlIK|lnrkfyABBI>
r"""°°°
Sidenote recursão da erro no metodo apply
°°°"""
def fact_tail(n, acc=1):
    if n == 0:
        return acc
    return fact_tail(n - 1, acc * n)

df["fact_rec(vlPrecoAjustado)"] = df["vlPrecoAjustado"].apply(fact_tail)
df.to_csv("./data/produto_transform.csv")

