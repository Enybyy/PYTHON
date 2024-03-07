# IMPORTAR LIBRERÍAS
import pandas as pd
import time


def read_excel_data(ruta_archivo_excel, columnas_requeridas):
    # Guardar el tiempo de inicio
    start_time = time.time()

    # READ EXCEL
    df = pd.read_excel(ruta_archivo_excel, header=0)

    # MOSTRAR COLUMNAS A LA IZQ
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', None)

    # SELECCIONAR COLUMNAS REQUQERIDAS
    datos_seleccionados = df[columnas_requeridas]

    # RELLENAR CELDAS EN VACÍAS
    valor_a_llenar = 'NaN'
    datos_seleccionados.fillna(valor_a_llenar, inplace=True)

    # CONVERTIR LOS DATOS SELECCIONADOS EN UNA LISTA DE L (sin encabezados)
    data_list = datos_seleccionados.values.tolist()

    # SAVE TIME
    end_time = time.time()

    # CALCULAR TIME
    elapsed_time = end_time - start_time
    time_01 = elapsed_time + 1

    # RETORNAR DATOS
    return data_list, time_01


# RUTA Y CULUMNAS REQUERIDAS
archivo_excel = 'C:/Users/EVENTOS/Desktop/PYTHON/TEST_ARCH/Copia_de_2.1_IT_CORRESPONDENCIA_CONTRATO_RH.xlsx'
columnas_requeridas = ['EMBAJADOR', 'N° DOC', 'DIRECCION', 'DISTRITO', 'CIUDAD',
                       'CAMPAÑA', 'DURACIÓN', 'FECHA DE INICIO', 'FECHA DE FIN', 'REMUNERACIÓN']

lista = read_excel_data(archivo_excel, columnas_requeridas)
# print(lista)
# print(lista[0][0])
