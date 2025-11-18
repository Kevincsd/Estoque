from datetime import datetime as date
import matplotlib.pyplot as plt
import sqlite3
DB_PATH= 'estoque.db'
conn = sqlite3.connect("estoque.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
);
""")

cur.execute("SELECT * FROM items")
linhas = cur.fetchall()

estoque = []
id_inicial = 0

for i in linhas:
    id_produto, nome, categoria, preco, quantidade = i
    data_registro= date.now().strftime("%d/%m/%Y %H:%M:%S")
    estoque.append({
        'produto': nome,
        'quantidade': quantidade,
        'unidade': categoria,
        'id_produto': id_produto,
        'preco': preco,
        'data-registro': data_registro
    })
    if id_produto > id_inicial:
        id_inicial = id_produto

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
    
    cur.execute("""
        INSERT INTO items (nome, categoria, preco, quantidade)
        VALUES (?, ?, ?, ?)
    """, (nome, unidade, preco, quantidade))
    
    conn.commit()

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

        cur.execute("""
            UPDATE items
            SET quantidade = ?
            WHERE id = ? OR nome = ?
        """, (achado['quantidade'], achado['id_produto'], achado['produto']))

        conn.commit()
        
    else:print("Id/Nome não encontrado ou digitado incorretamente: ")

def mostrar_tabela():
    cur.execute("SELECT * FROM items")
    linhas = cur.fetchall()
    if not linhas:
        print("Não há produtos no estoque!")
        return
    print("-"*25, "Produtos Cadastrados","-"*23)
    print(f"{'ID':<4} {'Nome':<20} {'Categoria':<15} {'Preço':<10} {'Qtd':<5} {'Status'}")
    print("-"*70)
    for linha in linhas:
        id_produto, nome, categoria, preco, quantidade = linha
        status = "Baixo" if quantidade <= 5 else "OK"
        print(f"{id_produto:<4} {nome:<20} {categoria:<15} {preco:<10.2f} {quantidade:<5} {status}")
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
        cur.execute("""
            UPDATE items
            SET quantidade = ?
            WHERE id = ?
        """, (retirar['quantidade'], retirar['id_produto']))
        conn.commit()
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
            cur.execute("DELETE FROM items WHERE id = ?", (i['id_produto'],))
            conn.commit()
            estoque.remove(i)
            print("O produto", i['produto'], "foi removido!")
            validar= True
    if validar == True:
        print()
    else: print("Id/Nome não encontrado ou digitado incorretamente")

def dashboard():
    categorias={}
    for i in estoque:
        categorias[i["unidade"]] = categorias.get(i["unidade"], 0) + i["quantidade"]
    plt.figure(figsize=(8, 6))
    plt.pie(categorias.values(), 
            labels=categorias.keys(), 
            autopct="%1.1f%%")
    plt.title("Distribuição do Estoque por Categoria")
    plt.show()
        
    plt.figure(figsize=(8, 6))
    plt.bar(categorias.keys(), 
            categorias.values(), 
            color='skyblue')
    plt.title("Quantidade Total por Categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Quantidade")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()

    produtos_abc = []
    for p in estoque:
        valor_total = p["preco"] * p["quantidade"]
        produtos_abc.append((p["produto"], valor_total))

    produtos_abc.sort(key=lambda x: x[1], reverse=True)

    nomes = [p[0] for p in produtos_abc]
    valores = [p[1] for p in produtos_abc]

    soma_total = sum(valores)
    acumulado = []
    soma = 0
    for v in valores:
        soma += v
        acumulado.append((soma / soma_total) * 100)
    
    plt.figure(figsize=(10, 5))
    plt.bar(nomes, valores, color="lightgreen")
    plt.plot(nomes, acumulado, color="red", marker="o")
    plt.xlabel("Produtos")
    plt.ylabel("Valor em Estoque (R$)")
    plt.title("Curva ABC")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()

while True:

    valor= input("""
1-Adicionar um novo item ao estoque.
2-Adicionar produtos.
3-Removover produtos.
4-Remover um item do estoque.
5-Dashboard
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
        dashboard()
    elif valor ==6:
        mostrar_tabela()
    elif valor== 7:
        print("Programa encerrando...")
        break
    else:
        print("Número inválido")