def calcular_total(preco, qntd):
    return preco * qntd

def calcular_desconto(total):
    if total < 100:
        return 0
    elif 100 <= total < 500:
        return total * 0.05
    else:
        return total * 0.10

produtos = []

continuar = True
while continuar:
    resposta = input("Deseja adicionar um produto ao carrinho? (s/n): ")
    if resposta.lower() == 's':
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        qntd = int(input("Quantidade: "))

        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": qntd
        }

        produtos.append(produto)
    elif resposta.lower() == 'n':
        continuar = False
    else:
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

total = 0
for produto in produtos:
    total += calcular_total(produto["preco"], produto["qntd"])

for produto in produtos:
    subtotal_produto = calcular_total(produto["preco"], produto["qntd"])

    print(f"{produto['nome']} - {produto['qntd']}x - R${subtotal_produto:.2f}")

desconto = calcular_desconto(total)
total_final = total - desconto

print(f"Subtotal: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total final: R$ {total_final:.2f}")
