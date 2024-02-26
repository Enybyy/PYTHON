import pandas as pd
# import xlrd
# import numpy as np

df = pd.read_excel(
    "C:/Users/EVENTOS/Downloads/Trabajo_Abby/ANEXO_1_ADICIONAL.xlsx", index_col="N°", header=6)

df_fil_Numero = df.fillna({"NUMERO": 0})
df_fil_Numero["NUMERO"] = df_fil_Numero["NUMERO"].astype(int)
# CONTAR CUANTAS CASILLAS "NA" HAY
# df["NUMERO"].fillna(0, inplace=True)
# CONTAR CUANTOS CASILLAS "INFINITO" HAY
# print(df["NUMERO"].isin([np.inf, -np.inf]).sum())
print(df_fil_Numero.query("TIPO == 'DNI'")[["TIPO", "NUMERO"]])

lista_DNI = df_fil_Numero.query("TIPO == 'DNI'")["NUMERO"].tolist()
print(lista_DNI)
