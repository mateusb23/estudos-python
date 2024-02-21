import cx_Oracle

# Conecta ao banco de dados Oracle
conn = cx_Oracle.connect('hr/hr@127.0.0.1:1521/XEPDB1')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Executa o SELECT * FROM em uma tabela chamada "exemplo"
cursor.execute("SELECT * FROM employees")

# Obtém os resultados
resultados = cursor.fetchall()

# Exibe os resultados
for linha in resultados:
    print(linha)

# Fecha o cursor e a conexão com o banco de dados
cursor.close()
conn.close()
