Objetivo da Atividade:
Desenvolver um programa que simule o módulo de estoque de um ERP, permitindo ao usuário cadastrar, excluir, listar e visualizar relatórios de produtos.
O sistema aplica conceitos de gestão de estoque, como controle de movimentações e geração de relatórios gerenciais.

Contextualização
Nos sistemas ERP (Enterprise Resource Planning), o módulo de estoque é essencial para:
Controlar produtos.
Evitar perdas e faltas de estoque.
Melhorar o planejamento de compras e produção.
Funções típicas do módulo de estoque:
Cadastro de produtos (nome, categoria, preço, quantidade).
Movimentação de estoque (entrada e saída).
Relatórios gerenciais (ex.: evolução do estoque, curva ABC de custos).
Dashboard com gráficos de acompanhamento (opcional, para visualização de categorias, evolução, etc.).
Nesta atividade, você irá criar um mini-ERP de estoque, simulando essas funcionalidades em um programa.

Funcionalidades
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
1-Clone o repositório:
git clone https://github.com/seu-usuario/nome-do-repositorio.git
2-Entre na pasta do projeto:
cd nome-do-repositorio
3-Execute o programa:
python main.py
