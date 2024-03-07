def invertir_palabra(texto):
    palabra_invertida = ""
    for cadena in texto:
        palabra_invertida = cadena + palabra_invertida
    return palabra_invertida


print(invertir_palabra("hola"))


def reconocer_palindromo(texto_01):
    inver_palabra = invertir_palabra(texto_01)
    if texto_01 == inver_palabra:
        return True
    else:
        return False


print(reconocer_palindromo("reconocer"))
