import pandas as pd

#|%%--%%| <FYZtDpms1a|LFTqxG4y0G>

## Declarando pd.Series a partir de listas do python
idade = [31, 33, 2, 29, 60, 58, 31, 45, 24]
s_idade = pd.Series(idade)
#|%%--%%| <LFTqxG4y0G|3JknBNh4nk>

## Metodos das pd.Series
mean = s_idade.mean()
variancia = s_idade.var()
desv = s_idade.std()

## Metodo descritivo das pd.Series
s_idade.describe()

#|%%--%%| <3JknBNh4nk|z1Ja0y4ZFZ>
r"""°°°
<h3>Listas possuem operadores escalares para comparação logica</h3>
°°°"""
#|%%--%%| <z1Ja0y4ZFZ|KqL9DSODAd>

filtro = s_idade >= 30
filtro

#|%%--%%| <KqL9DSODAd|Vf3Mh2tDSi>
r"""°°°
<h3>Essas operações escalares retornam pd.Series comparadas em cada termo</h3>
°°°"""

#|%%--%%| <Vf3Mh2tDSi|SQ1RiYURk6>
s_idade[filtro]

#|%%--%%| <SQ1RiYURk6|HltD1mKxzS>
r"""°°°
<h3>Que por sua vez podem ser utilizados em sua coleção como indice para a propria pd.Series</h3>
°°°"""
