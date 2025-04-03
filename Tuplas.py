    print("\n1. Registrar nuevo cliente.")
    print("2. Eliminar cliente.")
    print("3. Agregar lista de clientes.")
    print("0. Salir del Sistema.")
    print("... seleccione una opción.")
    return int(input("Opción: "))

def registrar_clientes():  
    nombre_cliente = input("Digite el nombre: ")
    apellido_cliente = input("Digite el apellido: ")
    cedula_cliente = input("Digite la cédula: ")
    return (nombre_cliente, apellido_cliente, cedula_cliente)  # Devuelve una tupla

def guardar_cliente(info_cliente, bd_clientes):
    bd_clientes.append(info_cliente)

def incluir_nueva_lista():
    aux_lista = []
    cantidad_nuevas = int(input("Digite la cantidad nueva de clientes: "))
    for _ in range(cantidad_nuevas):
        aux = registrar_clientes()
        aux_lista.append(aux)
    return aux_lista

# *Zona principal de código*
base_datos_clientes = []

while True:
    opcion = hacer_menu()
    
    match opcion:
        case 1:
            cliente = registrar_clientes()
            guardar_cliente(cliente, base_datos_clientes)
            print("\nCliente registrado con éxito!")

        case 2:
            if base_datos_clientes:
                print("\nClientes actuales:")
                for i, cliente in enumerate(base_datos_clientes):
                    print(f"{i + 1}. {cliente}")
                
                index = int(input("Ingrese el número del cliente a eliminar: ")) - 1
                if 0 <= index < len(base_datos_clientes):
                    eliminado = base_datos_clientes.pop(index)
                    print(f"\nCliente {eliminado} eliminado con éxito!")
                else:
                    print("\nNúmero inválido.")
            else:
                print("\nNo hay clientes registrados.")

        case 3:
            nueva_lista = incluir_nueva_lista()
            base_datos_clientes.extend(nueva_lista)
            print("\nLista de clientes agregada correctamente!")

        case 0:
            print("\nSaliendo del sistema...")
            break

        case _:
            print("\nOpción inválida. Intente de nuevo.")

    print("\nBase de datos actual:", base_datos_clientes)
