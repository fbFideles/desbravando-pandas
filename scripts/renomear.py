import pandas as pd
#|%%--%%| <q85IEfILwl|TbZ4zX5pjm>
df = pd.read_csv("./data/pedido.csv")
df
#|%%--%%| <TbZ4zX5pjm|Htv9hjUKdA>
df["descUF"].head()
#|%%--%%| <Htv9hjUKdA|8Gq4kughBF>
de_para_dict = {"descUF": "descEstado"}
df.rename(columns=de_para_dict, inplace=True)
#|%%--%%| <8Gq4kughBF|kDkNHb0BSG>
de_para_dict = {"descUF": "descEstado"}
df = df.rename(columns=de_para_dict)
#|%%--%%| <kDkNHb0BSG|W0l9N9IHsr>
df

