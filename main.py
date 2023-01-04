import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0202',
    database='vendas'
)
cursor = conexao.cursor()

print("Olá, QUAL OPERAÇÃO DESEJA FAZER")
escolha= input("1 = adicionar ITEM vendido \n"
               "2 = deletar Item \n"
               "3 = atualizar o Valor de algum item \n"
               "4 = Mostrar TOTAL DE VENDAS\n")

if escolha == '1':
    id_produto = input(" ITEM : \n")
    valor = input(" Valor do produto: \n")

    comando = f'INSERT INTO vendas (id_produto , valor) VALUES ("{id_produto}", {valor})'
    cursor.execute(comando)
    conexao.commit()  # edita o banco de dados
elif escolha == '2':
    id_produto = input("QUal item será deletado? \n")
    comando = f'DELETE FROM vendas  WHERE id_produto = "{id_produto}" '
    cursor.execute(comando)
    conexao.commit() #edita o banco de dados
elif escolha == '3':
    id_produto = input(" qual item será atualizado: \n")
    valor = input(" qual é o novo valor desse ITEM? \n")
    comando = f'UPDATE vendas SET valor = {valor} WHERE id_produto = "{id_produto}"'
    cursor.execute(comando)
    conexao.commit() #edita o banco de dados
elif escolha == '4':
    cursor.execute("SELECT SUM(valor) FROM vendas")
    print(cursor.fetchall()[0][0])  # ler o banco de dados

cursor.close()
conexao.close()
