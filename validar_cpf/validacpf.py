def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")  # Remove caracteres especiais
    if len(cpf) != 11 or not cpf.isnumeric():
        return False

    # Verifica se todos os dígitos são iguais (caso contrário, o CPF é inválido)
    if len(set(cpf)) == 1:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    # Verifica se os dígitos verificadores são iguais aos do CPF
    return cpf[-2:] == str(digito1) + str(digito2)