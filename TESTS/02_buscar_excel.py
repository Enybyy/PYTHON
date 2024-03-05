import pandas as pd

df = pd.read_excel(
    "C:/Users/EVENTOS/Downloads/Trabajo_Abby/ANEXO_1_ADICIONAL.xlsx", index_col="N°", header=6)

df["NUMERO"].fillna(0, inplace=True)
df["NUMERO"] = df["NUMERO"].astype(int)
# # CONTAR CUANTAS CASILLAS "NA" HAY
# # df["NUMERO"].fillna(0, inplace=True)
# # CONTAR CUANTOS CASILLAS "INFINITO" HAY
# # print(df["NUMERO"].isin([np.inf, -np.inf]).sum())
print(df.query("TIPO == 'DNI'")[["TIPO", "NUMERO"]])

lista_DNI = df.query("TIPO == 'DNI'")["NUMERO"].tolist()
print(lista_DNI)
