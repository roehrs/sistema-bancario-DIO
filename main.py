import getpass

def exibir_menu():
    menu = """
    [c] Cadastrar Usuário
    [d] Depositar
    [s] Sacar
    [t] Transferir
    [e] Extrato
    [q] Sair

    => """
    return input(menu)

def autenticar_usuarios(usuarios):
    usuario = input("Usuário: ")
    senha = getpass.getpass("Senha: ")

    if usuario in usuarios and usuarios[usuario]['senha'] == senha:
        print("Autenticação bem-sucedida!")
        return usuario
    else:
        print("Usuário ou senha incorretos.")
        return None

def cadastrar_usuario(usuarios):
    novo_usuario = input("Novo usuário: ")
    if novo_usuario in usuarios:
        print("Usuário já existe.")
        return usuarios

    nova_senha = getpass.getpass("Nova senha: ")
    usuarios[novo_usuario] = {"senha": nova_senha, "saldo": 0, "extrato": [], "numero_saques": 0}
    print("Usuário cadastrado com sucesso!")
    return usuarios

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def transferir(saldo, extrato, usuarios, usuario_atual):
    destinatario = input("Informe o usuário destinatário: ")
    if destinatario not in usuarios:
        print("Usuário destinatário não encontrado.")
        return saldo, extrato

    valor = float(input("Informe o valor da transferência: "))
    if valor > 0 and valor <= saldo:
        saldo -= valor
        usuarios[destinatario]['saldo'] += valor
        extrato.append(f"Transferência para {destinatario}: R$ {valor:.2f}")
        usuarios[destinatario]['extrato'].append(f"Transferência de {usuario_atual}: R$ {valor:.2f}")
    else:
        print("Operação falhou! Saldo insuficiente ou valor inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else "\n".join(extrato))
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    usuarios = {
        "user1": {"senha": "1234", "saldo": 0, "extrato": [], "numero_saques": 0},
        "user2": {"senha": "5678", "saldo": 0, "extrato": [], "numero_saques": 0}
    }
    LIMITE_SAQUES = 3
    limite = 500

    while True:
        opcao = exibir_menu()

        if opcao == "c":
            usuarios = cadastrar_usuario(usuarios)
        elif opcao == "d":
            usuario_atual = autenticar_usuarios(usuarios)
            if usuario_atual:
                usuarios[usuario_atual]['saldo'], usuarios[usuario_atual]['extrato'] = depositar(usuarios[usuario_atual]['saldo'], usuarios[usuario_atual]['extrato'])
        elif opcao == "s":
            usuario_atual = autenticar_usuarios(usuarios)
            if usuario_atual:
                usuarios[usuario_atual]['saldo'], usuarios[usuario_atual]['extrato'], usuarios[usuario_atual]['numero_saques'] = sacar(
                    usuarios[usuario_atual]['saldo'], usuarios[usuario_atual]['extrato'], usuarios[usuario_atual]['numero_saques'], LIMITE_SAQUES, limite)
        elif opcao == "t":
            usuario_atual = autenticar_usuarios(usuarios)
            if usuario_atual:
                usuarios[usuario_atual]['saldo'], usuarios[usuario_atual]['extrato'] = transferir(
                    usuarios[usuario_atual]['saldo'], usuarios[usuario_atual]['extrato'], usuarios, usuario_atual)case
        elif opcao == "e":
            usuario_atual = autenticar_usuarios(usuarios)
            if usuario_atual:
                exibir_extrato(usuarios[usuario_atual]['saldo'], usuarios[usuario_atual]['extrato'])
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
