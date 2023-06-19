import os
import psycopg2
import validar_cpf.validacpf as validacpf
import validar_cnpj.validacnpj as validacnpj

def connection():
    # Conectar ao banco de dados
    db_name = 'neoway'
    db_user = 'postgres'
    db_password = 'postgres'
    db_host =  os.environ.get('DB_HOST', 'localhost')
    db_port = '5432'

    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    return conn


def validarcpf():

# Configurações de conexão com o banco de dados
  conn = connection()
# Query para extrair o CPF da tabela
  query = "SELECT cpf FROM dados"
  
  cpf_validos = 0
  cpf_invalidos = 0  
  cnpj_validos = 0
  cnpj_invalidos = 0

  try:
    # Criação de um cursor
    cursor = conn.cursor()

    # Execução da consulta
    cursor.execute(query)
    certificados_rows = cursor.fetchall()

    # Iteração sobre os CPFs e CNPJs retornados
    for certificado_row in certificados_rows:
            certificado = certificado_row[0]  # Extrai o CPF da tupla retornada
            if len(certificado) <= 11: 
            # Chamada da função de validação do CPF
              if validacpf.validar_cpf(certificado):
                  print(f"CPF {certificado} é válido.")
                  cpf_validos += 1
              else:
                  print(f"CPF {certificado} é inválido.")
                  cpf_invalidos += 1
            elif len(certificado) > 11:
                if validacnpj.validar_cnpj(certificado):
                  print(f"CNPJ {certificado} é válido.")
                  cnpj_validos += 1
                else:
                  print(f"CNPJ {certificado} é inválido.")
                  cnpj_invalidos += 1
            
    # Fechamento do cursor e da conexão
    cursor.close()
    conn.close()
    print("***********************************************")
    print(f"TOTAL CPF VÁLIDOS:{cpf_validos}")
    print(f"TOTAL CPF INVÁLIDOS:{cpf_invalidos}")
    print("***********************************************")
    print(f"TOTAL CNPJ VÁLIDOS:{cnpj_validos}")
    print(f"TOTAL CNPJ INVÁLIDOS:{cnpj_invalidos}")

  except (Exception, psycopg2.Error) as error:
    print("Erro ao conectar ou executar a consulta:", error)


def clean_cpf_cnpj(certificado):
    certificado = certificado.replace(".", "").replace("/", "").replace("-", "")
    return certificado


def ticket_medio_float(num):
    if num == 'NULL':
        ticket_medio = 0.0
    else:
        ticket_medio = float(num.replace(',', '.'))
    return ticket_medio


def persistir_dados_arquivo(nome_arquivo):
    conn = connection()
    query = '''CREATE TABLE IF NOT EXISTS dados
               (id SERIAL PRIMARY KEY,
                cpf varchar(20),
                private int,
                incompleto int,
                dt_ultima_compra varchar(10),
                ticket_medio money, 
                ticket_ultima_compra money,
                loja_mais_frequente varchar(18),
                loja_ultima_compra varchar(18))'''

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()
    cursor.execute(query)

    # Ler o arquivo e persistir os dados
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            dados = linha.split()
            if len(dados) == 8:
                cpf, private, incompleto, dt_ultima_compra, ticket_medio, ticket_ultima_compra, loja_mais_frequente, loja_ultima_compra = dados[0], dados[1], dados[2], dados[3], dados[3], dados[5], dados[6], dados[7].strip()

                cpf = clean_cpf_cnpj(dados[0]) # retirada de traços pontos e barra
                ticket_medio = ticket_medio_float(dados[4])
                ticket_ultima_compra = ticket_medio_float(dados[5])
                loja_mais_frequente = clean_cpf_cnpj(dados[6])
                loja_ultima_compra = clean_cpf_cnpj(dados[7])

                cursor.execute("INSERT INTO dados (cpf, private, incompleto, dt_ultima_compra, ticket_medio, ticket_ultima_compra, loja_mais_frequente, loja_ultima_compra) VALUES (%s, %s, %s,%s, %s, %s,%s, %s)",
                               (cpf, private, incompleto, dt_ultima_compra, ticket_medio, ticket_ultima_compra, loja_mais_frequente, loja_ultima_compra))

    # Confirmar as alterações
    conn.commit()

    # Fechar a conexão com o banco de dados
    conn.close()


if __name__ == '__main__':
    # Chamada do serviço
    persistir_dados_arquivo('data/base_teste.txt')

    # Validar e listar CPF/CNPJ
    validarcpf()