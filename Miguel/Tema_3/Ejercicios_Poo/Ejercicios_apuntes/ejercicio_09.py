"""
Ejercicio 09 - Ejercicio Completo
"""
from abc import ABC, abstractmethod
from typing import List

class Recurso(ABC):
    """
    Docstring para Recurso
    -Es una interfaz
    -Atributos:
        titulo(string)->titulo del recurso
        tamano(int)->Tamaño en MB del recurso
    -Metodos:
        mostrar_info
    """
    def __init__(self,titulo:str,tamanio:int):
        self.titulo=titulo
        self.tamanio=tamanio

    @abstractmethod
    def mostrar_info(self):
        """
        Docstring para mostrar_info
        -Devuelve una descripcion del recurso
        """

class Video(Recurso):
    """
    Docstring para Video
    -Utiliza la interfaz recurso
    -Sobreescribe la funcion mostrar_info
    -Añade el atributo duracion(int)
    """
    def __init__(self,titulo:str,tamanio:int,duracion:int):
        super().__init__(titulo,tamanio)
        self.duracion=duracion

    def mostrar_info(self)->None:
        print(f"[VIDEO] {self.titulo} | Duración: {self.duracion} min | Tamaño: {self.tamanio} MB")

class DocumentoPDF(Recurso):
    """
    Docstring para DocumentoPDF
    -Utiliza la interfaz recurso
    -Sobreescribe la funcion mostrar_info
    -Añade el atributo num_paginas(int)
    """
    def __init__(self,titulo:str,tamanio:int,num_paginas:int):
        super().__init__(titulo,tamanio)
        self.num_paginas=num_paginas

    def mostrar_info(self)->None:
        print(f"[PDF] {self.titulo} | Páginas: {self.num_paginas} | Tamaño: {self.tamanio} MB")

class CursoInteractivo(Recurso):
    """
    Docstring para CursoInteractivo
    -Utiliza la interfaz recurso
    -Sobreescribe la funcion mostrar_info
    -Añade el atributo num_paginas(int)
    """
    def __init__(self,titulo:str,composicion:List[Recurso]):
        self.composicion=composicion
        tamanio_total = sum(curso.tamanio for curso in composicion)
        super().__init__(titulo,tamanio_total)

    def mostrar_info(self)->None:
        print(f"[CURSO] {self.titulo}. Tamaño total: {self.tamanio} MB")
        for curso_interactivo in self.composicion:
            print(f"    -{curso_interactivo.titulo} ({curso_interactivo.tamanio} MB)")

v1 = Video("Introducción a Redes", 300.0, 45)
v2 = Video("Práctica VLANs", 250.0, 35)
d1 = DocumentoPDF("Apuntes de Subredes", 5.0, 40)
curso = CursoInteractivo("Curso de Redes Básicas", [v1, v2, d1])
recursos: list[Recurso] = [v1,d1,curso]
for r in recursos:
    r.mostrar_info()
    print("-" * 40)
