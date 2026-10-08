from sqlalchemy import select

from models import Autor, Livro


def popular_banco(session):

    if session.scalar(select(Autor).limit(1)) is not None:
        return

    autor1 = Autor(nome="Machado de Assis", pais="Brasil")
    autor2 = Autor(nome="Clarice Lispector", pais="Brasil")
    autor3 = Autor(nome="J. K. Rowling", pais="Reino Unido")

    livro1 = Livro(
        titulo="Dom Casmurro",
        ano=1899,
        autor=autor1,
        disponivel=True
    )

    livro2 = Livro(
        titulo="Memórias Póstumas de Brás Cubas",
        ano=1881,
        autor=autor1,
        disponivel=False
    )

    livro3 = Livro(
        titulo="A Hora da Estrela",
        ano=1977,
        autor=autor2,
        disponivel=True
    )

    livro4 = Livro(
        titulo="Perto do Coração Selvagem",
        ano=1943,
        autor=autor2,
        disponivel=True
    )

    livro5 = Livro(
        titulo="Harry Potter e a Pedra Filosofal",
        ano=1997,
        autor=autor3,
        disponivel=False
    )

    livro6 = Livro(
        titulo="Harry Potter e a Câmara Secreta",
        ano=1998,
        autor=autor3,
        disponivel=True
    )

    session.add_all([
        autor1,
        autor2,
        autor3,
        livro1,
        livro2,
        livro3,
        livro4,
        livro5,
        livro6
    ])

    session.commit()