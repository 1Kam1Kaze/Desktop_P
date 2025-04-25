import datetime
import csv
import os
from collections import Counter

BASE_DIR = "finanzas"
DEBITO_DIR = os.path.join(BASE_DIR, "debito")
CREDITO_DIR = os.path.join(BASE_DIR, "credito")
AHORRO_DIR = os.path.join(BASE_DIR, "ahorro")

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def registrar_transaccion(tipo, monto):
    """Registra una transacción con la fecha actual."""
    fecha_actual = datetime.date.today()
    dia = fecha_actual.day
    mes = fecha_actual.month
    anio = fecha_actual.year
    return [tipo, dia, mes, anio, monto]

def guardar_transaccion(transaccion, nombre_archivo):
    """Guarda una transacción en un archivo CSV."""
    os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)
    with open(nombre_archivo, 'a', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(transaccion)

def leer_transacciones(nombre_archivo):
    """Lee todas las transacciones desde un archivo CSV."""
    transacciones = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', newline='') as archivo_csv:
            lector = csv.reader(archivo_csv)
            for fila in lector:
                transacciones.append(fila)
    return transacciones

def mostrar_tabla(transacciones):
    """Muestra las transacciones en una tabla."""
    if not transacciones:
        print("No hay transacciones registradas.")
        return

    print("-" * 40)
    print(f"{'Tipo':<10} | {'Día':<4} | {'Mes':<4} | {'Año':<6} | {'Monto':<10}")
    print("-" * 40)
    for transaccion in transacciones:
        tipo, dia, mes, anio, monto = transaccion
        print(f"{tipo:<10} | {dia:<4} | {mes:<4} | {anio:<6} | {monto:<10}")
    print("-" * 40)

def obtener_nombre_archivo(tipo_cuenta):
    """Genera la ruta completa del archivo basada en el tipo de cuenta, año y mes."""
    fecha_actual = datetime.date.today()
    mes_actual = fecha_actual.month
    anio_actual = fecha_actual.year
    nombre_archivo = f"registro_{tipo_cuenta}_{anio_actual}_{mes_actual:02d}.csv"
    if tipo_cuenta == "debito":
        ruta_archivo = os.path.join(DEBITO_DIR, str(anio_actual), nombre_archivo)
    elif tipo_cuenta == "credito":
        ruta_archivo = os.path.join(CREDITO_DIR, str(anio_actual), nombre_archivo)
    elif tipo_cuenta == "ahorro":
        ruta_archivo = os.path.join(AHORRO_DIR, str(anio_actual), nombre_archivo)
    else:
        ruta_archivo = os.path.join(BASE_DIR, nombre_archivo)
    return ruta_archivo

def mostrar_recuento_transacciones(transacciones):
    """Muestra el recuento de cada tipo de transacción."""
    if not transacciones:
        return

    tipos_transaccion = [transaccion[0] for transaccion in transacciones]
    recuento = Counter(tipos_transaccion)

    print("\n--- Recuento de Transacciones ---")
    for tipo, cantidad in recuento.items():
        print(f"{tipo}: {cantidad}")
    print("-------------------------------")

def calcular_saldo_debito(transacciones):
    """Calcula el saldo de la cuenta de débito."""
    saldo = 0
    for transaccion in transacciones:
        tipo, _, _, _, monto = transaccion
        try:
            monto = float(monto)
            if tipo == "Ingreso":
                saldo += monto
            elif tipo == "Gasto":
                saldo += monto
        except ValueError:
            print(f"Error: Monto inválido encontrado en la transacción: {transaccion}")
    return saldo

def calcular_total_ahorro(transacciones):
    """Calcula el total ahorrado."""
    total_ahorro = 0
    for transaccion in transacciones:
        tipo, _, _, _, monto = transaccion
        try:
            monto = float(monto)
            if tipo == "Ganancia":
                total_ahorro += monto
        except ValueError:
            print(f"Error: Monto inválido encontrado en la transacción: {transaccion}")
    return total_ahorro

def calcular_monto_credito(transacciones):
    """Calcula el monto actual de la deuda de crédito."""
    monto_credito = 0
    for transaccion in transacciones:
        tipo, _, _, _, monto = transaccion
        try:
            monto = float(monto)
            if tipo == "Deuda":
                monto_credito += monto
            elif tipo == "Pago":
                monto_credito += monto
        except ValueError:
            print(f"Error: Monto inválido encontrado en la transacción de crédito: {transaccion}")
    return monto_credito

def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    os.makedirs(DEBITO_DIR, exist_ok=True)
    os.makedirs(CREDITO_DIR, exist_ok=True)
    os.makedirs(AHORRO_DIR, exist_ok=True)

    while True:
        limpiar_pantalla()
        print("\n¿Qué tipo de cuenta deseas gestionar?")
        print("1. Débito (Ingresos y Gastos)")
        print("2. Crédito (Deudas)")
        print("3. Ahorro (Ganancias de Ventas)")
        print("4. Salir")

        opcion_cuenta = input("Selecciona una opción: ")

        if opcion_cuenta == '1':
            while True:
                limpiar_pantalla()
                nombre_archivo_debito = obtener_nombre_archivo("debito")
                print("\n¿Qué deseas hacer en la cuenta de Débito?")
                print("1. Ingresar un ingreso")
                print("2. Ingresar un gasto")
                print("3. Mostrar todas las transacciones de débito")
                print("4. Volver al menú principal")

                opcion_debito = input("Selecciona una opción: ")

                if opcion_debito == '1':
                    try:
                        monto = float(input("Ingrese el monto del ingreso: "))
                        transaccion = registrar_transaccion("Ingreso", monto)
                        guardar_transaccion(transaccion, nombre_archivo_debito)
                        print("Ingreso registrado correctamente en débito.")
                        input("Presiona Enter para continuar...")
                    except ValueError:
                        print("Monto inválido. Por favor, ingrese un número.")
                        input("Presiona Enter para continuar...")
                elif opcion_debito == '2':
                    try:
                        monto = float(input("Ingrese el monto del gasto: "))
                        transaccion = registrar_transaccion("Gasto", -monto)
                        guardar_transaccion(transaccion, nombre_archivo_debito)
                        print("Gasto registrado correctamente en débito.")
                        input("Presiona Enter para continuar...")
                    except ValueError:
                        print("Monto inválido. Por favor, ingrese un número.")
                        input("Presiona Enter para continuar...")
                elif opcion_debito == '3':
                    transacciones_debito = leer_transacciones(nombre_archivo_debito)
                    mostrar_tabla(transacciones_debito)
                    mostrar_recuento_transacciones(transacciones_debito)
                    saldo_debito = calcular_saldo_debito(transacciones_debito)
                    print(f"\n--- Saldo de Débito: ${saldo_debito:.2f} ---")
                    input("Presiona Enter para continuar...")
                elif opcion_debito == '4':
                    break
                else:
                    print("Opción inválida. Por favor, intenta de nuevo.")
                    input("Presiona Enter para continuar...")

        elif opcion_cuenta == '2':
            while True:
                limpiar_pantalla()
                nombre_archivo_credito = obtener_nombre_archivo("credito")
                print("\n¿Qué deseas hacer en la cuenta de Crédito (Deudas)?")
                print("1. Registrar una deuda")
                print("2. Registrar un pago a la deuda")
                print("3. Mostrar todas las transacciones de crédito")
                print("4. Volver al menú principal")

                opcion_credito = input("Selecciona una opción: ")

                if opcion_credito == '1':
                    try:
                        monto = float(input("Ingrese el monto de la deuda: "))
                        transaccion = registrar_transaccion("Deuda", -monto)
                        guardar_transaccion(transaccion, nombre_archivo_credito)
                        print("Deuda registrada correctamente.")
                        input("Presiona Enter para continuar...")
                    except ValueError:
                        print("Monto inválido. Por favor, ingrese un número.")
                        input("Presiona Enter para continuar...")
                elif opcion_credito == '2':
                    try:
                        monto = float(input("Ingrese el monto del pago: "))
                        transaccion = registrar_transaccion("Pago", monto)
                        guardar_transaccion(transaccion, nombre_archivo_credito)
                        print("Pago registrado correctamente.")
                        input("Presiona Enter para continuar...")
                    except ValueError:
                        print("Monto inválido. Por favor, ingrese un número.")
                        input("Presiona Enter para continuar...")
                elif opcion_credito == '3':
                    transacciones_credito = leer_transacciones(nombre_archivo_credito)
                    mostrar_tabla(transacciones_credito)
                    mostrar_recuento_transacciones(transacciones_credito)
                    monto_credito_actual = calcular_monto_credito(transacciones_credito)
                    print(f"\n--- Monto Total de Crédito (Deuda Actual): ${monto_credito_actual:.2f} ---")
                    input("Presiona Enter para continuar...")
                elif opcion_credito == '4':
                    break
                else:
                    print("Opción inválida. Por favor, intenta de nuevo.")
                    input("Presiona Enter para continuar...")

        elif opcion_cuenta == '3':
            while True:
                limpiar_pantalla()
                nombre_archivo_ahorro = obtener_nombre_archivo("ahorro")
                print("\n¿Qué deseas hacer en la cuenta de Ahorro (Ganancias de Ventas)?")
                print("1. Registrar una ganancia")
                print("2. Mostrar todas las ganancias")
                print("3. Volver al menú principal")

                opcion_ahorro = input("Selecciona una opción: ")

                if opcion_ahorro == '1':
                    try:
                        monto = float(input("Ingrese el monto de la ganancia: "))
                        transaccion = registrar_transaccion("Ganancia", monto)
                        guardar_transaccion(transaccion, nombre_archivo_ahorro)
                        print("Ganancia registrada correctamente en ahorro.")
                        input("Presiona Enter para continuar...")
                    except ValueError:
                        print("Monto inválido. Por favor, ingrese un número.")
                        input("Presiona Enter para continuar...")
                elif opcion_ahorro == '2':
                    transacciones_ahorro = leer_transacciones(nombre_archivo_ahorro)
                    mostrar_tabla(transacciones_ahorro)
                    mostrar_recuento_transacciones(transacciones_ahorro)
                    total_ahorro = calcular_total_ahorro(transacciones_ahorro)
                    print(f"\n--- Total Ahorrado: ${total_ahorro:.2f} ---")
                    input("Presiona Enter para continuar...")
                elif opcion_ahorro == '3':
                    break
                else:
                    print("Opción inválida. Por favor, intenta de nuevo.")
                    input("Presiona Enter para continuar...")

        elif opcion_cuenta == '4':
            limpiar_pantalla()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
