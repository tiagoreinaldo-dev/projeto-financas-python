# ==== Menu do app ====
import yfinance as yf

saldo = 0

historico = []

investimentos = []

while True:

    print("Controle de Investimentos")

    print()
    print("1 - Ver Saldo")
    print("2 - Adicionar Receita")
    print("3 - Adicionar Despeza")
    print("4 - Investimentos")
    print("5 - Ver Historico")
    print("6 - Sair")

    opcao = input("Escolha uma opçao: ")

# ==== Inteligencia do menu ====

# ==== 1. Saldo ====

    if opcao == "1":
      print(f"Seu saldo e: R${saldo:.2f}")

# ==== 2. Receitas ====

    elif opcao == "2":

        receita = float(input("Quanto voce Recebeu? R$ "))

        saldo = saldo + receita 

        historico.append({
            "tipo": "receita",
            "Valor": receita
        })

        print("Receita Adicionada!!!")

# === 3. Despesas ====

    elif opcao == "3":

        despesa = float(input("quanto voce gastou? R$ "))

        categoria = input("Categoria da despesa: ")

        saldo = saldo - despesa

        historico.append({
            "tipo": "despesa",
            "Valor": despesa,
            "categoria": categoria
        })

        print("Despesa Adicionada!!!")

# === 4. Meus Investimentos ====

    elif opcao == "4":
        print("Meus Investimentos")

        codigo = input("Digite o codigo do investimento: ")

        quantidade = int(input("Digite a quantidade:"))

        preco = float(input("Digite o preço de compra: R$R$"))

        valor_investido = quantidade * preco

        investimentos.append({
            "codigo": codigo,
            "quantidade": quantidade,
            "preco": preco,
            "valor_investido": valor_investido
        })

        print(f"Valor investido; R${valor_investido:.2f}")

        print(f"Investimento {codigo} com {quantidade} unidades adicionadas!")

        print("Investimentos cadastrados:")

        for investimento in investimentos:

    # ==== Parte Responsavel por pegar o preço atual do investimento ====        

            ticker = investimento['codigo'] + ".SA"

            dados = yf.Ticker(ticker)

            preco_atual = dados.history(period="1d")["Close"].iloc[-1]
            print(f"{investimento['codigo']} | Quantidade:{investimento['quantidade']} | Preço: R${investimento['preco']} | Investido: R${investimento['valor_investido']:.2f}")

            print(f"Preço atual: R${preco_atual:.2f}")

            valor_atual = investimento["quantidade"] * preco_atual
            print(f"Valor atual: R${valor_atual:.2f}")

    # ==== Calcular Lucro e Prejuizo ====
        
            resultado = valor_atual - investimento["valor_investido"]
            print(f"Resultado: R${resultado:.2f}")

            if resultado > 0:
                print("Lucro")

            elif resultado < 0:
                print("Prejuizo")

            else:
                print("Sem lucro nem prejuizo")    




# === 5. Historico de Transações ====

    elif opcao == "5":
        print("Historico de Transações:")

        if not historico:
            print("Nenhuma transação registrada.")

        for item in historico:

            if item["tipo"] == "receita":
                print(f"Receita: R${item['Valor']:.2f}")

            elif item["tipo"] == "despesa":
                print(f"Despesa: R${item['Valor']:.2f} | categoria:{item['categoria']}")    

# === 6. Sair do programa ====

    elif opcao =="6":
        print("Saindo do programa.") 

        break

    else:
        print("Opçao invalida")      



                  