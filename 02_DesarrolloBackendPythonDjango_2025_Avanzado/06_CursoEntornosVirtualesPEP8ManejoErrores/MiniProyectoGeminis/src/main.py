from gemini_client import configure_gemini

def main():
    try:
        model = configure_gemini()
        print(f"--- Conexión Configurada ---")
        print("Escribe 'salir' para terminar el programa.\n")
    except Exception as e:
        print(e)
        return

    # 3. Bucle de interacción
    while True:
        try:
            user_input = input("Tú: ")
            if user_input.lower() in ['salir', 'exit', 'quit']:
                print("¡Hasta luego!")
                break
            
            if not user_input.strip():
                continue

            # 4. Enviar solicitud al modelo
            response = model.generate_content(user_input)
            
            # 5. Mostrar respuesta
            print(f"Gemini: {response.text}\n")

        except Exception as e:
            print(f"\nOcurrió un error: {e}\n")

if __name__ == "__main__":
    main()
