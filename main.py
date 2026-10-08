from database import criar_banco, nova_sessao

from seed import popular_banco

from consultas import (
    listar_livros,
    listar_livros_disponiveis,
    buscar_livros_por_titulo,
    listar_livros_por_autor
)

from operacoes import (
    emprestar_livro,
    devolver_livro
)


criar_banco()

with nova_sessao() as session:

    popular_banco(session)

    print("\nTodos os livros:")
    listar_livros(session)

    print("\nLivros disponíveis:")
    listar_livros_disponiveis(session)

    print("\nBusca por parte do título:")
    buscar_livros_por_titulo(session, "a")

    print("\nLivros de um autor:")
    listar_livros_por_autor(
        session,
        "Machado de Assis"
    )

    print("\nEmprestando um livro:")
    emprestar_livro(
        session,
        "Dom Casmurro"
    )

    print("\nDevolvendo um livro:")
    devolver_livro(
        session,
        "Dom Casmurro"
    )