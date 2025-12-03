import os
from datetime import datetime

ARCHIVO = "biblioteca.txt"

class BibliotecaError(Exception):
    pass

class LibroNoEncontradoError(BibliotecaError):
    pass

class LibroPrestadoError(BibliotecaError):
    pass

class Libro:
    def __init__(self, titulo, autor, anio, estado="disponible"):
        self._titulo = titulo
        self._autor = autor
        self._anio = int(anio)
        self._estado = estado

    @property
    def titulo(self):
        return self._titulo
    @property
    def autor(self):
        return self._autor
    @property
    def anio(self):
        return self._anio
    @property
    def estado(self):
        return self._estado

    def prestar(self):
        if self._estado == "prestado":
            raise LibroPrestadoError(f"'{self._titulo}' ya esta prestado")
        self._estado = "prestado"

    def devolver(self):
        if self._estado == "disponible":
            raise BibliotecaError(f"'{self._titulo}' no esta prestado")
        self._estado = "disponible"

    def __str__(self):
        est = "Disponible" if self._estado == "disponible" else "Prestado"
        return f"Titulo: {self._titulo}, Autor: {self._autor}, Año: {self._anio}, Estado: {est}"

    def serializar(self):
        return f"LIBRO|{self._titulo}|{self._autor}|{self._anio}|{self._estado}\n"

class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, estado="disponible"):
        super().__init__(titulo, autor, anio, estado)
        self._formato = formato

    @property
    def formato(self):
        return self._formato

    def __str__(self):
        base = super().__str__()
        return f"{base}, Formato: {self._formato}"

    def serializar(self):
        return f"DIGITAL|{self._titulo}|{self._autor}|{self._anio}|{self._estado}|{self._formato}\n"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def cargar(self, ruta=ARCHIVO):
        if not os.path.exists(ruta):
            return
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.rstrip("\n")
                if not linea:
                    continue
                partes = linea.split("|")
                tipo = partes[0]
                if tipo == "LIBRO" and len(partes) >= 5:
                    _, titulo, autor, anio, estado = partes[:5]
                    self.libros.append(Libro(titulo, autor, anio, estado))
                elif tipo == "DIGITAL" and len(partes) >= 6:
                    _, titulo, autor, anio, estado, formato = partes[:6]
                    self.libros.append(LibroDigital(titulo, autor, anio, formato, estado))

    def guardar(self, ruta=ARCHIVO):
        with open(ruta, "w", encoding="utf-8") as f:
            for lib in self.libros:
                f.write(lib.serializar())

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_por_indice(self, indice_1based):
        idx = indice_1based - 1
        if idx < 0 or idx >= len(self.libros):
            raise IndexError("Indice fuera de rango")
        del self.libros[idx]

    def marcar_prestado_por_indice(self, indice_1based):
        idx = indice_1based - 1
        if idx < 0 or idx >= len(self.libros):
            raise IndexError("Indice fuera de rango")
        self.libros[idx].prestar()

    def devolver_por_indice(self, indice_1based):
        idx = indice_1based - 1
        if idx < 0 or idx >= len(self.libros):
            raise IndexError("Indice fuera de rango")
        self.libros[idx].devolver()

    def listar_todos(self):
        return list(self.libros)

    def buscar_por_subcadena(self, texto):
        key = texto.lower()
        return [ (i+1, l) for i, l in enumerate(self.libros) if key in l.titulo.lower() ]

# utilidades
def leer_texto(prompt):
    return input(prompt).strip()

def leer_int(prompt):
    while True:
        v = input(prompt).strip()
        if v.isdigit():
            return int(v)
        print("Entrada invalida. Ingrese un numero valido.")

def leer_int_en_rango(prompt, minimo, maximo):
    if minimo > maximo:
        raise ValueError("rango invalido")
    while True:
        n = leer_int(prompt)
        if minimo <= n <= maximo:
            return n
        print(f"Ingrese un numero entre {minimo} y {maximo}.")

def mostrar_lista_indexada(lista):
    if not lista:
        print("No hay libros.")
        return
    for i, lib in enumerate(lista, 1):
        print(f"{i}. {lib}")

def mostrar_lista_indexada_con_tuplas(lista_tuplas):
    # recibe [(indice_original, libro), ...] y muestra indice original
    if not lista_tuplas:
        print("No hay libros.")
        return
    for idx, lib in lista_tuplas:
        print(f"{idx}. {lib}")

biblioteca = Biblioteca()
try:
    biblioteca.cargar()
except Exception as e:
    print("Error cargando archivo:", e)

try:
    while True:
        print("\n--- Gestor de Biblioteca ---")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Ver todos los libros")
        print("4. Buscar libro")
        print("5. Marcar libro como prestado")
        print("6. Devolver libro")
        print("7. Salir")
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            tipo = input("Tipo (normal/digital) [n/d]: ").strip().lower()
            titulo = leer_texto("Titulo: ")
            autor = leer_texto("Autor: ")
            anio = leer_int("Anio: ")
            if tipo == "d":
                formato = leer_texto("Formato (PDF/ePub/...): ")
                libro = LibroDigital(titulo, autor, anio, formato)
            else:
                libro = Libro(titulo, autor, anio)
            biblioteca.agregar_libro(libro)
            print("Libro agregado.")

        elif opcion == "2":
            lista = biblioteca.listar_todos()
            if not lista:
                print("No hay libros para eliminar.")
                continue
            mostrar_lista_indexada(lista)  # muestra indices 1..n
            idx = leer_int_en_rango("Selecciona el numero del libro a eliminar: ", 1, len(lista))
            try:
                biblioteca.eliminar_por_indice(idx)
                print("Libro eliminado.")
            except Exception as e:
                print("Error:", e)

        elif opcion == "3":
            mostrar_lista_indexada(biblioteca.listar_todos())

        elif opcion == "4":
            texto = leer_texto("Texto a buscar (parte del titulo): ")
            resultados = biblioteca.buscar_por_subcadena(texto)
            if resultados:
                # mostrar con indice original en biblioteca
                mostrar_lista_indexada_con_tuplas(resultados)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "5":
            lista = biblioteca.listar_todos()
            if not lista:
                print("No hay libros para marcar.")
                continue
            mostrar_lista_indexada(lista)  # muestra indices 1..n
            idx = leer_int_en_rango("Selecciona el numero del libro a marcar como prestado: ", 1, len(lista))
            try:
                biblioteca.marcar_prestado_por_indice(idx)
                print("Libro marcado como prestado.")
            except BibliotecaError as e:
                print("Error:", e)
            except Exception as e:
                print("Error:", e)

        elif opcion == "6":
            lista = biblioteca.listar_todos()
            if not lista:
                print("No hay libros para devolver.")
                continue
            mostrar_lista_indexada(lista)  # muestra indices 1..n
            idx = leer_int_en_rango("Selecciona el numero del libro a devolver: ", 1, len(lista))
            try:
                biblioteca.devolver_por_indice(idx)
                print("Libro devuelto.")
            except BibliotecaError as e:
                print("Error:", e)
            except Exception as e:
                print("Error:", e)

        elif opcion == "7":
            print("Guardando cambios y saliendo...")
            break
        else:
            print("Opcion invalida.")
finally:
    try:
        biblioteca.guardar()
    except Exception as e:
        print("Error guardando archivo:", e)
