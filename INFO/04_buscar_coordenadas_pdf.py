# Importar PDFMiner
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

# Abrir el archivo PDF
pdf_file = open(
    "C:/Users/EVENTOS/Desktop/PYTHON/ARCHIVOS_TESTS/HOLA_MUNDO.pdf", "rb")

# Crear una lista vacía para guardar las palabras y sus coordenadas
words = []

# Recorrer cada página del PDF
for page_layout in extract_pages(pdf_file):

    # Recorrer cada elemento de texto de la página
    for element in page_layout:

        # Si el elemento es un contenedor de texto
        if isinstance(element, LTTextContainer):

            # Recorrer cada carácter del texto
            for text_line in element:

                for character in text_line:

                    # Si el carácter es una letra
                    if isinstance(character, LTChar):

                        # Obtener el texto y las coordenadas del carácter
                        text = character.get_text()
                        x0 = character.bbox[0]
                        y0 = character.bbox[1]
                        x1 = character.bbox[2]
                        y1 = character.bbox[3]

                        # Añadir el carácter y sus coordenadas a la lista de palabras
                        words.append([text, x0, y0, x1, y1])

# Crear una variable para guardar la palabra a buscar
word_to_find = "DNI"

# Crear una variable para guardar la longitud de la palabra a buscar
word_length = len(word_to_find)

# Recorrer la lista de palabras
for i in range(len(words)):

    # Obtener el texto y las coordenadas de la palabra actual
    word = words[i][0]
    x0 = words[i][1]
    y0 = words[i][2]
    x1 = words[i][3]
    y1 = words[i][4]

    # Si el texto es igual a la primera letra de la palabra a buscar
    if word == word_to_find[0]:

        # Crear una variable para guardar la palabra encontrada
        word_found = word

        # Crear una variable para guardar el índice de la palabra a buscar
        index = 1

        # Crear una variable para guardar la coordenada x final de la palabra encontrada
        x_end = x1

        # Recorrer los siguientes caracteres de la lista de palabras
        for j in range(i + 1, i + word_length):

            # Obtener el texto y las coordenadas del carácter actual
            char = words[j][0]
            x0_char = words[j][1]
            y0_char = words[j][2]
            x1_char = words[j][3]
            y1_char = words[j][4]

            # Si el texto es igual a la letra correspondiente de la palabra a buscar
            # y las coordenadas y son iguales o similares
            if char == word_to_find[index] and abs(y0 - y0_char) < 1:

                # Añadir el texto a la palabra encontrada
                word_found += char

                # Incrementar el índice de la palabra a buscar
                index += 1

                # Actualizar la coordenada x final de la palabra encontrada
                x_end = x1_char

            # Si no, salir del bucle
            else:
                break

        # Si la palabra encontrada es igual a la palabra a buscar
        if word_found == word_to_find:

            # Imprimir la palabra encontrada y sus coordenadas
            print(f"La palabra '{word_found}' se encuentra en las coordenadas ({
                  x0}, {y0}) - ({x_end}, {y1})")
