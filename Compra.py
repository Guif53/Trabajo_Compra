# Definir la tupla de alimentos con categorías y productos
alimentos = (
    ("Frutas", ["Manzanas", "Plátanos", "Naranjas", "Peras"]),
    ("Verduras", ["Lechuga", "Tomates", "Zanahorias", "Pepinos"]),
    ("Carnes", ["Filetes Adobados", "Albóndigas", "Hamburguesas", "Pechuga de Pollo"]),
    ("Pescados", ["Salmón", "Merluza", "Atún", "Bacalao"]),
    ("Congelados", ["Helado", "Pizza Congelada", "Vegetales Congelados", "Croquetas"]),
    ("Pasta", ["Espaguetis", "Macarrones", "Lasaña", "Fideos"]),
    ("Dulces", ["Chocolate", "Galletas", "Tartas", "Caramelos"])
)

# Asignar precios fijos para Mercadona y Alcampo
precios_mercadona = {
    "Manzanas": 2.50, "Plátanos": 1.80, "Naranjas": 2.20, "Peras": 2.60,
    "Lechuga": 1.50, "Tomates": 2.00, "Zanahorias": 1.70, "Pepinos": 1.90,
    "Filetes Adobados": 7.00, "Albóndigas": 5.50, "Hamburguesas": 6.20, "Pechuga de Pollo": 7.80,
    "Salmón": 12.00, "Merluza": 10.00, "Atún": 9.50, "Bacalao": 11.00,
    "Helado": 4.50, "Pizza Congelada": 5.00, "Vegetales Congelados": 3.50, "Croquetas": 4.00,
    "Espaguetis": 2.30, "Macarrones": 2.20, "Lasaña": 3.50, "Fideos": 1.80,
    "Chocolate": 3.00, "Galletas": 2.50, "Tartas": 5.50, "Caramelos": 1.50
}

precios_alcampo = {
    "Manzanas": 2.40, "Plátanos": 1.70, "Naranjas": 2.10, "Peras": 2.50,
    "Lechuga": 1.40, "Tomates": 1.90, "Zanahorias": 1.60, "Pepinos": 1.80,
    "Filetes Adobados": 6.90, "Albóndigas": 5.40, "Hamburguesas": 6.10, "Pechuga de Pollo": 7.70,
    "Salmón": 11.90, "Merluza": 9.90, "Atún": 9.40, "Bacalao": 10.90,
    "Helado": 4.40, "Pizza Congelada": 4.90, "Vegetales Congelados": 3.40, "Croquetas": 3.90,
    "Espaguetis": 2.20, "Macarrones": 2.10, "Lasaña": 3.40, "Fideos": 1.70,
    "Chocolate": 2.90, "Galletas": 2.40, "Tartas": 5.40, "Caramelos": 1.40
}

# Función para mostrar el menú principal
def mostrar_menu_principal():
    print("\n--- Secciones de Alimentos ---")
    for i, (categoria, _) in enumerate(alimentos, 1):
        print(f"{i}. {categoria}")
    print("0. Terminar Compra")

# Función para mostrar el menú de productos de una categoría
def mostrar_menu_productos(categoria, productos):
    print(f"\n--- {categoria} ---")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto}")
    print("0. Volver al Menú Principal")

# Función para pedir un número entero
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Seleccione el numero que tiene al lado el prducto porfavor o ponga un número entero")
            

# Función principal para gestionar la compra
def gestionar_compra():
    carrito = {}
    while True:
        mostrar_menu_principal()
        opcion = pedir_entero("Selecciona una opción: ")
        if opcion == 0:
            break
        elif 1 <= opcion <= len(alimentos):
            categoria, productos = alimentos[opcion - 1]
            while True:
                mostrar_menu_productos(categoria, productos)
                opcion_producto = pedir_entero("Selecciona un producto: ")
                if opcion_producto == 0:
                    break
                elif 1 <= opcion_producto <= len(productos):
                    producto = productos[opcion_producto - 1]
                    cantidad = pedir_entero(f"¿Cuántas unidades de {producto} quieres comprar? ")
                    if cantidad > 0:
                        if producto in carrito:
                            carrito[producto] += cantidad
                        else:
                            carrito[producto] = cantidad
    return carrito

# El resto del código permanece igual


# Función para calcular el total de la compra
def calcular_total(carrito, precios):
    total = 0
    detalle = []
    for producto, cantidad in carrito.items():
        precio_total = precios[producto] * cantidad
        detalle.append((producto, precios[producto], cantidad, precio_total))
        total += precio_total
    return total, detalle

# Función para calcular el costo de viaje a un supermercado
def calcular_costo_viaje(kilometros):
    consumo_gasolina = 8 / 100  # 8 litros cada 100 km
    precio_gasolina = 1.55  # Precio por litro
    litros_necesarios = consumo_gasolina * kilometros
    costo_viaje = litros_necesarios * precio_gasolina
    return costo_viaje

# Función principal
def main():
    carrito = gestionar_compra()
    
    total_mercadona, detalle_mercadona = calcular_total(carrito, precios_mercadona)
    total_alcampo, detalle_alcampo = calcular_total(carrito, precios_alcampo)
    
    print("\n--- Resumen de la Compra ---")
    for producto, cantidad in carrito.items():
        print(f"{producto}: {cantidad} unidades")
    
    print("\n--- Detalle de Precios en Mercadona ---")
    for producto, precio, cantidad, total in detalle_mercadona:
        print(f"{producto}: {cantidad} unidades a {precio:.2f} € cada una, Total: {total:.2f} €")
    
    print(f"\nTotal en Mercadona: {total_mercadona:.2f} €")
    
    print("\n--- Detalle de Precios en Alcampo ---")
    for producto, precio, cantidad, total in detalle_alcampo:
        print(f"{producto}: {cantidad} unidades a {precio:.2f} € cada una, Total: {total:.2f} €")
    
    print(f"\nTotal en Alcampo: {total_alcampo:.2f} €")
    
    # Preguntar distancia a los supermercados
    km_mercadona = float(input("\n¿A cuántos kilómetros está el Mercadona? "))
    km_alcampo = float(input("¿A cuántos kilómetros está el Alcampo? "))
    
    # Calcular costo de viaje a cada supermercado
    costo_viaje_mercadona = calcular_costo_viaje(km_mercadona)
    costo_viaje_alcampo = calcular_costo_viaje(km_alcampo)
    
    print("\nSuponiendo que el litro de gasolina esta a 1,55€ y nuestro coche gasta 8 litros cada 100 km")
    print(f"El costo del viaje al Mercadona sale a: {costo_viaje_mercadona:.2f} €")
    print(f"El costo del viaje al Alcampo sale a: {costo_viaje_alcampo:.2f} €")
    
    # Calcular costo total incluyendo viaje
    costo_total_mercadona = total_mercadona + costo_viaje_mercadona
    costo_total_alcampo = total_alcampo + costo_viaje_alcampo
    
    print(f"\nEl costo total en el Mercadona (incluyendo viaje) es: {costo_total_mercadona:.2f} €")
    print(f"El costo total en el Alcampo (incluyendo viaje) es: {costo_total_alcampo:.2f} €")
    
    # Determinar el supermercado más rentable
    if costo_total_mercadona < costo_total_alcampo:
        print("\nEl supermercado más rentable es el Mercadona.") 
    elif costo_total_alcampo < costo_total_mercadona:
        print("\nEl supermercado más rentable es el Alcampo.") 
    else: 
        print("\nAmbos supermercados son igual de rentables.")

if __name__ == "__main__":
    main()