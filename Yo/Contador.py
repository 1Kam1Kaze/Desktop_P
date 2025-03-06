import os

# Función para leer el valor del contador desde un archivo
def leer_contador():
    if os.path.exists("contador.txt"):
        with open("contador.txt", "r") as archivo:
            return int(archivo.read().strip())
    else:
        return 0

# Función para guardar el valor del contador en un archivo
def guardar_contador(valor):
    with open("contador.txt", "w") as archivo:
        archivo.write(str(valor))

# Función principal del programa
def main():
    # Leer el valor actual del contador
    contador = leer_contador()

    while True:
        print(f"Valor actual del contador: {contador}")
        # Solicitar al usuario cuánto desea incrementar o salir
        opcion = input("¿Cuánto deseas incrementar? (1 o 5) o escribe 'exit' para salir: ")

        if opcion == "exit":
            print("Saliendo del programa...")
            break  # Termina el bucle y el programa

        try:
            incremento = int(opcion)
            if incremento in [1, 5]:
                contador += incremento
                print(f"Nuevo valor del contador: {contador}")
                guardar_contador(contador)
            else:
                print("Solo puedes incrementar de 1 o 5.")
        except ValueError:
            print("Entrada no válida. Debes escribir un número (1 o 5) o 'exit' para salir.")

if __name__ == "__main__":
    main()

