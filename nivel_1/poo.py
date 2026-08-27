class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self._preco = novo_preco

    @property
    def quantidade(self):
        return self._quantidade
    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if nova_quantidade < 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        self._quantidade = nova_quantidade

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome do produto não pode ser vazio.")
        self._nome = novo_nome

    def adicionar_quantidade(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade a ser adicionada deve ser maior que zero.")
        self.quantidade += quantidade

    def remover_quantidade(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade a ser removida deve ser maior que zero.")
        if quantidade > self.quantidade:
            raise ValueError("Não há produtos suficientes em estoque.")
        self.quantidade -= quantidade

    def esta_disponivel(self):
        if self.quantidade == 0:
            return False
        return True

    def calcular_total(self):
        return self.preco * self.quantidade


def calcular_desconto(total):
    if total < 100:
        return 0
    elif total < 500:
        return total * 0.05
    else:
        return total * 0.10

class Carrinho:

    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.calcular_total()
        return total

produto1 = Produto("Teclado", 150.00, 2)
produto2 = Produto("Mouse", 80.00, 1)

carrinho = Carrinho()

carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)

continuar = True

while continuar:
    resposta = input("Deseja adicionar um produto ao carrinho? (s/n): ")

    if resposta.lower() == "s":
        try:
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))

            produto = Produto(nome, preco, quantidade)             
           

        except ValueError as e:
            print(e)
        else:
            carrinho.adicionar_produto(produto)
        
    elif resposta.lower() == "n":
        continuar = False

    else:
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

for produto in carrinho.produtos:
    subtotal_produto = produto.calcular_total()

    print(
        f"{produto.nome} - "
        f"{produto.quantidade}x - "
        f"R$ {subtotal_produto:.2f}"
    )


subtotal = carrinho.calcular_total()
desconto = calcular_desconto(subtotal)
total_final = subtotal - desconto

print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total final: R$ {total_final:.2f}")