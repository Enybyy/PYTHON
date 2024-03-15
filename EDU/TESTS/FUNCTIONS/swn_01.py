from docx import Document


def save_words_n(documento):
    """
    Esta función toma un documento de Word como entrada y devuelve una lista de palabras en negrita.
    """
    # Lista para almacenar palabras en negrita
    bold_words = []

    # Recorrer todos los párrafos del documento
    for para in documento.paragraphs:
        # Recorrer cada run en el párrafo
        for run in para.runs:
            # Verificar si el run está en negrita
            if run.bold:
                # Dividir el texto del run en palabras
                words = run.text.split()
                # Agregar palabras en negrita a la lista
                bold_words.extend(words)

    # Eliminar palabras duplicadas y ordenar alfabéticamente
    bold_words = sorted(set(bold_words))

    return bold_words


# Ejemplo de uso
if __name__ == "__main__":
    # Abrir el documento de Word
    doc = Document(
        'C:/Users/EVENTOS/Desktop/PROJECT_PYTHON/ARCHIVOS_LOCALES/Format_contrato.docx')

    # Obtener palabras en negrita del documento
    palabras_en_negrita = save_words_n(doc)

    # Imprimir la lista de palabras en negrita
    print("Palabras en negrita:", palabras_en_negrita)
