# hola_lenguaje.py

# Obtener el lenguaje favorito desde la variable de entorno
lenguaje_favorito = os.getenv('LANGUAGE')

# Definir mensajes personalizados para cada lenguaje
mensajes = {
    'Python': 'Hola amante de Python!',
    'JavaScript': '¡Hola fanático de JavaScript!',
    'Go': '¡Saludos al aficionado de Go!'
}

# Verificar si se proporcionó un lenguaje favorito válido
if lenguaje_favorito in mensajes:
    mensaje_personalizado = mensajes[lenguaje_favorito]
else:
    mensaje_personalizado = 'Hola, ¿cuál es tu lenguaje favorito?'

# Imprimir el mensaje personalizado
print(mensaje_personalizado)
