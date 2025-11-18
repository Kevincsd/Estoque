# Estoque

Objetivo da Atividade

Desenvolver um programa que simule o módulo de estoque de um ERP, permitindo ao usuário cadastrar, excluir, listar e visualizar relatórios de produtos.

O sistema aplica conceitos de gestão de estoque, como controle de movimentações e geração de relatórios gerenciais.

O sistema oferece um menu interativo com as seguintes opções:

Cadastrar produto

Informar: nome, categoria, preço e quantidade inicial.

Armazenar os dados em uma estrutura (lista ou banco de dados SQLite).

Excluir produto

Permitir remover um produto pelo nome ou ID.

Atualizar tanto a lista em memória quanto o banco de dados.

Retirar do estoque

Permitir movimentações de saída de produtos.

Atualizar quantidade disponível e registrar a data/hora da última movimentação.

Mostrar relatório de produtos cadastrados

Listar todos os produtos com: nome, categoria, preço, quantidade.

Destacar produtos com estoque baixo (quantidade menor que 5).

Sair do programa

Encerrar a execução.

Tecnologias Utilizadas

Linguagem: Python 3

Banco de dados: SQLite

Biblioteca para gráficos: matplotlib

Como Executar

Clone o repositório:

git clone https://github.com/seu-usuario/nome-do-repositorio.git


Entre na pasta do projeto:

cd nome-do-repositorio


Execute o programa:

python main.py
