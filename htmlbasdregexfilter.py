import re

# Función que intenta filtrar HTML usando una expresión regular
def filtrar_html(texto):
    # Expresión regular insegura para filtrar HTML
    regex = re.compile(r'<.*?>')
    texto_filtrado = re.sub(regex, '', texto)
    return texto_filtrado

# Función principal para probar la vulnerabilidad
def main():
    entrada_usuario = input("Introduce un texto con HTML: ")
    print("Texto original:")
    print(entrada_usuario)
    
    texto_filtrado = filtrar_html(entrada_usuario)
    print("Texto después del filtrado:")
    print(texto_filtrado)

if __name__ == "__main__":
    main()
