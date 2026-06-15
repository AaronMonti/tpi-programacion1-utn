# Trabajo Práctico Integrador - Gestión de Datos de Países

## Descripción

Este proyecto consiste en una aplicación desarrollada en Python la cual permite gestionar datos de países utilizando estructuras como listas y diccionarios, almacenados en un archivo csv

El sistema permite:

* Alta de países.
* Actualizar tanto población como superficie.
* Buscar países por nombre.
* Filtrar países por continente.
* Filtrar por rango de población.
* Filtrar por rango de superficie.
* Ordenamiento por nombre, población y superficie.
* Generar estadísticas generales.

## Tecnologías utilizadas

* Python 3
* CSV
* Listas
* Diccionarios
* Funciones


## Integrantes

* Aaron Montivero
* Maria Luciana Melana Colavita

## Instrucciones de ejecución

* Ejecutar:
python main.py o py main.py

## Estructura del proyecto

* helpers.py → Funciones genéricas de impresión y de pedir input al usuario.
* datos.py → Lectura y escritura del CSV.
* funcionalidades.py → Toda la lógica de negocio (agregar, actualizar, buscar, filtrar, ordenar, estadísticas).
* main.py → Punto de entrada, contiene solo el menú e importa todo lo demás.
* datos/paises_datos.csv → Dataset
* README.md → documentación


## Estructura del CSV

nombre,poblacion,superficie,continente

Argentina,45376763,2780400,America

## Funcionalidades

1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar países
5. Ordenar países
6. Estadísticas

## Video demostrativo

https://www.youtube.com/watch?v=zhRpSP5i_Vo&feature=youtu.be


