# pagecraft

Paquete python poderoso y fácil de usar que simplifica la creación de paginación en tus aplicaciones

[![Downloads](https://static.pepy.tech/badge/pagecraft)](https://pepy.tech/project/pagecraft)
[![PyPI version](https://badge.fury.io/py/pagecraft.svg)](https://badge.fury.io/py/pagecraft)
![Repo Size](https://img.shields.io/github/repo-size/raulodev/pagecraft)
![PyPI - License](https://img.shields.io/pypi/l/pagecraft)

## Instalando

```console
pip install pagecraft
```

## Tutorial <a name = "usage"></a>

```python
from pagecraft import PageCraft

# crear u obtener una lista de objectos.
lista_de_objetos = [
    "Automatización Eficiente con Python",
    "Explorando las Profundidades de Python",
    "Desarrollo Web Moderno con Python y Flask",
    "Introducción a la Ciencia de Datos con Python",
    "Creando Aplicaciones de Escritorio con Python y PyQt",
    "Aventuras en el Aprendizaje Automático con Python",
    "Python y la Internet de las Cosas (IoT)",
]

# crear una instacia pasando la lista como argumento.
pgcraft = PageCraft(lista_de_objetos)

# Obtener la primera página.
page = pgcraft.page(1)
```

Al imprimir el objeto `page` obtendremos algo como esto

```console
{
    "_": "Page",
    "number": 1,
    "data": [
        "Automatizaci\u00f3n Eficiente con Python",
        "Explorando las Profundidades de Python",
        "Desarrollo Web Moderno con Python y Flask",
        "Introducci\u00f3n a la Ciencia de Datos con Python",
        "Creando Aplicaciones de Escritorio con Python y PyQt"
    ],
    "next_page": 2,
    "prev_page": null,
    "is_exist": true
}
```

## Acceder a los datos:

```python
# Obtener el contenido de la página
page.data

# Devuelve True o False si posee página siguiente
page.has_next_page

# Obtener el número de la página siguiente
page.next_page

# Devuelve True o False si posee página anterior
page.has_prev_page

# Obtener el número de la página anterior
page.prev_page

# Obtener el número de la página actual
page.number
```

## Ampliando la cantidad de datos devueltos

```python
# pasar un número entero como segundo argumento
# al instanciar la clase
pgcraft = PageCraft(lista_de_objetos,10)

page = pgcraft.page(1)
# El page.data contendrá una lista de hasta 10 elementos
```
