from FUNCTIONS.buscar_excel_02 import leer_datos_desde_excel

# Ejemplo de uso de la función
archivo_excel = 'C:/Users/EVENTOS/Desktop/PYTHON/TEST_ARCH/Copia_de_2.1_IT_CORRESPONDENCIA_CONTRATO_RH.xlsx'
columnas_requeridas = ['EMBAJADOR', 'N° DOC', 'DIRECCION', 'DISTRITO', 'CIUDAD',
                       'CAMPAÑA', 'DURACIÓN', 'FECHA DE INICIO', 'FECHA DE FIN', 'REMUNERACIÓN']

datos = leer_datos_desde_excel(archivo_excel, columnas_requeridas)
print(datos)
