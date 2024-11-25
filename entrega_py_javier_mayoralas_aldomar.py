# Clase que representa un artículo en el inventario
class Articulo:
    # Constructor de la clase. Inicializa el artículo con nombre, categoría, precio y stock.
    def __init__(self, nombre, categoria, precio, stock):
        self.__nombre = nombre        # Nombre del artículo
        self.__categoria = categoria  # Categoría del artículo
        self.__precio = precio        # Precio del artículo
        self.__stock = stock          # Cantidad en stock del artículo

    # Getter y setter para el nombre del artículo
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor  # Permite actualizar el nombre del artículo

    # Getter y setter para la categoría del artículo
    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        self.__categoria = valor

    # Getter y setter para el precio del artículo
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor > 0:  # El precio no puede ser negativo o cero
            self.__precio = valor
        else:
            raise ValueError("El precio debe ser mayor que 0.")  # Si el precio no es válido, muestra un error

    # Getter y setter para el stock del artículo
    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if valor >= 0:  # El stock no puede ser negativo
            self.__stock = valor
        else:
            raise ValueError("La cantidad en stock debe ser mayor o igual a 0.")  # Si el stock es negativo, muestra un error

    # Método que devuelve una representación en texto del artículo
    def __str__(self):
        return f"{self.__nombre} | {self.__categoria} | {self.__precio:.2f} € | {self.__stock}"

# Clase que gestiona el inventario de artículos
class GestorInventario:
    # Constructor de la clase. Inicializa el inventario vacío y un contador para los IDs de los artículos.
    def __init__(self):
        self.__articulos = {}  # Diccionario para almacenar los artículos
        self.__contador_id = 1  # Contador para asignar un ID único a cada artículo

    # Método para añadir un nuevo artículo al inventario
    def añadir_articulo(self, nombre, categoria, precio, stock):
        # Verifica si el artículo ya está en el inventario por su nombre
        for articulo in self.__articulos.values():
            if articulo.nombre == nombre:
                print(f"Error: El artículo '{nombre}' ya está registrado en el inventario.")
                return
        # Si no existe, crea el artículo y lo agrega al inventario con un ID único
        articulo = Articulo(nombre, categoria, precio, stock)
        self.__articulos[self.__contador_id] = articulo
        print(f"Artículo añadido con ID {self.__contador_id}: {articulo}")
        self.__contador_id += 1  # Incrementa el contador para el siguiente artículo

    # Método para actualizar el artículo (incluyendo nombre, precio y stock)
    def actualizar_articulo(self, articulo_id, nuevo_nombre=None, nuevo_precio=None, nuevo_stock=None):
        articulo = self.__articulos.get(articulo_id)  # Busca el artículo por su ID
        if articulo:
            # Si se proporciona un nuevo nombre, lo actualiza
            if nuevo_nombre is not None:
                articulo.nombre = nuevo_nombre  # Usa el setter para cambiar el nombre del artículo
                print(f"Nombre actualizado a '{nuevo_nombre}'.")
            
            # Si se proporciona un nuevo precio, lo actualiza
            if nuevo_precio is not None:
                try:
                    articulo.precio = nuevo_precio  # Usa el setter para validar el nuevo precio
                    print(f"Precio actualizado a {nuevo_precio:.2f} €.")
                except ValueError as e:
                    print(e)  # Si el precio no es válido, muestra el error

            # Si se proporciona un nuevo stock, lo actualiza
            if nuevo_stock is not None:
                try:
                    articulo.stock = nuevo_stock  # Usa el setter para validar el nuevo stock
                    print(f"Cantidad en stock actualizada a {nuevo_stock}.")
                except ValueError as e:
                    print(e)  # Si el stock no es válido, muestra el error
        else:
            print(f"Error: No se encontró un artículo con ID {articulo_id}.")

    # Método para eliminar un artículo del inventario
    def eliminar_articulo(self, articulo_id):
        if articulo_id in self.__articulos:
            eliminado = self.__articulos.pop(articulo_id)  # Elimina el artículo por su ID
            print(f"Artículo '{eliminado.nombre}' eliminado del inventario.")
        else:
            print(f"Error: No se encontró un artículo con ID {articulo_id}.")

    # Método para mostrar todo el inventario de artículos
    def mostrar_inventario(self):
        if not self.__articulos:  # Si el inventario está vacío, muestra un mensaje
            print("El inventario está vacío.")
        else:
            # Muestra una tabla con los artículos en el inventario
            print("+----+----------------+----------------+-----------+----------+")
            print("| ID | Nombre         | Categoría      | Precio/u  | Cantidad |")
            print("+----+----------------+----------------+-----------+----------+")
            for id_articulo, articulo in self.__articulos.items():
                print(
                    f"| {id_articulo:<2} | {articulo.nombre:<14} | {articulo.categoria:<14} | {articulo.precio:>7.2f} € | {articulo.stock:<8} |"
                )
            print("+----+----------------+----------------+-----------+----------+")

    # Método para buscar un artículo por su ID
    def buscar_articulo(self, articulo_id):
        return self.__articulos.get(articulo_id)

    # Método para buscar un artículo por su nombre
    def buscar_articulo_por_nombre(self, nombre):
        if not self.__articulos:  # Si el inventario está vacío, muestra un mensaje
            print("Error: El inventario está vacío. No se puede realizar la búsqueda.")
            return

        # Busca los artículos que coinciden con el nombre proporcionado
        encontrados = [
            (id_articulo, articulo) for id_articulo, articulo in self.__articulos.items() if articulo.nombre.lower() == nombre.lower()
        ]
        if encontrados:
            # Muestra los artículos encontrados en una tabla
            print("+----+----------------+----------------+-----------+----------+")
            print("| ID | Nombre         | Categoría      | Precio/u  | Cantidad |")
            print("+----+----------------+----------------+-----------+----------+")
            for id_articulo, articulo in encontrados:
                print(
                    f"| {id_articulo:<2} | {articulo.nombre:<14} | {articulo.categoria:<14} | {articulo.precio:>7.2f} € | {articulo.stock:<8} |"
                )
            print("+----+----------------+----------------+-----------+----------+")
        else:
            print(f"No se encontró ningún artículo con el nombre '{nombre}'.")

# Función principal que muestra un menú para interactuar con el inventario
def menu_principal():
    inventario = GestorInventario()  # Crea una instancia de la clase GestorInventario

    while True:  # Bucle infinito que muestra el menú hasta que el usuario decida salir
        print("\n=== Menú de Gestión de Inventario ===")
        print("1. Añadir artículo")
        print("2. Actualizar artículo")
        print("3. Eliminar artículo")
        print("4. Mostrar inventario")
        print("5. Buscar artículo por nombre")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Añadir artículo
            nombre = input("Introduce el nombre del artículo: ")
            categoria = input("Introduce la categoría del artículo: ")
            try:
                precio = float(input("Introduce el precio por unidad (en €. Los decimales se separan con un punto): "))  # El precio debe ser un número decimal
                stock = int(input("Introduce la cantidad en stock: "))  # El stock debe ser un número entero
                inventario.añadir_articulo(nombre, categoria, precio, stock)
            except ValueError:
                print("Error: El precio y la cantidad deben ser valores numéricos válidos.")  # Mensaje si hay un error en los valores
        elif opcion == "2":
            # Actualizar artículo
            try:
                articulo_id = int(input("Introduce el ID del artículo a actualizar: "))  # ID del artículo
                nuevo_nombre = input("Introduce el nuevo nombre (deja en blanco para no cambiarlo): ")
                nuevo_precio = input("Introduce el nuevo precio por unidad (€) (deja en blanco para no cambiarlo): ")
                nuevo_stock = input("Introduce la nueva cantidad (deja en blanco para no cambiarla): ")

                # Llamamos al método para actualizar el artículo, pasando los nuevos valores
                inventario.actualizar_articulo(
                    articulo_id,
                    nuevo_nombre if nuevo_nombre else None,
                    float(nuevo_precio) if nuevo_precio else None,
                    int(nuevo_stock) if nuevo_stock else None,
                )
            except ValueError:
                print("Error: El ID, precio y cantidad deben ser valores numéricos válidos.")  # Mensaje si hay un error en los valores
        elif opcion == "3":
            # Eliminar artículo
            try:
                articulo_id = int(input("Introduce el ID del artículo a eliminar: "))
                inventario.eliminar_articulo(articulo_id)
            except ValueError:
                print("Error: El ID debe ser un número.")  # Mensaje si el ID no es un número
        elif opcion == "4":
            # Mostrar inventario
            inventario.mostrar_inventario()
        elif opcion == "5":
            # Buscar artículo por nombre
            nombre = input("Introduce el nombre del artículo a buscar: ")
            inventario.buscar_articulo_por_nombre(nombre)
        elif opcion == "6":
            print("Saliendo del programa.")  # Mensaje al salir
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")  # Mensaje si la opción no es válida

# Ejecuta el programa
if __name__ == "__main__":
    menu_principal()
