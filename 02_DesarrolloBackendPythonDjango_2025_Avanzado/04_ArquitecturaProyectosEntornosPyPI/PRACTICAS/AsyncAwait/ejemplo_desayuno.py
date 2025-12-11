import asyncio
import time

# 1. Definimos una corrutina con 'async def'
# Esta funcion simula una tarea que tarda tiempo (IO-bound), como tostar pan.
async def tostar_pan():
    print("[1] Poniendo el pan en la tostadora...")
    
    # 2. Usamos 'await' para pausar esta funcion sin bloquear todo el programa.
    # asyncio.sleep(2) simula que esperamos 2 segundos.
    await asyncio.sleep(2)
    
    print("[2] Pan tostado listo!")
    return "Tostada"

async def freir_huevos():
    print("[1] Rompiendo huevos en la sarten...")
    await asyncio.sleep(3) # Esta tarea tarda 3 segundos
    print("[2] Huevos fritos listos!")
    return "Huevos"

async def preparar_cafe():
    print("[1] Encendiendo cafetera...")
    await asyncio.sleep(1) # Esta es la mas rapida
    print("[2] Cafe listo!")
    return "Cafe"

# Funcion principal (tambien es asincrona) coordinando todo
async def main():
    inicio = time.time()
    print("--- Comienza el desayuno ASINCRONO ---")

    # 3. asyncio.gather ejecuta las corrutinas concurrentemente (al "mismo tiempo").
    # Si fuera sincrono, tardaria 2 + 3 + 1 = 6 segundos.
    # Como es asincrono, tardara lo que tarde la mas larga (aprox 3 segundos).
    print("Lanzando tareas...")
    resultado = await asyncio.gather(tostar_pan(), freir_huevos(), preparar_cafe())

    fin = time.time()
    
    print("\nServimos:", resultado)
    print(f"Tiempo total: {fin - inicio:.2f} segundos")
    print("   (Nota: Si fuera sincrono, habria tardado ~6 segundos)")

# 4. Punto de entrada para ejecutar el event loop
if __name__ == "__main__":
    """
    Es el puente obligatorio entre tu código normal y el código async. Sin él, si llamaras solo a 
    main() , Python te devolvería una corrutina en pausa y no pasaría nada
    """
    # asyncio.run(main()) #event loop es el director de orquesta que coordina todas las corrutinas

    """
    Tambien podemos generar nuestro propio event loop 
    """
    my_loop = asyncio.new_event_loop() # Creo 
    asyncio.set_debug(True)            # Solo en DEV es para debugear 
    asyncio.set_event_loop(my_loop)    # Asigno 
    
    try:
        my_loop.run_until_complete(main()) # Ejecuto  
    finally:
        my_loop.close() # Siempre cerramos el loop al final
