def message_creator(text):
   # Escribe tu solución 👇
    mensaje = ''
    match text:
        case "computadora":
            mensaje = "Con mi computadora puedo programar usando Python"
        case "celular":
            mensaje = "En mi celular puedo aprender usando la app de Platzi"
        case "cable":
            mensaje = "¡Hay un cable en mi bota!"
        case _:  # El equivalente a 'default'
            mensaje = "Artículo no encontrado"
    return mensaje

list_op = ("computadora", "celular", "cable")
op = str(input(f'Escoge tu herramienta por favor: {list_op}: '))
response = message_creator(op)
print(response)