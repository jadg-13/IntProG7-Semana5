import os
op = 1
while op != 0:
    os.system("color 07")
    producto = input("Producto: ")
    precio = int(input("Precio: "))
    cantidad = int(input("Candidad: "))
    if cantidad < 0:
        print(f"\033[31m{cantidad}\033[0m")
    else:
        print(f"\033[32m{cantidad}\033[0m")

    with open("produtos.txt", "a", encoding = "utf-8") as p:
        p.write(f"\nProducto: {producto}\nPrecio: {precio}\nCantidad: {cantidad}\nTotal: {precio*cantidad}\n")
        p.write("="*10)
        p.write("\n")
    print("Producto agregado\n")
    op = int(input("Agregar otro? escriba 0 para salir"))
    
print("\nArchivo guardado")    