# ==== Menu dessa bagaça ====

saldo = 0

while True:

    print("Controle de Investimentos")

    print()
    print("1 - Ver Saldo")
    print("2 - Adicionar Receita")
    print("3 - Adicionar Despeza")
    print("4 - Investimentos")
    print("5 -  Sair")

    opcao = input("Escolha uma opçao: ")

# ==== Inteligencia do menu ====

    if opcao == "1":
      print(f"Seu saldo e: R${saldo:.2f}")

    elif opcao == "2":
        receita = float(input("Quanto voce Recebeu? R$ "))
        saldo = saldo + receita                
        print("Receita Adicionada!!!.")

    elif opcao == "3":
        print("Voce escolheu adicionaruma despesa.")

    elif opcao == "4":
        print("Voce escolheu investimentos.")

    elif opcao =="5":
        print("Saindo do programa.") 
        break

    else:
        print("Opçao invalida")      



                  