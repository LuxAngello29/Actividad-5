# -*- coding: utf-8 -*-
"""ejercicio_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11d4tKphHuJhUdwUcl0K5WprC5fjLwbSa
"""

class ValidacionError(Exception):
    pass


class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = []

    def esta_lleno(self):
        return len(self.programadores) >= 3

    def añadir_programador(self, programador):
        if self.esta_lleno():
            raise ValidacionError("El equipo está completo. No se puede agregar más programadores.")
        self.programadores.append(programador)

    @staticmethod
    def validar_campo(campo):
        if len(campo) > 20:
            raise ValidacionError("La longitud no debe ser superior a 20 caracteres.")
        for c in campo:
            if c.isdigit():
                raise ValidacionError("El nombre o apellido no puede contener dígitos.")


def main():
    try:
        nombre_equipo = input("Nombre del equipo: ")
        universidad = input("Universidad: ")
        lenguaje = input("Lenguaje de programación: ")

        equipo = EquipoMaratonProgramacion(nombre_equipo, universidad, lenguaje)

        for i in range(3):
            print(f"\nDatos del integrante {i + 1}:")
            nombre = input("Nombre del integrante: ")
            EquipoMaratonProgramacion.validar_campo(nombre)

            apellidos = input("Apellidos del integrante: ")
            EquipoMaratonProgramacion.validar_campo(apellidos)

            programador = Programador(nombre, apellidos)
            equipo.añadir_programador(programador)

        print("\nEquipo registrado correctamente con los siguientes integrantes:")
        for p in equipo.programadores:
            print(f"{p.nombre} {p.apellidos}")

    except ValidacionError as e:
        print(f"Error de validación: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


# Ejecutar el programa
if __name__ == "__main__":
    main()

