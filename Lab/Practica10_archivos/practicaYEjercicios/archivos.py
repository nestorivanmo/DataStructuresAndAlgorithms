# -*- coding: utf-8 -*-
import locale
import pickle
import os

# try:
#     file = open("open.py", "r", encoding='utf-8')
#     print(locale.getpreferredencoding())
#     print(locale.setlocale(locale.LC_ALL, ''))
# except:
#     print('No fue posible abrir el archivo.')
# finally:
#     if file:
#         file.close()


# with open("open.py", "r", encoding='utf-8') as file:
#     print(locale.getpreferredencoding())
#     print(locale.setlocale(locale.LC_ALL, ''))


# file = open("attributes.py", 'r')
# name = file.name
# mode = file.mode
# encoding = file.encoding
# file.close()
# print("Name: ",name)
# print("Mode: ",mode)
# print("Encoding: ",encoding)
# print("Closed file?: ", file.closed)

# print("read()")
# with open("read.py", "r", encoding='utf-8') as file:
#     print(file.read())
# print("\nread(-111)")
# with open("read.py", "r", encoding='utf-8') as file:
#     print(file.read(-111))
# print("\nread(10)")
# with open("read.py", "r", encoding='utf-8') as file:
#     print(file.read(10))
#
# print("\nread(10) binary")
# with open("read.py", "rb") as file:
#     print(file.read(10))
# with open("read.py", "r") as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)

# print("readline()")
# with open("readline.py", "r", encoding='utf-8') as file:
#     print(file.readline())
# with open("readline.py", "r", encoding='utf-8') as file:
#     for line in file:
#         print(line)
# with open("readline.py", "r", encoding='utf-8') as file:
#     print(list(file))
# with open("readline.py", "r", encoding='utf-8') as file:
#     print(file.readlines())

# numbers = ['hello', 'world']
# print("write()")
# with open("file.txt", "w") as file:
#     print(file.write("Hello world!"))
#     print(file.writelines(numbers))
# with open("file.txt", "r") as file:
#     print(file.readlines())

# tell(): indica la posición del cursor dentro del archivo

# print("tell()")
# with open("tell.py", "r") as file:
#     print(file.tell())
#     print(file.readline())
#     print(file.tell())

# seek(): permite cambiar la posición del objeto file en el archivo.

# print("seek()")
# with open("seek.py", "r") as file:
#     print(file.tell())
#     print(file.readline())
#     print(file.tell())
#     print(file.seek(30))
#     print(file.readline())
#     print(file.seek(3, 0))
#     print(file.readline())
#     # print(file.seek(-2, 2))
#     # print(file.readline())

# Biblioteca pickle
    # dump(): permite escribir la lista de datos en el archivo
    # load(): lee los datos del archivo en forma de cadena

# print("pickle")
# memory = ['Hello','world','!!']
# file = open('list.txt', 'wb')
# pickle.dump(memory, file)
# file.close()
# file = open('list.txt', 'rb')
# file_memory = pickle.load(file)
# file.close()
# print(file_memory)


# Biblioteca os: funciones para operar directamente con el sistema operativo
    # os.mkdir(path, mode): crea la carpeta con el nombre path y el nivel de acceso en mode
    # os.chdir(path): cambia el directorio de trabajo actal por el enviado en path


# def make_dir(path):
#     try:
#         os.mkdir(path)
#     except:
#         print("Error al crear el archivo", path)
#     os.chdir(path)
#
# print("os.mkdir")
# make_dir("test1")

#CADENAS en python
# subcadenas -> cadena[inicio:fin]
# Búsqueda en cadenas:
    # cadena.find()
    # cadena.find("patron", indice)

# Cadena original
# cadena = "Amor y deseo son dos cosas diferentes; que no todo lo que se ama se desea, ni todo lo que se desea se ama. (Don Quijote)"
# # Busca la cadena "ama"
# print (cadena.find("ama"))
# #Imprimie la subcadena
# print (cadena[cadena.find("ama"):])
#
# # Busca la siguiente coincidencia de "ama"
# print (cadena[cadena.find("ama") + 1:].find("ama"))
# # Imprime la cadena a partir de la segunda coincidencia
# print (cadena[61 + 1 + 40:])
# # Busca "corazon" en la cadena
# print (cadena.find("corazon"))
# # Busca a partir de un indice
# print(cadena.find("todo", 62))
# # Imprime a partir de un índice y hasta el final
# print (cadena[75:])


# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# impr = ["Aprobados", "No aprobados", "deserción", "NP"]
# vol = [2, 10, 20, 10]
# expl =(0.05, 0.05, 0, 0)
# fig1, ax1 = plt.subplots()
# ax1.pie(vol, explode=expl, labels=impr, autopct='%1.1f%%', shadow=True,startangle=90)
# plt.show()

# impr = ["Aprobados", "No aprobados", "deserción", "NP"] vol = [2, 10, 20, 10]
# expl =(0.05, 0.05, 0, 0)
# fig1, ax1 = plt.subplots()
# ax1.pie(vol, explode=expl, labels=impr, autopct='%1.1f%%', shadow=True,startangle=90)
# plt.show()
