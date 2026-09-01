class Livro:
    def __init__(self, titulo, autor, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.quantidade = quantidade

    def exibir_informacoes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Quantidade Disponível: {self.quantidade}"

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, novo_titulo):
        if not novo_titulo:
            raise ValueError("O título do livro não pode ser vazio.")
        self._titulo = novo_titulo

    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, novo_autor):
        if not novo_autor:
            raise ValueError("O autor do livro não pode ser vazio.")
        self._autor = novo_autor

    @property
    def quantidade(self):
        return self._quantidade
    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if nova_quantidade < 0:
            raise ValueError("A quantidade de livros não pode ser negativa.")
        self._quantidade = nova_quantidade

    def emprestar(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade a ser emprestada deve ser maior que zero.")
        if quantidade > self.quantidade:
            raise ValueError("Não há livros suficientes disponíveis para empréstimo.")
        self.quantidade -= quantidade

    def devolver(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade a ser devolvida deve ser maior que zero.")
        self.quantidade += quantidade

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro (self, livro):
        if not isinstance(livro, Livro):
            raise ValueError("O objeto adicionado deve ser uma instância da classe Livro.")
        self.livros.append(livro)
