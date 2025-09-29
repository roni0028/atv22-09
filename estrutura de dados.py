"""
Sistema de Gerenciamento de Produtos

Este módulo implementa um sistema simples para gerenciar produtos e suas informações.
Contém duas classes principais:
- Product: Representa um produto individual com nome, preço e quantidade
- ProductList: Gerencia uma coleção de produtos com operações matemáticas

Autor: Ronicarlos Ferreira 37012676
Data: 27/09/2025
"""

class Product:
    """
    Classe que representa um produto com suas características básicas.
    
    Esta classe encapsula as informações de um produto, incluindo nome,
    preço e quantidade disponível.
    
    Attributes:
        name (str): Nome do produto
        price (float): Preço unitário do produto
        quantity (int): Quantidade disponível do produto
    """
    
    def __init__(self, name, price, quantity):
        """
        Inicializa um novo produto.
        
        Args:
            name (str): Nome do produto
            price (float): Preço unitário do produto
            quantity (int): Quantidade disponível do produto
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """
        Retorna uma representação em string do produto.
        
        Returns:
            str: String formatada com as informações do produto
        """
        return f"Produto: {self.name}, Preço: {self.price}, Quantidade: {self.quantity}"

class ProductList:
    """
    Classe que gerencia uma coleção de produtos.
    
    Esta classe implementa uma lista personalizada de produtos com métodos
    especiais para operações matemáticas e manipulação da lista.
    
    Attributes:
        products (list): Lista contendo objetos da classe Product
    """
    
    def __init__(self):
        """
        Inicializa uma nova lista de produtos vazia.
        """
        self.products = []
    
    def add_product(self, name, price, quantity):
        """
        Adiciona um novo produto à lista.
        
        Args:
            name (str): Nome do produto
            price (float): Preço unitário do produto
            quantity (int): Quantidade disponível do produto
        """
        self.products.append(Product(name, price, quantity))
    
    def __str__(self):
        """
        Retorna uma representação em string da lista de produtos.
        
        Returns:
            str: String com todos os produtos, um por linha
        """
        return "\n".join(str(product) for product in self.products)
    
    def __len__(self):
        """
        Retorna o número de produtos na lista.
        
        Returns:
            int: Quantidade de produtos na lista
        """
        return len(self.products)
    
    def __getitem__(self, index):
        """
        Permite acesso aos produtos por índice usando notação de lista.
        
        Args:
            index (int): Índice do produto desejado
            
        Returns:
            Product: O produto no índice especificado
        """
        return self.products[index]
    
    def __setitem__(self, index, product):
        """
        Permite modificar produtos por índice usando notação de lista.
        
        Args:
            index (int): Índice do produto a ser modificado
            product (Product): Novo produto para substituir o existente
        """
        self.products[index] = product
    
    def __delitem__(self, index):
        """
        Permite remover produtos por índice usando notação de lista.
        
        Args:
            index (int): Índice do produto a ser removido
        """
        del self.products[index]
        
    def __total__(self):
        """
        Calcula o valor total de todos os produtos (preço × quantidade).
        
        Returns:
            float: Valor total de todos os produtos na lista
        """
        return sum(product.price * product.quantity for product in self.products)
    
    def __media__(self):
        """
        Calcula o valor médio dos produtos baseado no valor total.
        
        Returns:
            float: Valor médio dos produtos
        """
        return self.__total__() / len(self.products)
    
    def __maior_valor__(self):
        """
        Encontra o produto com maior preço unitário.
        
        Returns:
            Product: O produto com maior preço unitário
        """
        return max(self.products, key=lambda x: x.price)
    
    def __menor_valor__(self):
        """
        Encontra o produto com menor preço unitário.
        
        Returns:
            Product: O produto com menor preço unitário
        """
        return min(self.products, key=lambda x: x.price)

    def __total_itens_diferentes__(self):
        """
        Calcula o total de itens diferentes na lista.
        
        Returns:
            int: Total de itens diferentes na lista
        """
        return len(set(product.name for product in self.products))
# Main
if __name__ == "__main__":
    # Criando a lista de produtos
    product_list = ProductList()
    product_list.add_product("Arroz", 10.0, 10)
    product_list.add_product("Feijão", 20.0, 20)
    product_list.add_product("Leite", 30.0, 30)
    product_list.add_product("Pão", 40.0, 40)
    product_list.add_product("Café", 50.0, 50)

    # Exibindo os produtos
    for product in product_list:
        print(f"Produto: {product.name} | Quantidade: {product.quantity} | Preço: {product.price}")
    
    # Exibindo o resumo da compra
    print("\n")
    print("-" * 5 + "  Resumo da Compra  " + "-" * 5)
    print(f"Total de itens diferentes: {product_list.__total_itens_diferentes__()}")
    print(f"Total: {product_list.__total__():.2f}")
    print(f"Média: {product_list.__media__():.2f}")
    print(f"Item de maior valor: {product_list.__maior_valor__().name} | Quantidade: {product_list.__maior_valor__().quantity} | Preço: {product_list.__maior_valor__().price}")
    print(f"Item de menor valor: {product_list.__menor_valor__().name} | Quantidade: {product_list.__menor_valor__().quantity} | Preço: {product_list.__menor_valor__().price}")
    print("-" * 20 + "\n")