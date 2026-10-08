from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):

    livro = session.scalar(
        select(Livro).where(Livro.titulo == titulo)
    )

    if livro is None:
        print("Livro não encontrado.")
        return

    if not livro.disponivel:
        print("O livro já está emprestado.")
        return

    livro.disponivel = False

    session.commit()

    print("Livro emprestado com sucesso.")


def devolver_livro(session, titulo):

    livro = session.scalar(
        select(Livro).where(Livro.titulo == titulo)
    )

    if livro is None:
        print("Livro não encontrado.")
        return

    if livro.disponivel:
        print("O livro já está disponível.")
        return

    livro.disponivel = True

    session.commit()

    print("Livro devolvido com sucesso.")