import os
import random

prefijos = [
    "Pilares de la ingeniería ",
    "Procesos de la ingeniería ",
    "Fundamentos de ",
    "Principios de ",
    "Aplicaciones modernas de ",
    "Conocimientos de ",
    "Sistematizacion de ",
    "Calidad en el desarrollo de ",
    "El gran libro de "
    "Handbook de "
]
categorias = [
    "Ambiental", "Informática",
    "Artes", "Filosofía", "Economía", "Educación","Industrial","Civil","Biodiversidad y recursos geneticos",
    "Derecho","Arquitectura","Hoteleria y turismo","Ciencias de la salud","Robotica","Mecanica"
]
autores = [
    "Carlos Pérez", "Andrea Gómez", "Luis Martínez", "María Torres",
    "Fernando Ortega", "Patricia León", "Ricardo Gualán", "Julia Herrera",
    "Esteban Aguilar", "Verónica Salazar","Carlos Javier","Daniel Martinez",
    "Agustin Reboredo","Paul Clements","Alfons Gonzalez","Fernando Jimenez",
    "Kenneth E. Kendall","Nicolas Sau","Julio Martin","Daniela Lopez","Jose Munoz",
    "Jose Rafael","Sebastian Raschka","Guillermo Pantaleon","Sergio Gomez","Nuria Alvarez"
]
editoriales = [
    "McGraw-Hill", "Pearson", "Alfaomega", "Cengage", "Oxford Press",
    "Springer", "Cambridge Press", "Marcombo", "Reverté", "Panamericana","Santillana"
]
formatos = ["Físico", "Digital"]
iteraciones = int(input("Ingrese cuántos libros desea generar: "))
fname = "DatasetLibros.csv"
write_header = (not os.path.exists(fname)) or os.path.getsize(fname) == 0

with open(fname, "a+", encoding="utf-8", newline="") as base:
    if write_header:
        base.write("libro,autor,editorial,anio_publicacion,num_paginas,formato,categoria,rating,popularidad_libro\n")
    for _ in range(iteraciones):
        categoria = random.choice(categorias)
        prefijo = random.choice(prefijos)
        nombre_libro = f"{prefijo}{categoria}"
        autor = random.choice(autores)
        editorial = random.choice(editoriales)
        formato = random.choice(formatos)
        anio_publicacion = random.randint(2000, 2022)
        num_paginas = random.randint(120, 800)
        rating = round(random.uniform(0, 5), 2)
        popularidad_libro = random.randint(1, 10)

        base.write(f"{nombre_libro},{autor},{editorial},{anio_publicacion},{num_paginas},{formato},{categoria},{rating},{popularidad_libro}\n")

print("DatasetLibros.csv generado")
