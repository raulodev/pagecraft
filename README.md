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

## Tutorial

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

## PageCraftAlchemy Tutorial

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

from pagecraft.alchemy import PageCraftAlchemy

Base = declarative_base()

class Frases(Base):
    __tablename__ = "frases"
    id = Column(Integer, primary_key=True)
    texto = Column(String)

    def __str__(self):
        return self.texto

engine = create_engine("sqlite:///:memory:")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for i in range(1, 21):
    frase = Frases(texto=f"Frase {i}")
    session.add(frase)

session.commit()

query = session.query(Frases)

alchemycraft = PageCraftAlchemy(query)

# Get first page
page = alchemycraft.page(1)
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

alchemycraft = PageCraftAlchemy(query , 20)
```

## Release Notes (0.0.6)

- add PageCraftAlchemy : create easy pagination for [Sqlalchemy ORM](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- now there are 10 items returned by default
