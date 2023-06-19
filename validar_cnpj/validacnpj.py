def validar_cnpj(cnpj):
    cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")  # Remove caracteres especiais
    if len(cnpj) != 14 or not cnpj.isnumeric():
        return False

    # Verifica se todos os dígitos são iguais (caso contrário, o CNPJ é inválido)
    if len(set(cnpj)) == 1:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cnpj[i]) * (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)[i] for i in range(12))
    digito1 = 11 - soma % 11
    if digito1 >= 10:
        digito1 = 0

    # Calcula o segundo dígito verificador
    soma = sum(int(cnpj[i]) * (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)[i] for i in range(13))
    digito2 = 11 - soma % 11
    if digito2 >= 10:
        digito2 = 0

    # Verifica se os dígitos verificadores são iguais aos do CNPJ
    return cnpj[-2:] == str(digito1) + str(digito2)
