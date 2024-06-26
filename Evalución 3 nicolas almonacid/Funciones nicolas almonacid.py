# Autor Nicolas Almonacid 009D

import json

def agregar_categoria(parNombre: str):
    with open("biblioteca.json", "r") as lector:
        agregar = json.load(lector)

        anadir= { 
            "CategoriaID": len(agregar["Categoria"]) +1,
            "Nombre": parNombre
        }
        agregar["Categoria"].append(anadir)

    with open ("biblioteca.json", "w") as escritor:
        json.dump(agregar, escritor, indent=4)


def editar_categoria():
    with open("biblioteca.json", "r") as lector:
        editar = json.load(lector)

        for i in editar["Categoria"]:
            if "CategoriaID" == 2:
                editar["CategoriaID"]["Nombre"] = "editor"
                break

    with open("biblioteca.json", "w") as escritor:
        json.dump(editar, escritor, indent=4)


def eliminar_categoria():
    with open("biblioteca.json", "r") as lector:
        eliminar = json.load(lector)

def listar_categoria():
    with open("biblioteca.json") as lector:
        listado = json.load(lector)

        for producto in listado["Categoria"]:
            print(f"{producto}")



        






