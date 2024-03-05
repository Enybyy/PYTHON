import fitz  # IMPORTAR LIBRERIA "PyMuPDF"

# INGRESAR RUTA  Y ABRIR EL ARCHIVO PDF
pdf_file_path = "C:/Users/EVENTOS/Desktop/PYTHON/TEST_ARCH/HOLA_MUNDO.pdf"
pdf_document = fitz.open(pdf_file_path)

# TEXTO A BUSCAR Y REMPLAZAR
find = input("Ingresa una opcion: ")
replace_text = "HELLO"

# RECORRER CADA PAGINA DEL PDF
for page_number in range(len(pdf_document)):
    page = pdf_document.load_page(page_number)
    text_instances = page.search_for(find)

    for inst in text_instances:
        # Obtenemos el tamaño de la fuente del texto original
        font_size = inst[3] - inst[1]
        # Agregamos la anotación de redacción
        page.add_redact_annot(inst)
        # Aplicamos las redacciones
        page.apply_redactions()
        # Insertamos el texto reemplazado con el formato deseado
        page.insert_text((inst[0], inst[1] + 12), replace_text,
                         fontsize=font_size, fontname="Times-Roman")

# Guardamos el PDF modificado
output_pdf_path = "C:/Users/EVENTOS/Desktop/PYTHON/TEST_ARCH/NuevoPdf.pdf"
pdf_document.save(output_pdf_path)
pdf_document.close()

print("Palabra reemplazada en todas las páginas del PDF conservando el formato original del texto.")
