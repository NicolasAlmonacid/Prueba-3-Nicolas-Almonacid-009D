
#Autor Nicolas Almonacid 009D

import funciones

while true:
    print("Bienvanido a mantenedor de categorias: ")
    print("presione '1' para agregar categoria")
    print("presione '2' para editar categoria: ")
    print("presione '3' para eliminar categoria")
    print("presione '4' para buscar categoria")

    eleccion = int(input("Digite opcion"))
    eleccion = 0

    if eleccion == 1:
        nombre_anadir = input("anada nombre")
        agregar_categoria(nombre_anadir)

    if eleccion == 2:
        editar_categoria()

    if eleccion == 3:
        eliminar_categoria()

    if eleccion == 4:
        listar_categoria()


