class CarrinhoCompras:
    def __init__(self, data, nome, endereco):
        self.data = data
        self.cliente = Cliente(nome, endereco)# Ex. Composição - recebe a instancia da classe Cliente
        self.produtos = [] #x. Agregação - a cada execução do método addproduto
    def addProduto(self, descricao, preco): #agrega um novo objeto da classe produto ao atributo self.produto(lista)
        produto = Produto(descricao, preco)
        self.produtos.append(produto)
        
    def calcularTotal(self):
        total=0
        for p in self.produtos:
            print(p.descricao, p.preco)
            total+=p.preco
        return total
    

class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

class Produto:
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco