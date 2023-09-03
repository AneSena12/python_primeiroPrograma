opcao = int(input("Informe uma opcao: [1] Extrato [2] Depositar [3] Sacar [0] Sair:"))
saldo = 500


if opcao == 1:
    print(f"Seu saldo é de {saldo}.")

elif opcao == 2:
    valor_deposito = float(input("Informe o valor que você deseja depositar:"))
    saldo += valor_deposito
    print(f'Depósito realizado com sucesso! Seu novo saldo é de {saldo}.')

elif opcao == 3:
    saque = float(input("Informe o valor do saque:"))
    if saldo >= saque:
        print("Valor sacado!")
        print("Retire o seu dinheiro na boca do caixa.")
    
    else:
        print("Saldo Insuficiente!")
    
elif opcao == 0:
    SystemExit

print("Obrigador por ser nosso cliente, tenha um bom dia!")

