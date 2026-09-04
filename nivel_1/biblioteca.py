class Livro:
    def __init__(self, titulo, autor, quantidade):
        self.titulo = titulo
        self.autor = autor

        if quantidade < 0:
            raise ValueError("A quantidade de livros não pode ser negativa.")
        self._quantidade = quantidade

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

    def emprestar(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade a ser emprestada deve ser maior que zero.")
        if quantidade > self.quantidade:
            raise ValueError("Não há livros suficientes disponíveis para empréstimo.")
        self._quantidade -= quantidade

    def devolver(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade a ser devolvida deve ser maior que zero.")
        self._quantidade += quantidade

    def __repr__(self):
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', quantidade={self.quantidade})"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro (self, livro):
        if not isinstance(livro, Livro):
            raise TypeError("O objeto adicionado deve ser uma instância da classe Livro.")
        if any(l.titulo == livro.titulo for l in self.livros):
            raise ValueError("Um livro com este título já existe na biblioteca.")
        self.livros.append(livro)

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None

    def emprestar_livro(self, titulo, quantidade):
        livro = self.buscar_livro(titulo)
        if livro is None:
            raise ValueError("Livro não encontrado na biblioteca.")
        livro.emprestar(quantidade)

    def devolver_livro(self, titulo, quantidade):
        livro = self.buscar_livro(titulo)
        if livro is None:
            raise ValueError("Livro não encontrado na biblioteca.")
        livro.devolver(quantidade)

    def listar_livros(self):
        return self.livros.copy()



livro1 = Livro("1984", "George Orwell", 5)

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)

lista = biblioteca.listar_livros()

lista[0].emprestar(2)

print(livro1.quantidade)
print(biblioteca.livros[0].quantidade)
print(lista[0].quantidade)