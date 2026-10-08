# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

1. Para que serve o campo `disponivel` em `Livro`?
o campo disponivel informa se o livro está disponível para empréstimo. quando o livro é emprestado fica False; quando é devolvido volta para True.

2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?
pq o commit salva a alteraçao no banco de dados.

3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?
Na consulta dos livros, usando:
livro.autor.nome
e também na consulta dos livros de um autor, usando:
autor.livros