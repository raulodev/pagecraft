# pagecraft

Powerful package and easy to use that simplifies the creation of pagination in your apps

[![Downloads](https://static.pepy.tech/badge/pagecraft)](https://pepy.tech/project/pagecraft)
[![PyPI version](https://badge.fury.io/py/pagecraft.svg)](https://badge.fury.io/py/pagecraft)
![Repo Size](https://img.shields.io/github/repo-size/raulodev/pagecraft)
![PyPI - License](https://img.shields.io/pypi/l/pagecraft)

## Installing

```console
pip install pagecraft
```

## Tutorial <a name = "usage"></a>

```python
from pagecraft import PageCraft

lista_de_objetos = [
    "Automatización Eficiente con Python",
    "Explorando las Profundidades de Python",
    "Desarrollo Web Moderno con Python y Flask",
    "Introducción a la Ciencia de Datos con Python",
    "Creando Aplicaciones de Escritorio con Python y PyQt",
    "Aventuras en el Aprendizaje Automático con Python",
    "Python y la Internet de las Cosas (IoT)",
]


pgcraft = PageCraft(lista_de_objetos)

# Get first page
page = pgcraft.page(1)
```

when we print the `page` we get this

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

## Accessing data:

```python
# Get data from page
page.data

# True or False if next page exists
page.has_next_page

# Get the next page number
page.next_page

# True or False if prev page exists
page.has_prev_page

# Get the prev page number
page.prev_page

# Get the current page number
page.number
```

## Extend the data returned

```python
# set integer number as second argument
pgcraft = PageCraft(lista_de_objetos,20)
```
