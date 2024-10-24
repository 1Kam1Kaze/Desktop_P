# 2. Numeritos, numeritos

# Haz un programa de Python que pida un número entero N al usuario entre 10 y 20.

# Muestra por pantalla todos los números enteros entre el 1 y el N.

# Muestra por pantalla todos los números enteros entre el 30 y el N, en orden inverso.

flag = True

while flag == True:

    print("")
    N = int(input("Escriba un número entre el 10 y el 20: "))

    if N >= 10 and N <= 20:
        flag = False
    else: 
        print("")
        print("Reingrese el número")

print("")
print("Normal ----------------------")

for i in range(1, N+1):
    print("")
    print(i)

print("")
print("Inverso --------------------")

for k in range(30,N,-1):
    print("")
    print(k)

print("")