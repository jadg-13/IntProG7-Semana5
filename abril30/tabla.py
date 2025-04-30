import time
import random
cont = 1
print("Aprendiendo las tablas")
print("¿Que tablas quiere aprender?")
numero = int(input("Dime un numero: "))
while cont <= 12:
    time.sleep(1)
    print(f"{cont} * {numero} = {cont * numero}")
    print("="*30)
    cont += 1

resp = 1
while resp != 0:
    num = random.randint(1, 12)
    mult = numero * num
    est = int(input(f"Cuanto es {numero} * {num}? "))
    if est == mult:
        print(f"Felicidades {numero} * {num} es igual a {mult}")
    else:
        print(f"Sigue intentando {numero} * {num} es igual a {mult}")
    resp = int(input("Quieres seguir practicando?"))
