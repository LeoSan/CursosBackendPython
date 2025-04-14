import asyncio

async def process_data(data):
    print(f'Procesando {data}...')
    #Simular una operación
    await asyncio.sleep(10)
    print(f'{data} procesado.')
    return data * 2

async def main():
    print('Inicio de procesamiento')
    result = await process_data('archivo.txt')
    print(f'Resultado: {result}')

asyncio.run(main())