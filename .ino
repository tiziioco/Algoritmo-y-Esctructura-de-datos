import random

inventario = {
    'computadoras': [('laptop', 5), ('pc de escritorio', 3)],
    'accesorios': [('mouse', 10), ('teclado', 6)],
    'periféricos': [('monitor', 4), ('impresora', 2)]
}

for i in range(3):
    categoria = random.choice(list(inventario.keys()))
    if inventario[categoria]:
        indice = random.randrange(len(inventario[categoria]))
        nombre_producto, cantidad = inventario[categoria][indice]
        print(f"Venta {i+1}: {nombre_producto} (categoría: {categoria})")
        if cantidad == 1:
            inventario[categoria].pop(indice)
        else:
            inventario[categoria][indice] = (nombre_producto, cantidad - 1)
    else:
        print(f"Venta {i+1}: No se puede vender en la categoría '{categoria}' (vacía)")

categoria_reposicion = random.choice(list(inventario.keys()))
nuevo_producto = ('auriculares', 7)
inventario[categoria_reposicion].append(nuevo_producto)
print(f"\nReposición: Se añadió {nuevo_producto[0]} (cantidad: {nuevo_producto[1]}) a la categoría '{categoria_reposicion}'")

print("\nResumen Final del Inventario:")
for categoria, productos in inventario.items():
    print(f"\nCategoría: {categoria}")
    if productos:
        for nombre, cantidad in productos:
            print(f" - {nombre}: {cantidad} unidades")
    else:
        print(" - Sin productos en inventario.")
