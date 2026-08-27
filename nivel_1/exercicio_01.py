def calcular_total(preco, qntd):
    return preco * qntd

def calcular_desconto(total):
    if total < 100:
        return 0
    elif 100 <= total < 500:
        return total * 0.05
    else:
        return total * 0.10

nome = input("Nome: ")
preco = float(input("Preço: "))
qntd = int(input("Quantidade: "))

print(f"Nome: {nome}")
print(f"Preço: {preco}")
print(f"Quantidade: {qntd}")



total = calcular_total(preco, qntd)
print(f"Total: {total}")

desconto = calcular_desconto(total)
print(f"Desconto: {desconto}")

total_final = total - desconto
print(f"Total final: {total_final}")