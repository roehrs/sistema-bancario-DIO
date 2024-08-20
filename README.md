# Sistema Bancário Simples

Este é um programa simples de sistema bancário em Python que permite aos usuários realizar operações básicas como depósito, saque, transferência e exibição de extrato. Além disso, é possível cadastrar novos usuários no sistema.

Projeto desenvolvido como parte do desenvolvimento da trilha de Python da DIO.

Criado o projeto base conforme o desafio e adicionado novas funcionalidades.

- **Cadastrar Usuário**: Permite adicionar novos usuários ao sistema.
- **Autenticação de Usuário**: Os usuários precisam se autenticar com um nome de usuário e senha.
- **Depósito**: Permite que os usuários depositem dinheiro em suas contas.
- **Saque**: Permite que os usuários saquem dinheiro de suas contas, respeitando limites diários e de saldo.
- **Transferência**: Permite que os usuários transfiram dinheiro entre contas.
- **Extrato**: Exibe o histórico de transações e o saldo atual.

## Como Usar

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/sistema-bancario-simples.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd sistema-bancario-simples
    ```

3. Execute o programa:
    ```bash
    python sistema_bancario.py
    ```

## Estrutura do Código

- **Funções Modulares**: O código é dividido em funções para melhorar a organização e a reutilização.
- **Autenticação**: Implementa um sistema de login com autenticação por senha.
- **Transações**: Funções para depósito, saque e transferência de dinheiro.
- **Extrato**: Função para exibir o histórico de transações e o saldo atual.

 ## 📋 Menu de Opções

- `[c] Cadastrar Usuário`
- `[d] Depositar`
- `[s] Sacar`
- `[t] Transferir`
- `[e] Extrato`
- `[q] Sair`


## Exemplo de Uso

```plaintext
Usuário: user1
Senha: ****
Autenticação bem-sucedida!

[d] Depositar
[s] Sacar
[t] Transferir
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 1000
Depósito realizado com sucesso!

[d] Depositar
[s] Sacar
[t] Transferir
[e] Extrato
[q] Sair

=> e

================ EXTRATO ================
Depósito: R$ 1000.00

Saldo: R$ 1000.00
==========================================
```

## 📝 Notas

- O programa utiliza a biblioteca `getpass` para ocultar a senha durante a digitação.
- O limite de saques diários é configurado como 3 e o limite de valor para saque é R$ 500,00.
- As senhas dos usuários são armazenadas em texto simples para simplificação. Em um sistema real, recomenda-se o uso de hashing para armazenar senhas de forma segura.

## 📌 Requisitos

- Python 3

## 📧 Contato

Para mais informações, entre em contato com diogoroehrs@gmail.com
