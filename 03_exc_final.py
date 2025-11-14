from datetime import datetime as date
estoque = []
id_inicial= 0

def adicionar_estoque():
    global id_inicial
    global ultimo_registro
    print("-"*20, "Cadastrar Produto", "-"*20)
    nome=input("Digite o nome do produto a ser adicionado ao estoque: ").strip().lower()
    quantidade=int(input("Digite q quantidade a ser adicionada: "))
    unidade=input("Digite a unidade (ex: kg, un): ")
    id_inicial += 1
    id_produto = id_inicial
    data_registro= date.now().strftime("%d/%m/%Y %H:%M:%S")
    ultimo_registro = "Sem alteração"
    preco=float(input("Digite o preço do produto: "))
    estoque_atualizado= {'produto': nome, 'quantidade': quantidade, 'unidade':unidade,'id_produto': id_produto, 'preco': preco, 'data_registro': data_registro, 'ultimo_registro': ultimo_registro }
    estoque.append(estoque_atualizado)

def atualizar_estoque():
    if not estoque:
        print("Não há produtos no estoque!")
        return
    validar = False
    nome_procurar= input("Digite o ID/Nome do item que deseja acrescentar: ").strip().lower()
    try:
        nome_procurar = int(nome_procurar)
    except:
        pass
    for i in estoque:
        if i['produto'] == nome_procurar or i['id_produto'] == nome_procurar:
            achado = i
            i['ultimo_registro'] = date.now().strftime("%d/%m/%Y %H:%M:%S")
            validar = True
            break
    if validar == True:
        print("O produto", achado['produto'], "foi encontrado! A quantidade atual dele é igual a ", achado['quantidade'])
        aumento = int(input("Digite a quantidade que deseja adicionar: "))
        achado['quantidade'] += aumento
    else:print("Id/Nome não encontrado ou digitado incorretamente: ")

def mostrar_tabela():
    if not estoque:
        print("Não há produtos no estoque!")
        return
    print("-"*44, "Produtos Cadastrados","-"*44)
    print(f"{'ID':<4} {'Nome':<20} {'Categoria':<15} {'Preço':<10} {'Qtd':<5} {'Primerio registro':<20} {'Último Registro':<20} {'Status'}")
    print("-"*110)
    for i in estoque:
        status= "Baixo" if i['quantidade'] <= 5 else "OK"
        print(f"{i['id_produto']:<4} {i['produto']:<20} {i['unidade']:<15} {i['preco']:<10} {i['quantidade']:<5} {i['data_registro']:<20} {i['ultimo_registro']:<20}, {status}")

def retirar_estoque():
    if not estoque:
        print("Não há produtos no estoque!")
        return
    validacao= False
    nome_retirar= input("Digite o ID/Nome do item que deseja retirar: ").strip().lower()
    try:
        nome_retirar = int(nome_retirar)
    except:
        pass
    for i in estoque:
        if i['produto'] == nome_retirar or i['id_produto'] == nome_retirar:
            retirar = i
            i['ultimo_registro'] = date.now().strftime("%d/%m/%Y %H:%M:%S")
            validacao = True
            break
    if validacao == True:
        print("O produto", retirar['produto'], "foi encontrado! A quantidade atual dele é igual a ", retirar['quantidade'])
        remover= int(input("Quanto deseja remover do estoque?: "))
        retirar['quantidade'] -= remover
        print("A quantidade final ficou igual a: ", retirar['quantidade'])
    else:print("Id/Nome não encontrado ou digitado incorretamente")

def verificar_saldo():
    if not estoque:
        print("Não há produtos no estoque!")
        return
    nome_verificar=input("Digite o ID/Nome do produto que deseja verificar o saldo: ").strip().lower()
    valid= False
    try:
        nome_verificar = int(nome_verificar)
    except:
        pass
    for i in estoque:
        if i['produto'] == nome_verificar or i['id_produto'] == nome_verificar:
            print("O saldo do item (", i['produto'],") é igual a", i['preco'])
            valid= True
            break
    if valid==True:
        print()
    else:print("Id/Nome não encontrado ou digitado incorretamente")

def remover_estoque():
    if not estoque:
        print("Não há produtos no estoque!")
        return
    verifica = input("Digite o ID/Nome do produto que deseja remover: ").strip().lower()
    validar= False
    try:
        verifica = int(verifica)
    except:
        pass
    for i in estoque:
        if i['produto'] == verifica or i["id_produto"] == verifica:
            estoque.remove(i)
            print("O produto", i['produto'], "foi removido!")
            validar= True
    if validar == True:
        print()
    else: print("Id/Nome não encontrado ou digitado incorretamente")

while True:

    valor= input("""
1-Adicionar um novo item ao estoque.
2-Adicionar produtos.
3-Removover produtos.
4-Remover um item do estoque.
5-Verificar o saldo de um produto.
6-Mostrar a tabela de produtos.
7-Encerrar programa.
""")
    try:
        valor= int(valor)
    except:
        pass

    if valor == 1:
        adicionar_estoque()
    elif valor ==2:
        atualizar_estoque()
    elif valor ==3:
        retirar_estoque()
    elif valor ==4:
        remover_estoque()
    elif valor ==5:
        verificar_saldo()
    elif valor ==6:
        mostrar_tabela()
    elif valor== 7:
        print("Programa encerrando...")
        break
    else:
        print("Número inválido")