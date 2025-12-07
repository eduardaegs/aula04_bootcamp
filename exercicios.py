# Crie uma estrutura de dados que armazene informações de título, autor e publicação de livros.
from typing import List, Dict, Any

livros: Dict[str, Any] = {
    'Título': 'Menina bonita do laço de fita',
    'Autor': 'Ana Maria Machado',
    'Publicação': 1986
}

for i, livro in enumerate(livros):
    print(f'{livro}: {livros[livro]}')