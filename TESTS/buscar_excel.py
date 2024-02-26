import pandas as pd

df = pd.read_excel(
    "C:/Users/EVENTOS/Downloads/Trabajo_Abby/ANEXO_1_ADICIONAL.xlsx", index_col="N°", header=6)

df_filtro_numero = df.fillna({"NUMERO": 0})
df_filtro_numero["NUMERO"] = df_filtro_numero["NUMERO"].astype(int)
# CONTAR CUANTAS CASILLAS "NA" HAY
# df["NUMERO"].fillna(0, inplace=True)
# CONTAR CUANTOS CASILLAS "INFINITO" HAY
# print(df["NUMERO"].isin([np.inf, -np.inf]).sum())
print(df_filtro_numero.query("TIPO == 'DNI'")[["TIPO", "NUMERO"]])

lista_DNI = df_filtro_numero.query("TIPO == 'DNI'")["NUMERO"].tolist()
print(lista_DNI)
